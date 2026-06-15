from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Sistema de Gerenciamento de Biblioteca"

@app.route("/sobre")
def sobre():
    return "Sistema desenvolvido em Flask para estudo de CI/CD"

@app.route("/livros")
def livros():
    return "Lista de livros cadastrados"


@app.route("/cadastro-livro")
def cadastro_livro():
    return "Formulário de cadastro de livros"

@app.route("/autores")
def autores():
    return "Lista de autores cadastrados"

@app.route("/contato")
def contato():
    return "Página de contato do sistema"

@app.route("/status")
def status():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True)
