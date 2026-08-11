from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def start():
    return "Primeiro Projeto"

@app.route("/curso")
def curso():
    return jsonify({
        "curso": "Engenharia de Software"
    })

@app.route("/estudante")
def estudante():
    return jsonify({
        "estudante": "Fellipe de Castro"
    })


@app.route("/estudante/<nome>")
def estudanteX(nome):
    return jsonify({
        "Nome": nome,
        "curso": "Engenharia de software",
        "Numero": "1"
    })


if __name__ == "__main__":
    app.run(debug=True)