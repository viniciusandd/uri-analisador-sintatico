# Analisador Sintático Top-Down Preditivo Tabular

O projeto consiste é uma implementação de um analisador sintático.

## Como executar

Abaixo, as 3 maneiras de como executar a aplicação.

## :cloud: Nuvem

O projeto está disponível em: http://viniciusandd.pythonanywhere.com

## :whale: Container

Builde uma nova imagem.

`docker build -t analisador_sintatico .`

Execute o container (a porta utilizada é a `8000`).

`docker run -dti -p 8000:5000 analisador_sintatico`

## :computer: Máquina local

Primeiro, clone o projeto.

`git clone https://github.com/viniciusandd/uri-analisador-sintatico.git`

Entre na pasta e crie um ambiente virtual.

```
cd uri-analisador-sintatico
python3 -m venv venv
```

Ative-o e instale as dependências do projeto.

```
source venv/bin/active
pip install -r requirements.txt
```

Crie um arquivo chamado `.env` para armazenar as variáveis de ambiente. Cole o conteúdo abaixo e salve-o.

```
FLASK_APP=analisador_sintatico/app.py
FLASK_ENV=development
FLASK_DEBUG=1
```

Inicie a aplicação (a porta padrão é a `5000`).

`flask run`