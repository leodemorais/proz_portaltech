from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Mapeamento de rotas para serviços
service_mapping = {
    '/service1': 'http://localhost:5001',
    '/service2': 'http://localhost:5002',
}

@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def route_request(path):
    if path in service_mapping:
        # Obtemos o URL do serviço de acordo com a rota
        service_url = service_mapping[path]

        # Encaminha a solicitação para o serviço correspondente
        response = requests.request(
            method=request.method,
            url=f"{service_url}/{path}",
            headers=request.headers,
            data=request.data
        )

        # Retorna a resposta do serviço
        return (response.content, response.status_code, response.headers.items())

    return jsonify({'error': 'Rota não encontrada'}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
