from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey
)

from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class Esercizio(Base):

    __tablename__ = "esercizi"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    titolo = Column(
        String(200),
        nullable=False
    )

    testo = Column(
        Text,
        nullable=False
    )

    soluzione_json = Column(
        Text,
        nullable=False
    )

    prove_studenti = relationship(
        "ProvaStudente",
        back_populates="esercizio"
    )


class ProvaStudente(Base):

    __tablename__ = "prove_studenti"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    id_esercizio = Column(
        Integer,
        ForeignKey("esercizi.id")
    )

    contenuto_json = Column(
        Text,
        nullable=False
    )

    nome_file = Column(
        String(200),
        nullable=False
    )

    valutazione_ai = Column(
        Text
    )

    esercizio = relationship(
        "Esercizio",
        back_populates="prove_studenti"
    )

    