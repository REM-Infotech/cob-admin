from datetime import datetime

import pytz
from flask_wtf import FlaskForm
from wtforms import (
    BooleanField,
    DateField,
    EmailField,
    SelectField,
    StringField,
    SubmitField,
    TextAreaField,
)
from wtforms.validators import DataRequired

# from app.forms.proc_adm.defaults import bairros_manaus, cidades_amazonas

# import string
# import random


class SearchProc(FlaskForm):

    campo_busca = StringField("Buscar...")
    tipoBusca = SelectField("Buscar por: ", choices=[])

    def __init__(self, *args, **kwargs):

        super(SearchProc, self).__init__(*args, **kwargs)
        self.tipoBusca.choices = [
            ("numproc", "Número do Processo"),
            ("parte_contraria", "Parte Contrária"),
            ("cliente", "Cliente"),
            ("uc", "Unidade Consumidora"),
            ("bairro", "Bairro"),
            ("cidade", "Cidade"),
            ("estado", "Estado"),
        ]

    submit = SubmitField("Buscar")


class ProcessoForm(FlaskForm):

    numproc = StringField("Número do Processo *")
    automake = BooleanField("Criar Dinamicamente número do processo")
    cliente = SelectField(
        "Cliente",
        choices=[("Selecione", "Selecione")],
    )
    parte_contraria = SelectField(
        "Parte Contrária", choices=[("Selecione", "Selecione")]
    )
    description = TextAreaField("Descrição")
    valor_debito = StringField("Valor Total Débito")
    data_cadastro = DateField(
        "Data Cadastro", default=datetime.now(pytz.timezone("America/Manaus")).date()
    )
    submit = SubmitField("Salvar")

    def __init__(
        self,
        partes_contra: list[tuple[str, str]] = None,
        clientes: list[tuple[str, str]] = None,
        *args,
        **kwargs
    ):
        super(ProcessoForm, self).__init__(*args, **kwargs)

        if partes_contra:
            self.parte_contraria.choices.extend(partes_contra)

        if clientes:
            self.cliente.choices.extend(clientes)


class PessoaForm(FlaskForm):

    nome = StringField("Nome *", validators=[DataRequired()])
    cpf_cnpj = StringField("CPF/CNPJ *", validators=[DataRequired()])
    endereco = StringField("Endereço")
    bairro = StringField("Bairro")
    cidade = StringField("Cidade")
    estado = StringField("Estado")
    cep = StringField("CEP")
    email = EmailField("E-mail")
    telefone1 = StringField("Telefone 1")
    telefone2 = StringField("Telefone 2")
    telefone3 = StringField("Telefone 3")
    submit = SubmitField("Salvar")

    def __init__(self, *args, **kwargs):
        super(PessoaForm, self).__init__(*args, **kwargs)


class clienteForm(FlaskForm):

    cliente = StringField("Nome cliente *", validators=[DataRequired()])
    cpf_cnpj = StringField("CPF/CNPJ *", validators=[DataRequired()])
    endereco = StringField("Endereço")
    cidade = StringField("Cidade")
    estado = StringField("Estado")
    cep = StringField("CEP")
    email = StringField("E-mail")
    telefone1 = StringField("Telefone 1")
    telefone2 = StringField("Telefone 2")
    telefone3 = StringField("Telefone 3")
    submit = SubmitField("Salvar")

    def __init__(self, *args, **kwargs):
        super(clienteForm, self).__init__(*args, **kwargs)
