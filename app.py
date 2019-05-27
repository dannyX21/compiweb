#!venv/bin/python3
from flask import Flask, render_template, request, abort, jsonify
from compi.lexico import Lexico
from compi.simbolo import Simbolo

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compila/', methods=['POST'])
def compila():
    if not request.json or not 'codigo' in request.json:
        abort(400)
    else:
        response = {
            'tokens': [],
            'errores': []
        }
        lex = Lexico(request.json['codigo'])
        tokens = []
        while True:
            t = lex.siguiente_componente_lexico()
            if t:
                response['tokens'].append({ 'token': t.Token, 'lexema': t.Lexema})
            else:
                break

        response['errores'] = lex.error.errores
        return (jsonify(response), 200)

    return "Hello World!"

# app.run must go BELOW all the routes.
if __name__ == "__main__":
    app.run(debug=True)
