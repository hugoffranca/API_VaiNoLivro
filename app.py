from flask import Flask, request, jsonify

app = Flask(__name__)

import sqlite3

def init_db():
    # sqlite3 crie o arquivo database.db e se conecte com a variável conn (connection)
    with sqlite3.connect("database.db") as conn:
        conn.execute("""
                CREATE TABLE IF NOT EXISTS LIVROS(
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     titulo TEXT NOT NULL,
                     categoria TEXT NOT NULL,
                     autor TEXT NOT NULL,
                     image_url TEXT NOT NULL
                     )
        """)
    
init_db()

@app.route("/home_msg")
def home_msg():
    
    return "<h3>Olá! Essa aqui é a rota /home_msg </h3>"


@app.route("/doar", methods =["POST"])

def doar():
    dados = request.get_json()
    titulo = dados.get("titulo")
    categoria = dados.get("categoria")
    autor = dados.get("autor")
    image_url = dados.get("image_url")
    if not titulo or not categoria or not autor or not image_url:
        return jsonify({"erro":"Todos os campos são obrigatórios"}),400
    with sqlite3.connect("database.db") as conn: 
        conn.execute(f"""
        INSERT INTO LIVROS (titulo, categoria, autor, image_url) 
        VALUES ("{titulo}", "{categoria}", "{autor}", "{image_url}")
        """)
        conn.commit()

    return jsonify({"mensagem": "O livro foi doado com sucesso"}), 201

    

if __name__ == "__main__":
    app.run(debug=True)

