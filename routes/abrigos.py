from flask import Blueprint, render_template, request, redirect, url_for
from models.models_clean import Abrigo

abrigos_route = Blueprint('abrigos', __name__, url_prefix='/abrigos')


@abrigos_route.route('/')
def lista_abrigos():
    abrigos = Abrigo.select()
    return render_template('lista_abrigos.html', abrigos=abrigos)


@abrigos_route.route('/new', methods=['GET'])
def form_abrigo():
    return render_template('form_abrigo.html')


@abrigos_route.route('/<int:abrigo_id>')
def detalhe_abrigo(abrigo_id):
    abrigo = Abrigo.get_or_none(Abrigo.id_abrigo == abrigo_id)
    return render_template('detalhe_abrigos.html', abrigo=abrigo)

@abrigos_route.route('/<int:abrigo_id>/edit', methods=['GET'])
def form_edit_abrigo(abrigo_id):
    abrigo = Abrigo.get_or_none(Abrigo.id_abrigo == abrigo_id)

    return render_template('form_abrigo.html', abrigo=abrigo)

@abrigos_route.route('/', methods=['POST'])
def inserir_abrigo():
    data = request.json

    # 1️⃣ Busca todos os códigos existentes
    codigos_existentes = [a.codigo_publico for a in Abrigo.select() if a.codigo_publico is not None]
    codigos_existentes.sort()

    # 2️⃣ Encontra o menor código livre
    proximo_codigo = 1
    for codigo in codigos_existentes:
        if codigo == proximo_codigo:
            proximo_codigo += 1
        else:
            break  # encontrou um "buraco", reutiliza


    novo_abrigo = Abrigo.create(
        nome=data['nome'],
        endereco=data['endereco'],
        capacidade_total=data['capacidade_total'],
        status_operacao=data['status_operacao'],
        tipo=data['tipo'],
        codigo_publico=proximo_codigo
    )

    return render_template('item_abrigo.html', abrigo=novo_abrigo)
    


@abrigos_route.route('/<int:abrigo_id>/editar', methods=['PUT'])
def editar_abrigo(abrigo_id):
    data = request.json
    abrigo = Abrigo.get_by_id(abrigo_id)
    abrigo.nome = data['nome']
    abrigo.endereco = data['endereco']
    abrigo.capacidade_total = data['capacidade_total']
    abrigo.status_operacao = data['status_operacao']
    abrigo.tipo = data['tipo']
    abrigo.save()

    return render_template('item_abrigo.html', abrigo=abrigo)

    


@abrigos_route.route('/<int:abrigo_id>/deletar', methods=['DELETE'])
def deletar_abrigo(abrigo_id):
    abrigo = Abrigo.get_by_id(abrigo_id)
    abrigo.delete_instance()
    
