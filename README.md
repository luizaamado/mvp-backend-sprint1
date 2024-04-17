# Minha API

Este projeto tem como objetivo ser um 'ratreador' de filmes, uma espécie de diário de cinema,
onde o usuário pode cadastrar filmes que já assistiu ou que ainda não assistiu, dar sua avaliação 
pessoal para cada obra e encontrar facilmente os filmes que ainda assistiu para não perder mais tempo 
procurando nos streamings algo para assistir.

---
## Como executar 


Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
$ python3 -m venv env install
```
Este comando cria o ambiente virtual.

```
$ source env/bin/activate
```
Este comando habilita o ambiente virtual para ser utilizado.

```
(env)$ pip3 install -r requirements.txt
```
Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.
