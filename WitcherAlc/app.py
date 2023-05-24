from flask import Flask, render_template, request
from utils import empacotar_ingredientes
from data import ingredientes

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/knapsack', methods=['GET', 'POST'])
def knapsack():
    if request.method == 'POST':
        # Obter os dados do formulário
        num_frascos = int(request.form.get('num_frascos'))
        capacidades = []

        for i in range(1, num_frascos + 1):
            capacidade = int(request.form.get(f'frasco_capacidade_{i}'))
            capacidades.append(capacidade)

        # Chamar a função empacotar_ingredientes()
        frascos = empacotar_ingredientes(ingredientes, capacidades)

        # Passar os frascos para o template
        return render_template('resultado.html', frascos=frascos, frascos_range=range(1, num_frascos + 1))
    return render_template('knapsack.html')

if __name__ == '__main__':
    app.run(debug=True)