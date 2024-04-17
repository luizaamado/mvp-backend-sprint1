from sqlalchemy import Column, String, Integer, Float, CheckConstraint

from model.base import Base

class Filme(Base):
    __tablename__ = 'filme'

    id = Column("pk_filme", Integer, primary_key=True)
    titulo = Column(String(128), unique=True)
    ano = Column(Integer)
    genero = Column(String(50), nullable=True)
    sinopse = Column(String(1024))
    assistido = Column(String(3))
    avaliacao = Column(Float, nullable=True)

    __table_args__ = (
        CheckConstraint(assistido.in_(['Sim', 'Não'])),
        CheckConstraint(genero.in_(['Ação','Animação','Aventura','Comédia','Comédia romântica','Documentário','Drama','Espionagem','Ficção científica','Musical','Policial','Romance','Suspense','Terror']))
        )

    def __init__(self, titulo:str, ano:int, genero:str, sinopse:str, assistido:str, avaliacao:float):
        """
        Cria um Filme

        Arguments:
            titulo: titulo do filme
            ano: ano em que o filme foi lançado
            gênero: gênero do filme
            sinopse: sinopse do filme
            assistido: indica se o filme foi assistido ou não
            avaliacao: a nota dada ao filme
        """
        self.titulo = titulo
        self.ano = ano
        self.genero = genero
        self.sinopse = sinopse
        self.assistido = assistido
        self.avaliacao = avaliacao
        