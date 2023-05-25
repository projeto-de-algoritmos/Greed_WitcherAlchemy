from flask import Flask, render_template, request
from utils import knapsack_, interval_scheduling
from data import ingredientes
from models import Contrato

from datetime import datetime

app = Flask(__name__)

# Rota Default
@app.route('/')
def index():
    return render_template('index.html')

# Rota do Knapsack (formulário de frascos), retorna o resultado
@app.route('/knapsack', methods=['GET', 'POST'])
def knapsack():
    if request.method == 'POST':
        # Obter os dados do formulário
        num_frascos = int(request.form.get('num_frascos'))
        capacidades = []

        for i in range(1, num_frascos + 1):
            capacidade = int(request.form.get(f'frasco_capacidade_{i}'))
            capacidades.append(capacidade)

        # Chamar a função de knapsack
        frascos = knapsack_(ingredientes, capacidades)

        # Passar os frascos para o template
        return render_template('resultado_knapsack.html', frascos=frascos, frascos_range=range(1, num_frascos + 1))
    return render_template('knapsack.html', ingredientes=ingredientes)

contratos_ = []

# Rota do Interval Scheduling (formulário de contratos), retorna o resultado
@app.route('/contratos', methods=['GET', 'POST'])
def contratos():
    if request.method == 'POST':
        # Obter os dados do formulário
        num_contratos = int(request.form.get('num_contratos'))
        
        for i in range(1, num_contratos + 1):
            nome = request.form.get(f'nome_{i}')
            descricao = request.form.get(f'descricao_{i}')
            inicio = datetime.strptime(request.form.get(f'inicio_{i}'), '%Y-%m-%dT%H:%M')
            termino = datetime.strptime(request.form.get(f'termino_{i}'), '%Y-%m-%dT%H:%M')

            print(inicio, str(type(inicio)))

            contratos = Contrato(nome, descricao, inicio, termino)
            contratos_.append(contratos)

        # Chamar a função de Interval Scheduling
        contratos_selecionados = interval_scheduling(contratos_)

        # Passar os contratos para o template
        return render_template('resultado_scheduling.html', contratos_selecionados=contratos_selecionados)
    return render_template('contratos.html')

if __name__ == '__main__':
    app.run(debug=True)