from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Configura la URL y los encabezados de la API de Uptime Kuma
API_URL = 'http://localhost:3001/api/monitor'
HEADERS = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer <uk2_4DBZ4eqaqC1Ap0ksVF1HVZW24vaxN1M7Y8LrGvuT>'
}

@app.route('/')
def index():
    response = requests.get(API_URL, headers=HEADERS)
    monitors = response.json()
    return render_template('index.html', monitors=monitors)

if __name__ == '__main__':
    app.run(debug=True)


#Instalar python, pip y requests en Linux
#Clonar el repositorio y ejecutar