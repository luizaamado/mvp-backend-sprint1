from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session
from model.filme import Filme
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="My Movie Tracker", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
filme_tag = Tag(name="Filme", description="Adição, visualização e remoção de filmes à base")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/filme', tags=[filme_tag],
          responses={"200": FilmeViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_filme(form: FilmeSchema):
    """Adiciona um novo filme à base de dados

    Retorna uma representação dos filmes.
    """
    filme = Filme(
        titulo=form.titulo,
        ano=form.ano,
        genero=form.genero,
        sinopse=form.sinopse,
        assistido=form.assistido,
        avaliacao=form.avaliacao)
    logger.debug(f"Adicionando filme de titulo: '{filme.titulo}'")
    try:
        # criando conexão com a base
        session = Session()
        # adicionando filme
        session.add(filme)
        # efetivando o comando de adição de novo filme na tabela
        session.commit()
        logger.debug(f"Adicionado filme de título: '{filme.titulo}'")
        return apresenta_filme(filme), 200

    except IntegrityError as e:
        # caso ocorra um erro de integridade (algum dos valores inseridos está fora do padrão esperado)
        error_msg = "Erro ao adicionar o filme. Verifique se os valores estão corretos!"
        logger.warning(f"Erro ao adicionar filme '{filme.assistido}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar o filme :/"
        logger.warning(f"Erro ao adicionar filme '{filme.titulo}', {error_msg}")
        return {"message": error_msg}, 400


@app.get('/filmes', tags=[filme_tag],
         responses={"200": ListagemFilmesSchema, "404": ErrorSchema})
def get_filmes():
    """Faz a busca por todos os filmes cadastrados

    Retorna uma representação da listagem de filmes.
    """
    logger.debug(f"Coletando filmes...")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    filmes = session.query(Filme).all()

    if not filmes:
        # se não há filmes cadastrados
        return {"filmes": []}, 200
    else:
        logger.debug(f"%d filmes encontrados" % len(filmes))
        # retorna a representação de filme
        print(filmes)
        return apresenta_filmes(filmes), 200
    
@app.get('/filmes-nao-assistidos', tags=[filme_tag],
         responses={"200": ListagemFilmesSchema, "404": ErrorSchema})
def get_filmes_nao_assistidos():
    """Faz a busca por todos os filmes cadastrados que ainda não foram assistidos

    Retorna uma representação da listagem de filmes que ainda não foram assistidos.
    """
    logger.debug(f"Coletando filmes que você ainda não assistiu...")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    filmes = session.query(Filme).filter(Filme.assistido == "Não")

    if not filmes:
        # se não há filmes cadastrados
        return {"filmes": []}, 200
    else:
        # retorna a representação de filme
        print(filmes)
        return apresenta_filmes(filmes), 200    


@app.get('/filme', tags=[filme_tag],
         responses={"200": FilmeViewSchema, "404": ErrorSchema})
def get_filme(query: FilmeBuscaSchema):
    """Faz a busca por um Filme a partir do titulo do filme

    Retorna uma representação do filme e nota associada.
    """
    filme_titulo = unquote(unquote(query.titulo))
    logger.debug(f"Coletando dados sobre filme \'{filme_titulo}\'")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    filme = session.query(Filme).filter(Filme.titulo == filme_titulo).first()

    if not filme:
        # se o filme não foi encontrado
        error_msg = "Filme não encontrado na base :/"
        logger.warning(f"Erro ao buscar filme '{filme_titulo}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        logger.debug(f"Filme encontrado: '{filme_titulo}'")
        # retorna a representação de filme
        return apresenta_filme(filme), 200


@app.delete('/filme', tags=[filme_tag],
            responses={"200": FilmeDelSchema, "404": ErrorSchema})
def del_filme(query: FilmeBuscaSchema):
    """Deleta um Filme a partir do titulo informado

    Retorna uma mensagem de confirmação da remoção.
    """
    filme_titulo = unquote(unquote(query.titulo))
    print(filme_titulo)
    logger.debug(f"Removendo dados sobre filme \'{filme_titulo}\'")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Filme).filter(Filme.titulo == filme_titulo).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Filme removido: \'{filme_titulo}\'")
        return {"message": "Filme removido", "id": filme_titulo}
    else:
        # se o filme não foi encontrado
        error_msg = "Poxa, não encontramos esse filme :/"
        logger.warning(f"Erro ao remover o filme '{filme_titulo}', {error_msg}")
        return {"message": error_msg}, 404