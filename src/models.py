import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nombre_usuario = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

    favoritos = relationship("Favorito")

class Pokemon(Base):
    __tablename__ = 'pokemon'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    tipo = Column(String(250))
    habilidades = relationship("Habilidad", secondary="pokemon_habilidad")
    estadisticas = relationship("Estadistica")

class Favorito(Base):
    __tablename__ = 'favorito'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    pokemon_id = Column(Integer, ForeignKey('pokemon.id'))
    usuario = relationship(Usuario)
    pokemon = relationship(Pokemon)

class Habilidad(Base):
    __tablename__ = 'habilidad'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    descripcion = Column(String(250))

class PokemonHabilidad(Base):
    __tablename__ = 'pokemon_habilidad'
    id = Column(Integer, primary_key=True)
    pokemon_id = Column(Integer, ForeignKey('pokemon.id'))
    habilidad_id = Column(Integer, ForeignKey('habilidad.id'))

class Estadistica(Base):
    __tablename__ = 'estadistica'
    id = Column(Integer, primary_key=True)
    pokemon_id = Column(Integer, ForeignKey('pokemon.id'))
    tipo_estadistica = Column(String(250), nullable=False)
    valor = Column(Integer)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
