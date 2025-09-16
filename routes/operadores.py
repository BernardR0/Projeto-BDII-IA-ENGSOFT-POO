from flask import Blueprint, render_template, request, redirect, url_for
from models.models_clean import Operador

operadores_route = Blueprint('operadores', __name__, url_prefix='/operadores')


@operadores_route.route('/')
def lista_operadores():
    operadores = Operador.select()
    return render_template('lista_operador.html', operadores=operadores)

@operadores_route.route('/new', methods=['GET'])
def form_operador():
    return render_template('form_operador.html')


@operadores_route.route('/', methods=['POST'])
def inserir_operador():
    data = request.json
    # 1️⃣ Busca todos os códigos existentes
    codigos_existentes = [o.codigo_publico for o in Operador.select() if o.codigo_publico is not None]
    codigos_existentes.sort()

    # 2️⃣ Encontra o menor código livre
    proximo_codigo = 1
    for codigo in codigos_existentes:
        if codigo == proximo_codigo:
            proximo_codigo += 1
        else:
            break  # encontrou um "buraco", reutiliza

    novo_operador = Operador.create(
        nome=data['nome'],
        funcao=data['funcao'],
        codigo_publico=proximo_codigo
    )
    return render_template('item_operador.html', operador=novo_operador)


@operadores_route.route('/<int:operador_id>')
def detalhe_operador(operador_id):
    operador = Operador.get_or_none(Operador.id_operador == operador_id)
    return render_template('detalhe_operador.html', operador=operador)




@operadores_route.route('/<int:operador_id>/edit', methods=['GET'])
def form_edit_operador(operador_id):
    operador = Operador.get_or_none(Operador.id_operador == operador_id)

    return render_template('form_operador.html', operador=operador)


@operadores_route.route('/<int:operador_id>/editar', methods=['PUT'])
def editar_operador(operador_id):
    data = request.json
    operador = Operador.get_by_id(operador_id)
    operador.nome = data['nome']
    operador.funcao = data['funcao']
    operador.save()
    return render_template('item_operador.html', operador=operador)



@operadores_route.route('/<int:operador_id>/deletar', methods=['DELETE'])
def deletar_operador(operador_id):
    operador = Operador.get_by_id(operador_id)
    operador.delete_instance()
    
