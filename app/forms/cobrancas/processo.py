from datetime import datetime

from flask_wtf import FlaskForm
from pytz import timezone
from wtforms import (
    BooleanField,
    DateField,
    IntegerField,
    SelectField,
    SelectMultipleField,
    StringField,
    TextAreaField,
)
from wtforms.validators import Length


class ProcessoADMForm(FlaskForm):

    numero_processo = StringField("Número de Controle")
    data_cadastro = DateField(
        "Data de Cadastro", default=datetime.now(timezone("America/Manaus"))
    )
    cliente = SelectField("Cliente")
    pessoa = SelectField("Pessoa")
    descricao = TextAreaField("Descrição")
    valor_debito = StringField("Valor do Débito")
    cobranca_id = StringField("UC da Cobrança")


class ModelPrazoForm(FlaskForm):

    prazo_nome = StringField("Nome do Prazo")
    sigla = StringField("Sigla", validators=[Length(max=5)], render_kw={"maxlength": 5})
    descricao = TextAreaField("Descrição")
    contagem_data = IntegerField("Contagem de Dias do prazo", default=5)


class PrazosForm(FlaskForm):

    prazo_nome = StringField("Nome do Prazo")
    sigla = StringField("Sigla", validators=[Length(max=5)], render_kw={"maxlength": 5})
    descricao = TextAreaField("Descrição")

    ask_prazofilho = BooleanField("Prazo Filho?", default=False)
    prazo_filho = SelectMultipleField("Selecione os prazos filhos", choices=[])
