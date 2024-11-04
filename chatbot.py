import os
from transformers import T5Tokenizer, T5ForConditionalGeneration
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone

# Initialize Pinecone instance
pc = Pinecone(api_key='89eeb534-da10-4068-92f7-12eddeabe1e5')

# Check if the index exists; if not, create it
index_name = 'abstractive-question-answering'
index = pc.Index(index_name)

def load_models():
    retriever = SentenceTransformer("flax-sentence-embeddings/all_datasets_v3_mpnet-base")
    tokenizer = T5Tokenizer.from_pretrained('t5-base')
    generator = T5ForConditionalGeneration.from_pretrained('t5-base')
    return retriever, generator, tokenizer

retriever, generator, tokenizer = load_models()

def query_pinecone(query, top_k=1):
    xq = retriever.encode([query]).tolist()
    xc = index.query(vector=xq, top_k=top_k, include_metadata=True)
    return xc

def format_query_t5(query, context):
    context_passages = [m['metadata']['Output'] for m in context]
    context = " ".join(context_passages)
    return f"answer the question: {query} context: {context}"

def generate_answer_t5(query, context):
    output_text = context[0]['metadata']['Output']
    if len(output_text.splitlines()) > 5:
        return output_text

    if output_text.lower() == "none":
        return "The topic is not covered in the student manual."

    inputs = tokenizer.encode(query, return_tensors="pt", max_length=512, truncation=True)
    ids = generator.generate(inputs, num_beams=4, min_length=10, max_length=60, repetition_penalty=1.2)
    answer = tokenizer.decode(ids[0], skip_special_tokens=True, clean_up_tokenization_spaces=False)
    return answer
