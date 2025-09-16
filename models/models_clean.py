from peewee import *
from database.database import db

class BaseModel(Model):
    class Meta:
        database = db

class Abrigo(BaseModel):
    id_abrigo = AutoField()
    codigo_publico = IntegerField()
    nome = CharField()
    endereco = CharField()
    capacidade_total = IntegerField()
    status_operacao = CharField()
    tipo = CharField()

    class Meta:
        table_name = 'abrigo'


class Assistido(BaseModel):
    id_assistido = AutoField()
    codigo_publico = IntegerField()
    nome = CharField()
    data_nascimento = DateField(null=True)
    telefone = CharField(null=True)
    genero = CharField(null=True)
    prioridade_fuzzy = FloatField(null=True)   # valor calculado (0-100)
    status_prioridade = CharField(null=True)   # "Recusado", "Neutro" ou "Aprovado"


    class Meta:
        table_name = 'assistido'


class Operador(BaseModel):
    id_operador = AutoField()
    codigo_publico = IntegerField(unique=True)
    nome = CharField()
    funcao = CharField()

    class Meta:
        table_name = 'operador'


class Risco(BaseModel):
    id_risco = AutoField()
    descricao = CharField(null=True)
    nivel = CharField()
    peso_numero = DecimalField()

    class Meta:
        table_name = 'risco'


class Triagem(BaseModel):
    id_triagem = AutoField()
    data_triagem = DateTimeField(constraints=[SQL("DEFAULT now()")], index=True)
    id_assistido = ForeignKeyField(Assistido, column_name='id_assistido')
    id_operador = ForeignKeyField(Operador, column_name='id_operador')
    id_risco = ForeignKeyField(Risco, column_name='id_risco')
    observacoes = TextField(null=True)
    prioridade_fuzzy = DecimalField()

    class Meta:
        table_name = 'triagem'


class Encaminhamento(BaseModel):
    id_encaminhamento = AutoField()
    data_criacao = DateTimeField(constraints=[SQL("DEFAULT now()")])
    id_abrigo = ForeignKeyField(Abrigo, column_name='id_abrigo', null=True)
    id_triagem = ForeignKeyField(Triagem, column_name='id_triagem')
    status = CharField(index=True)

    class Meta:
        table_name = 'encaminhamento'


class Ocupacao(BaseModel):
    id_ocupacao = AutoField()
    data_entrada = DateTimeField(constraints=[SQL("DEFAULT now()")], index=True)
    data_saida_prevista = DateTimeField(null=True)
    data_saida_real = DateTimeField(null=True)
    id_abrigo = ForeignKeyField(Abrigo, column_name='id_abrigo')
    id_encaminhamento = ForeignKeyField(Encaminhamento, column_name='id_encaminhamento', unique=True)
    qtd_pessoas = IntegerField()

    class Meta:
        table_name = 'ocupacao'
