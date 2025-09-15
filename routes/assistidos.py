from flask import Blueprint, render_template, request
from database.assistidos import ASSISTIDOS

assistidos_route = Blueprint('assistidos', __name__)


@assistidos_route.route('/')
def lista_assistidos():
    return render_template('lista_assistidos.html', assistidos=ASSISTIDOS)

@assistidos_route.route('/', methods=['POST'])
def inserir_assistido():
    data = request.form or request.json
    novo_usuario = {
        "id": len(ASSISTIDOS) + 1,
        "nome": data['nome'],
        "data": data['data_nascimento'],
        "telefone": data['telefone'],
        "genero": data['genero'],
    }
    
    ASSISTIDOS.append(novo_usuario)

    return render_template('item_cliente.html', assistido=novo_usuario)

@assistidos_route.route('/new', methods=['GET'])
def form_assistido():
    return render_template('form_assistidos.html')

@assistidos_route.route('/<int:assistido_id>', methods=['GET'])
def detalhe_assistido(assistido_id):
    assistido = list(filter(lambda a: a['id'] == assistido_id, ASSISTIDOS))[0]

    return render_template('detalhe_assistidos.html', assistido=assistido)

@assistidos_route.route('/<int:assistido_id>/edit', methods=['GET'])
def form_edit_assistido(assistido_id):
    assistido = None
    for a in ASSISTIDOS:
        if a['id'] == assistido_id:
            assistido = a

    return render_template('form_assistidos.html', assistido=assistido)

@assistidos_route.route('/<int:assistido_id>/update', methods=['PUT'])
def atualizar_assistido(assistido_id):
    assistido_editado = None
    
    data = request.json

    
    for a in ASSISTIDOS:
        if a['id'] == assistido_id:
            a['nome'] = data['nome']
            a['data_nascimento'] = data['data_nascimento']
            a['telefone'] = data['telefone']
            a['genero'] = data['genero']

            assistido_editado = a

    return render_template('item_cliente.html', assistido=assistido_editado)

    
@assistidos_route.route('/<int:assistido_id>/delete', methods=['DELETE'])
def deletar_assistido(assistido_id):
  global ASSISTIDOS
  ASSISTIDOS = [ a for a in ASSISTIDOS if a['id'] != assistido_id ]

  return {'deleted' : 'ok'}     


        