from flask import Blueprint, render_template
from database.assistidos import ASSISTIDOS

assistidos_route = Blueprint('assistidos', __name__)


@assistidos_route.route('/')
def lista_assistidos():
    return render_template('lista_assistidos.html', assistidos=ASSISTIDOS)

@assistidos_route.route('/', methods=['POST'])
def inserir_assistido():
    pass

@assistidos_route.route('/new', methods=['GET'])
def form_assistido():
    return render_template('form_assistidos.html')

@assistidos_route.route('/<int:assistido_id>', methods=['GET'])
def detalhe_assistido(assistido_id):
    return render_template('detalhe_assistidos.html')

@assistidos_route.route('/<int:assistido_id>/edit', methods=['GET'])
def form_edit_assistido(assistido_id):
    pass

@assistidos_route.route('/<int:assistido_id>/update', methods=['PUT'])
def atualizar_assistido(assistido_id):
    pass
    
@assistidos_route.route('/<int:assistido_id>/delete', methods=['DELETE'])
def deletar_assistido(assistido_id):
    pass
        