from flask import Blueprint

operadores_route = Blueprint('operadores', __name__)


@operadores_route.route('/')
def lista_operadores():
    pass

@operadores_route.route('/', methods=['POST'])
def inserir_operador():
    pass

@operadores_route.route('/new', methods=['GET'])
def form_operador():
    pass

@operadores_route.route('/<int:operador_id>', methods=['GET'])
def detalhe_operador(operador_id):
    pass

@operadores_route.route('/<int:operador_id>/edit', methods=['GET'])
def form_edit_operador(operador_id):
    pass

@operadores_route.route('/<int:operador_id>/update', methods=['PUT'])
def atualizar_operador(operador_id):
    pass
    
@operadores_route.route('/<int:operador_id>/delete', methods=['DELETE'])
def deletar_operador(operador_id):
    pass
        