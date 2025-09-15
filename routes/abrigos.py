from flask import Blueprint

abrigos_route = Blueprint('abrigos', __name__)


@abrigos_route.route('/')
def lista_abrigo():
    pass

@abrigos_route.route('/', methods=['POST'])
def inserir_abrigo():
    pass

@abrigos_route.route('/new', methods=['GET'])
def form_abrigo():
    pass

@abrigos_route.route('/<int:abrigo_id>', methods=['GET'])
def detalhe_abrigo(abrigo_id):
    pass

@abrigos_route.route('/<int:abrigo_id>/edit', methods=['GET'])
def form_edit_abrigo(abrigo_id):
    pass

@abrigos_route.route('/<int:abrigo_id>/update', methods=['PUT'])
def atualizar_abrigo(abrigo_id):
    pass
    
@abrigos_route.route('/<int:abrigo_id>/delete', methods=['DELETE'])
def deletar_abrigo(abrigo_id):
    pass
        