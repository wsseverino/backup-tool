# Backup Tool

## Ferramenta de Backup Automatizado em Python com Docker

---

## Descrição

Esta ferramenta é uma aplicação **Python** desenvolvida para realizar **backups automáticos** de arquivos a partir de um diretório de origem para um diretório de destino.

O projeto foi estruturado para simular **cenários reais de DevOps**, com foco em boas práticas de organização de código, versionamento, testes automatizados e execução em containers Docker.

### Principais funcionalidades

* Modularização do código para reutilização:
  * `backup.py`
  * `logger.py`
  * `main.py`
* Geração de logs no arquivo `backup.log` para rastreamento:
  * Níveis `INFO` e `ERROR`
* Versionamento automático dos backups:
  * Cada execução gera uma pasta com timestamp (ex.: `20251222_173045`)
* Testes unitários com **pytest**, cobrindo cenários de sucesso e falha
* Execução em **container Docker**, garantindo portabilidade
* Tratamento de erros (ex.: diretórios inexistentes)
* Passagem de argumentos via linha de comando

---

## Requisitos

### Desenvolvimento local

* Python **3.8+**
* Pip

### Execução em container

* Docker instalado

### Dependências

* `pytest` (listado em `requirements.txt`)

---

## Instalação Local

1. Clone ou baixe este repositório
2. Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## Uso Local

Execute o backup informando os diretórios de origem e destino:

```bash
python src/main.py caminho/origem caminho/destino
```

---

## Testes Unitários

Execute os testes localmente com:

```bash
pytest tests/
```

---

## Construção e Execução em Docker

### Construir a Imagem Docker

Na raiz do projeto (`backup-tool`), execute:

```bash
docker build -t backup-tool .
```

### Executar o Container para Backup

Execute o container montando os volumes:

**Linux/macOS:**
```bash
docker run --rm \
  -v "/caminho/origem":/origem \
  -v "/caminho/destino":/destino \
  -v "/caminho/backup.log":/app/backup.log \
  backup-tool /origem /destino
```

**Windows:**
```bash
docker run --rm \
  -v "C:/backup-tool/Origem":/origem \
  -v "C:/backup-tool/Destino":/destino \
  -v "C:/backup-tool/backup.log":/app/backup.log \
  backup-tool /origem /destino
```

### Executar Testes no Container

Para rodar os testes unitários dentro do container:

```bash
docker run --rm backup-tool pytest tests/ -v
```

---

## Estrutura do Projeto

```
backup-tool/
├── Origem/             #Arquivos que terão backup
│   ├── [Python para Automação em Devopsl]-[Atividade Final].pdf
│   ├── teste.txt
│   ├── webconfig.txt
├── src/
│   ├── __init__.py
│   ├── main.py          # Ponto de entrada
│   ├── backup.py        # Lógica de backup
│   └── logger.py        # Sistema de logging
├── tests/
│   ├── __init__.py
│   ├── test_backup.py   # Testes de backup
│   └── test_logger.py   # Testes de logging
├── Dockerfile           # Container Docker
├── requirements.txt     # Dependências Python
└── README.md           # Documentação
```

---

## Conclusão

Este projeto demonstra uma solução completa de backup automatizado utilizando **Python, Docker e testes automatizados**, alinhada a práticas modernas de **DevOps e Engenharia de Software**.
