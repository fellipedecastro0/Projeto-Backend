from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def start(): 
    return jsonify ({
        "biblioteca": "API",
        "versao": "1.0"
    })

livros = [
    {
        "id" : 10,
        "titulo" : "A volta dos que nao foram",
        "autor" : "Eu"    
    },

    {
        "id" : 11,
        "titulo" : "livro 2 ",
        "autor" : "Eu"    
    },

    {
        "id" : 12,
        "titulo" : "livro 3 ",
        "autor" : "Eu"    
    }
]

@app.route("/livros", methods=["GET"])
def lista ():
    return jsonify(livros) 

@app.route("/livros/<int:id>", methods=["GET"])
def buscar(id):

    for livro in livros:
        if livro ["id"] == id:
            return jsonify(livro)
        
    return jsonify({
        "Erro": "Livro nao encontrado"
    })

@app.route("/livros", methods=["POST"])
def cadastrar():

    dados = request.get_json()

    livros.append(dados)

    return jsonify ({
        "Aviso": "Livro cadastrado com sucesso!!",
        "livro" : dados
    })

@app.route("/livros/<int:id>", methods=["PUT"])
def atualizar(id):

    dados = request.get_json()

    for livro in livros: 
        if livro ["id"] == id:

            livro["titulo"] = dados["titulo"]
            livro["autor"] = dados["autor"] 
            
            return jsonify ({
                "Aviso": "Livro atualizado com sucesso!!",
                "livro":livro
            })
        
    return jsonify ({
        "Erro": "Livro nao encontrado"
    })


@app.route("/livros/<int:id>", methods=["DELETE"])
def delete(id):
    for livro in livros:
        if livro["id"] == id:
            livros.remove(livro)

            return jsonify({
                "Aviso": "livro deletado com sucesso!!"
            })
        
    return jsonify ({
        "Erro": "Livro nao encontrado"
    })


if __name__ == "__main__":
    app.run(debug=True)