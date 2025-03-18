from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()

# Carregar modelo de IA (Exemplo: GPT-2)
modelo = pipeline("text-generation", model="gpt2")

@app.get("/")
def home():
    return {"mensagem": "API de IA rodando no Vercel"}

@app.get("/pergunta/")
def responder(pergunta: str):
    resposta = modelo(pergunta, max_length=50, do_sample=True)[0]["generated_text"]
    return {"pergunta": pergunta, "resposta": resposta}
