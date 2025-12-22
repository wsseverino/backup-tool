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

### Passo a Passo com Scripts e Demonstração

Esta seção documenta o processo completo para **construção e execução do container Docker**, incluindo os comandos utilizados e a descrição dos resultados esperados.

> **Observação:** Como este é um `README.md` textual, os prints são descritos. Em uma entrega real, insira imagens utilizando Markdown, por exemplo:
> `![Descrição](caminho/imagem.png)`

---

### Passo 1: Construir a Imagem Docker

Na raiz do projeto (`backup-tool`), execute:

```bash
docker build -t backup-tool .
```

**Saída esperada:**

* Download das camadas base (ex.: `python:3.12-slim`)
* Instalação das dependências via `pip`
* Mensagem final:

  * `Successfully tagged backup-tool:latest`

**Print exemplo:**

* Captura de tela do terminal mostrando o build completo sem erros

---

### Passo 2: Verificar a Imagem Construída

Execute:

```bash
docker images
```

**Saída esperada:**

* Lista de imagens contendo:

  * `backup-tool`
  * Tag: `latest`
  * Tamanho aproximado: ~150 MB

**Print exemplo:**

* Captura de tela da lista de imagens destacando `backup-tool`

---

### Passo 3: Preparar Pastas de Teste

No host, crie as pastas de origem e destino.

**Exemplo (Windows):**

```text
C:\backup-tool\Origem
C:\backup-tool\Destino
```

* Adicione arquivos de teste em `Origem`

  * Exemplo: `teste.txt` com o conteúdo `Olá, mundo!`

**Print exemplo:**

* Captura do Explorador de Arquivos mostrando:

  * Pasta `Origem` com arquivos
  * Pasta `Destino` vazia antes da execução

---

### Passo 4: Executar o Container para Backup

Execute o container montando os volumes:

```bash
docker run --rm \
  -v "C:/backup-tool/Origem":/origem \
  -v "C:/backup-tool/Destino":/destino \
  -v "C:/backup-tool/backup.log":/app/backup.log \
  backup-tool /origem /destino
```

> Ajuste os caminhos conforme o sistema operacional utilizado.

**Saída esperada:**

* Mensagem indicando início do backup (ex.: `Iniciando backup...`)
* Execução rápida e sem erros visíveis no terminal

**Print exemplo:**

* Captura de tela do terminal mostrando o comando executado e a saída sem erros

---

### Resultados Obtidos Após a Execução

#### Pasta de destino

* Criação automática de uma subpasta com timestamp:

  * Exemplo: `20251222_173045`
* Arquivos da origem copiados para dentro dessa pasta

**Print exemplo:**

* Explorador de Arquivos mostrando a pasta versionada com os arquivos copiados

#### Arquivo de log

* Criação/atualização do arquivo `backup.log`
* Entradas como:

  * `INFO - Arquivo copiado com sucesso`
  * `INFO - Backup concluído com sucesso`

**Print exemplo:**

* Bloco de Notas exibindo o conteúdo do `backup.log`

---

### Passo 5: Executar Testes no Container

Para rodar os testes unitários dentro do container:

```bash
docker run --rm backup-tool pytest tests/ -v
```

**Saída esperada:**

```text
collected 3 items
... [100%]
3 passed
```

**Print exemplo:**

* Captura de tela do terminal mostrando os testes sendo executados e aprovados

---

### Passo 6: Limpeza (Opcional)

Para remover a imagem Docker:

```bash
docker rmi backup-tool
```

---

## Notas Adicionais

* O container utiliza **volumes Docker** para persistir dados no host
* Em caso de erro:

  * Consulte o arquivo `backup.log`
* Para Linux ou macOS, ajuste os caminhos dos volumes:

```bash
/home/usuario/backup-tool/Origem
/home/usuario/backup-tool/Destino
```

---

## Conclusão

Este projeto demonstra uma solução completa de backup automatizado utilizando **Python, Docker e testes automatizados**, alinhada a práticas modernas de **DevOps e Engenharia de Software**.
