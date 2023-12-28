from flask import Flask, jsonify, request

app = Flask(__name__)  # cria uma aplicação Flask

livros = [
    {
        "id": 1,
        "título": "O senhor dos Anéis",
        "autor": 'Jrr Hoken'
    }
]

# Consultar (todos)
@app.route("/livros", methods=["GET"])
def obter_livros():
    return jsonify(livros)

# Consultar (id)
@app.route("/livros/<int:id>", methods=["GET"])
def obter_livros_por_id(id): 
    for livro in livros:
        if livro.get("id") == id:
            return jsonify(livro)
app.run(port=5000, host="localhost", debug=True)