from datetime import datetime

import pytz

from app import db

partes_enderecos = db.Table(
    "partes_enderecos",
    db.Column("parte_id", db.Integer, db.ForeignKey("partes.id")),
    db.Column("endereco_id", db.Integer, db.ForeignKey("parte_addresses.id")),
)


class ParteAddresses(db.Model):

    id = db.Column(db.Integer, primary_key=True, unique=True)
    parte_id = db.Column(db.Integer, db.ForeignKey("partes.id"))
    endereco = db.Column(db.String(length=64))
    bairro = db.Column(db.String(length=64))
    cidade = db.Column(db.String(length=64))
    estado = db.Column(db.String(length=64))
    cep = db.Column(db.String(length=64))
    email = db.Column(db.String(length=64))
    telefone1 = db.Column(db.String(length=64))
    telefone2 = db.Column(db.String(length=64))
    telefone3 = db.Column(db.String(length=64))


class Processos(db.Model):

    id = db.Column(db.Integer, primary_key=True, unique=True)
    numproc = db.Column(db.String(length=64), nullable=False, unique=True)
    parte_contraria = db.Column(db.String(length=64), nullable=False)
    adv_contrario = db.Column(db.String(length=64), nullable=False)
    cliente = db.Column(db.String(length=64), nullable=False)
    assunto = db.Column(db.String(length=64), nullable=False)
    classe = db.Column(db.String(length=64), nullable=False)
    foro = db.Column(db.String(length=64), nullable=False)
    vara = db.Column(db.String(length=64), nullable=False)
    juiz = db.Column(db.String(length=64), nullable=False)
    area = db.Column(db.String(length=64), nullable=False, default="Vazio")
    valor_causa = db.Column(db.Float, nullable=False, default=0.01)
    data_distribuicao = db.Column(
        db.DateTime, default=datetime.now(pytz.timezone("Etc/GMT+4"))
    )
    data_cadastro = db.Column(
        db.DateTime, default=datetime.now(pytz.timezone("Etc/GMT+4"))
    )


class Partes(db.Model):

    id = db.Column(db.Integer, primary_key=True, unique=True)
    nome = db.Column(db.String(length=64), nullable=False)
    cpf_cnpj = db.Column(db.String(length=64))
    email = db.Column(db.String(length=64))


class Clientes(db.Model):

    id = db.Column(db.Integer, primary_key=True, unique=True)
    cliente = db.Column(db.String(length=64), nullable=False)
    cpf_cnpj = db.Column(db.String(length=64), nullable=False)
    endereco = db.Column(db.String(length=64))
    cidade = db.Column(db.String(length=64))
    estado = db.Column(db.String(length=64))
    cep = db.Column(db.String(length=64))
    email = db.Column(db.String(length=64))
    telefone1 = db.Column(db.String(length=64))
    telefone2 = db.Column(db.String(length=64))
    telefone3 = db.Column(db.String(length=64))
