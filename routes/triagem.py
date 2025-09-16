from logica_fuzzy import calculo_fuzzy
from flask import Blueprint, render_template, request, redirect, url_for
from models.models_clean import Assistido

triagem_route = Blueprint('triagem', __name__ , url_prefix='/triagem')

@triagem_route.route('/<int:assistido_id>', methods=['GET'])
def form_triagem(assistido_id):
    assistido = Assistido.get_or_none(Assistido.id_assistido == assistido_id)
    return render_template('form_triagem.html', assistido=assistido)

@triagem_route.route('/<int:assistido_id>', methods=['POST'])
def aplicar_triagem(assistido_id):
    assistido = Assistido.get_or_none(Assistido.id_assistido == assistido_id)

    # pega dados do json
    num_pessoas = int(request.form['num_pessoas'])
    num_vagas = int(request.form['num_vagas'])
    prioridade = float(request.form['prioridade'])

    resultado = calculo_fuzzy(num_pessoas, num_vagas, prioridade)

    # salva no banco

    assistido.prioridade_fuzzy = resultado['prioridade_fuzzy']
    assistido.status_prioridade = resultado['status']
    assistido.save()

    return redirect(url_for('assistidos.detalhe_assistido', assistido_id=assistido.id_assistido))
    

