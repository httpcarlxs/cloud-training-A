from flask import Flask, request
import logging

app = Flask(__name__)

logging.basicConfig(filename='aplicacao_a.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/endpoint', methods=['POST'])
def endpoint_handler():
    data = request.json
    logging.info(f"Requisição recebida: {data}")
    return "Requisição recebida com sucesso"

if __name__ == '__main__':
    app.run(host='10.11.19.192', port=5000)