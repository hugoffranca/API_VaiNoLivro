from flask import Flask

app = Flask(__name__)

@app.route("/pagar")
def exibir_mensagem():
    return "<h1>Pagar as pessoasssss, faz bem as pessoass!!!</h1>"

@app.route("/femandaopix")
def manda_o_pix():
    return "<h2>Se a tela apagou, tá devendo!!!</h2>"

@app.route("/x")
def manda_o_pixx():
    return "<h2>Se a tela apagou, tá devendo!!!</h2>"

if __name__ == "__main__":
    app.run(debug=True)