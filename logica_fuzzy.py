import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from skfuzzy import control as ctrl

def pedir_inteiro(n, minimo, maximo):
    while True:
        try:
            valor = int(input(n))
            if minimo <= valor <= maximo:
                return valor
            else:
                print(f"Digite um valor entre {minimo} e {maximo}.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

def pedir_float(n, minimo, maximo):
    while True:
        try:
            valor = float(input(n))
            if minimo <= valor <= maximo:
                return valor
            else:
                print(f"Digite um valor entre {minimo} e {maximo}.")
        except ValueError:
            print("Entrada inválida. Digite um número (ex: 0.5).")

# ------------------ Variáveis de entrada ------------------
qtde_pessoas = ctrl.Antecedent(np.arange(0, 501, 1), 'pessoas')
qtde_vagas   = ctrl.Antecedent(np.arange(0, 301, 1), 'vagas')
prioridade   = ctrl.Antecedent(np.arange(0, 1.01, 0.01), 'prioridade')

# ------------------ Variável de saída ---------------------
encaminhamento = ctrl.Consequent(np.arange(0, 101, 1), 'encaminhamento')

# ------------------ Funções de pertinência ----------------
qtde_pessoas['baixo'] = fuzz.trapmf(qtde_pessoas.universe, [0, 0, 50, 100])
qtde_pessoas['medio'] = fuzz.trimf(qtde_pessoas.universe, [50, 125, 200])
qtde_pessoas['alto']  = fuzz.trapmf(qtde_pessoas.universe, [200, 300, 500, 500])

qtde_vagas['baixo'] = fuzz.trapmf(qtde_vagas.universe, [0, 0, 30, 70])
qtde_vagas['medio'] = fuzz.trimf(qtde_vagas.universe, [30, 90, 150])
qtde_vagas['alto']  = fuzz.trapmf(qtde_vagas.universe, [150, 200, 300, 300])

prioridade['baixo'] = fuzz.trapmf(prioridade.universe, [0, 0, 0.3, 0.5])
prioridade['medio'] = fuzz.trimf(prioridade.universe, [0.3, 0.5, 0.7])
prioridade['alto']  = fuzz.trapmf(prioridade.universe, [0.5, 0.7, 1.0, 1.0])

encaminhamento['Recusado'] = fuzz.trapmf(encaminhamento.universe, [0, 0, 30, 50])
encaminhamento['Neutro']   = fuzz.trimf(encaminhamento.universe, [30, 50, 70])
encaminhamento['Aprovado'] = fuzz.trapmf(encaminhamento.universe, [50, 70, 100, 100])

# ------------------ Regras ------------------
regra1  = ctrl.Rule(qtde_pessoas['alto']  & qtde_vagas['baixo'] & prioridade['alto'],  encaminhamento['Aprovado'])
regra2  = ctrl.Rule(qtde_pessoas['alto']  & qtde_vagas['baixo'] & prioridade['medio'], encaminhamento['Recusado'])
regra3  = ctrl.Rule(qtde_pessoas['alto']  & qtde_vagas['baixo'] & prioridade['baixo'], encaminhamento['Recusado'])
regra4  = ctrl.Rule(qtde_pessoas['medio'] & qtde_vagas['baixo'] & prioridade['alto'],  encaminhamento['Aprovado'])
regra5  = ctrl.Rule(qtde_pessoas['medio'] & qtde_vagas['baixo'] & prioridade['medio'], encaminhamento['Neutro'])
regra6  = ctrl.Rule(qtde_pessoas['medio'] & qtde_vagas['baixo'] & prioridade['baixo'], encaminhamento['Recusado'])
regra7  = ctrl.Rule(qtde_pessoas['baixo'] & qtde_vagas['baixo'] & prioridade['alto'],  encaminhamento['Aprovado'])
regra8  = ctrl.Rule(qtde_pessoas['baixo'] & qtde_vagas['baixo'] & prioridade['medio'], encaminhamento['Neutro'])
regra9  = ctrl.Rule(qtde_pessoas['baixo'] & qtde_vagas['baixo'] & prioridade['baixo'], encaminhamento['Recusado'])
regra10 = ctrl.Rule(qtde_vagas['medio'] & prioridade['alto'],  encaminhamento['Aprovado'])
regra11 = ctrl.Rule(qtde_vagas['medio'] & prioridade['medio'], encaminhamento['Aprovado'])
regra12 = ctrl.Rule(qtde_vagas['medio'] & prioridade['baixo'], encaminhamento['Neutro'])
regra13 = ctrl.Rule(qtde_vagas['alto'], encaminhamento['Aprovado'])

# ------------------ Sistema ------------------
sistema_ctrl = ctrl.ControlSystem([
    regra1, regra2, regra3, regra4, regra5, regra6, regra7,
    regra8, regra9, regra10, regra11, regra12, regra13
])
sistema = ctrl.ControlSystemSimulation(sistema_ctrl)


def calculo_fuzzy(num_pessoas, num_vagas, num_prioridade):
    

    sistema.input['pessoas']    = num_pessoas
    sistema.input['vagas']      = num_vagas
    sistema.input['prioridade'] = num_prioridade

    sistema.compute()

    if 'encaminhamento' in sistema.output:
        resultado = sistema.output['encaminhamento']

        if resultado < 40:
            status = "Recusado"
        elif resultado < 60:
            status = "Neutro"
        else:
            status = "Aprovado"
    
        return {
            "prioridade_fuzzy": float(resultado),
            "status": status
        }
        
    else:
        print("\n Nenhuma regra foi ativada para os valores informados!\n")
