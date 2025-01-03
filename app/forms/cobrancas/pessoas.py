from flask_wtf import FlaskForm
from wtforms import DateField, IntegerField, SelectField, StringField, TextAreaField


class PessoaForm(FlaskForm):

    nome = StringField("Nome")
    cpf = StringField("CPF")
    rg = StringField("RG")
    email = StringField("Email")
    telefone = StringField("Telefone")


class EnderecoForm(FlaskForm):

    cep = StringField("CEP")
    logradouro = StringField("Logradouro")
    numero = IntegerField("Número")
    complemento = StringField("Complemento")
    bairro = StringField("Bairro")
    cidade = StringField("Cidade")

    estado = SelectField(
        "Estado",
        choices=[
            ("Acre", "Acre"),
            ("Alagoas", "Alagoas"),
            ("Amapá", "Amapá"),
            ("Amazonas", "Amazonas"),
            ("Bahia", "Bahia"),
            ("Ceará", "Ceará"),
            ("Distrito Federal", "Distrito Federal"),
            ("Espírito Santo", "Espírito Santo"),
            ("Goiás", "Goiás"),
            ("Maranhão", "Maranhão"),
            ("Mato Grosso", "Mato Grosso"),
            ("Mato Grosso do Sul", "Mato Grosso do Sul"),
            ("Minas Gerais", "Minas Gerais"),
            ("Pará", "Pará"),
            ("Paraíba", "Paraíba"),
            ("Paraná", "Paraná"),
            ("Pernambuco", "Pernambuco"),
            ("Piauí", "Piauí"),
            ("Rio de Janeiro", "Rio de Janeiro"),
            ("Rio Grande do Norte", "Rio Grande do Norte"),
            ("Rio Grande do Sul", "Rio Grande do Sul"),
            ("Rondônia", "Rondônia"),
            ("Roraima", "Roraima"),
            ("Santa Catarina", "Santa Catarina"),
            ("São Paulo", "São Paulo"),
            ("Sergipe", "Sergipe"),
            ("Tocantins", "Tocantins"),
        ],
    )


class DebitosForm(FlaskForm):

    tipo = StringField("Tipo")
    valor = StringField("Valor")
    status = StringField("Status")
    vencimento = DateField("Vencimento")

    descricao = TextAreaField("Descrição")
    observacao = TextAreaField("Observação")
