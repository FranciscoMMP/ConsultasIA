# Usando uma imagem Python leve
FROM python:3.9

# Criando diretório de trabalho
WORKDIR /app

# Copiando arquivos
COPY . .

# Instalando dependências
RUN pip install -r requirements.txt

# Expondo porta
EXPOSE 8000

# Comando para rodar o servidor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
