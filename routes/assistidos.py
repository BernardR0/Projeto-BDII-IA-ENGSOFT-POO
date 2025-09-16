from flask import Blueprint, render_template, request
from models.models_clean import Assistido
assistidos_route = Blueprint('assistidos', __name__)


@assistidos_route.route('/')
def lista_assistidos():
  assistidos=Assistido.select()
  return render_template('lista_assistidos.html', assistidos=assistidos)

@assistidos_route.route('/', methods=['POST'])
def inserir_assistido():
    data = request.form or request.json
    # 1️⃣ Busca todos os códigos existentes
    codigos_existentes = [a.codigo_publico for a in Assistido.select() if a.codigo_publico is not None]
    codigos_existentes.sort()

    # 2️⃣ Encontra o menor código livre
    proximo_codigo = 1
    for codigo in codigos_existentes:
        if codigo == proximo_codigo:
            proximo_codigo += 1
        else:
            break  # encontrou um "buraco", reutiliza

    novo_usuario = Assistido.create(
        nome = data['nome'],
        data = data['data_nascimento'],
        telefone = data['telefone'],
        genero = data['genero'],
        codigo_publico=proximo_codigo
    )
    

    return render_template('item_cliente.html', assistido=novo_usuario)

@assistidos_route.route('/new', methods=['GET'])
def form_assistido():
    return render_template('form_assistidos.html')

@assistidos_route.route('/<int:assistido_id>', methods=['GET'])
def detalhe_assistido(assistido_id):
    assistido = Assistido.get(Assistido.id_assistido == assistido_id)
    return render_template('detalhe_assistidos.html', assistido=assistido)

@assistidos_route.route('/<int:assistido_id>/edit', methods=['GET'])
def form_edit_assistido(assistido_id):
    assistido = Assistido.get(Assistido.id_assistido == assistido_id)

    return render_template('form_assistidos.html', assistido=assistido)

@assistidos_route.route('/<int:assistido_id>/update', methods=['PUT'])
def atualizar_assistido(assistido_id):
    data = request.json
    
    assistido = Assistido.get(Assistido.id_assistido == assistido_id)
    assistido.nome = data['nome']
    assistido.data = data['data_nascimento']
    assistido.telefone = data['telefone']
    assistido.genero = data['genero']

    return render_template('item_cliente.html', assistido=assistido)

    
@assistidos_route.route('/<int:assistido_id>/delete', methods=['DELETE'])
def deletar_assistido(assistido_id):
  assistido = Assistido.get(Assistido.id_assistido == assistido_id)
  assistido.delete_instance()

  return {'deleted' : 'ok'}     


        