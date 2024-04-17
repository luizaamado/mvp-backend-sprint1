from pydantic import BaseModel
from typing import Optional, List
from model.filme import Filme


class FilmeSchema(BaseModel):
    """ Define como um novo filme a ser inserido deve ser representado
    """
    titulo: str = "Kill Bill: Vol 1"
    ano: int = 2003
    genero: str = "Ação"
    sinopse: str = "Uma assassina é baleada por seu cruel empregador, Bill, e outros membros do seu círculo de assassinos - mas ela vive para planejar a sua vingança"
    assistido: str = "Sim"
    avaliacao: float = 8.5

# class FilmeNaoAssistidoSchema(BaseModel):
#     """ Define como um novo filme a ser inserido deve ser representado
#     """
#     titulo: str = "Kill Bill: Vol 1"
#     ano: int = 2003
#     genero: str = "Ação"
#     sinopse: str = "Uma assassina é baleada por seu cruel empregador, Bill, e outros membros do seu círculo de assassinos - mas ela vive para planejar a sua vingança"
#     assistido: str = "Não"
#     avaliacao: float = 8.5

class FilmeBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no titulo do filme.
    """
    titulo: str = "Kill Bill: Vol 1"


class ListagemFilmesSchema(BaseModel):
    """ Define como uma listagem de filmes será retornada.
    """
    filmes:List[FilmeSchema]


def apresenta_filmes(filmes: List[Filme]):
    """ Retorna uma representação do filme seguindo o schema definido em
        FilmeViewSchema.
    """
    result = []
    for filme in filmes:
        result.append({
            "titulo": filme.titulo,
            "ano": filme.ano,
            "genero": filme.genero,
            "sinopse": filme.sinopse,
            "assistido": filme.assistido,
            "avaliacao": filme.avaliacao
        })

    return {"filmes": result}


class FilmeViewSchema(BaseModel):
    """ Define como um filme será retornado: filme + avaliação.
    """
    id: int = 1
    titulo: str = "Kill Bill: Vol 1"
    ano: int = 2003
    genero: str = "Ação"
    sinopse: str = "Uma assassina é baleada por seu cruel empregador, Bill, e outros membros do seu círculo de assassinos - mas ela vive para planejar a sua vingança"
    assistido: str = "Sim"
    avaliacao: float = "8.5"


class FilmeDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    message: str
    titulo: str

def apresenta_filme(filme: Filme):
    """ Retorna uma representação do filme seguindo o schema definido em
        FilmeViewSchema.
    """
    return {
        "id": filme.id,
        "titulo": filme.titulo,
        "ano": filme.ano,
        "genero": filme.genero,
        "sinopse": filme.sinopse,
        "assistido": filme.assistido,
        "avaliacao": filme.avaliacao
    }
