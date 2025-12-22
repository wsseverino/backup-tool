FROM python:3.12-slim

# Instala dependências
RUN pip install pytest

# Cria diretório de trabalho
WORKDIR /app

# Copia o código
COPY src/ /app/src/
COPY tests/ /app/tests/
COPY requirements.txt /app/

# Instala dependências do projeto
RUN pip install -r requirements.txt

# Define entrypoint com argumentos
ENTRYPOINT ["python", "src/main.py"]