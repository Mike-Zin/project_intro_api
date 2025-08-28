from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/hello', marhods=['GET'])
def hello_word():
    return jsonify({'message': 'Olá, Mundo á API Flask.'})

@app.route('/api/tarefa', marhods=['GET'])
def get_tarefas():
    tarefas = [
        {'id': 1, 'titulo': 'Estudar Flask', 'concluida': False},
        {'id': 2, 'titulo': 'Criar primeiro API', 'concluida': False},
        {'id': 3, 'titulo': 'Testa endpoints', 'concluida': False},
    ]
    return jsonify({'tarefas': tarefas})

if __name__=='__main__':
    app.run(debug=True)