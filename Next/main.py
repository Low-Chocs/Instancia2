from flask  import Flask, jsonify, request


app = Flask(__name__)

@app.route('/check', methods=['GET'])
def check_status():
    return 'OK', 200

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "Instancia": "Instancia #1 - API #1",
        "Curso": "Seminario de Sistemas 1",
        "Estudiante": "Luis Mariano Moreira García 202010770"
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)