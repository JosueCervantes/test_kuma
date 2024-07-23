from flask import Flask, render_template
import requests

app = Flask(__name__)

# Configura la URL y los encabezados de la API de Uptime Kuma
API_URL = 'http://localhost:3001/settings/api-keys'
HEADERS = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer <uk3__QPZ9esmnjsbWm5D4zuPgnhHtwnxUK1JFz4Ashj9>'
}

@app.route('/')
def index():
    try: 
        response = requests.get(API_URL, headers=HEADERS)
        response.raise_for_status() 
        print('Response status code:', response.status_code)
        print('Response headers:', response.headers)
        print('Response content:', response.text)
        monitors = response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occured: {http_err}')
        monitors = []
    except requests.exceptions.RequestException as err:
        print(f'Other error occured: {err}')
        monitors = []
    except ValueError as json_err:
        print(f'JSON decode error: {json_err}')
        print(f'Response content: ', response.text)
        monitors = []

    return render_template('index.html', monitors=monitors)

if __name__ == '__main__':
    app.run(debug=True)

