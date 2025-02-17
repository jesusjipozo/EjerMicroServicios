from flask import Flask, jsonify
import requests

app4 = Flask(__name__)

# Definir las URLs de los microservicios
MS1_URL = "http://127.0.0.1:5000"  # Microservicio Geo
MS2_URL = "http://127.0.0.1:5001"  # Microservicio Meteo
MS3_URL = "http://127.0.0.1:5002"  # Microservicio Demo

@app4.route('/<int:municipioid>/<path:subpaths>', methods=['GET'])
def get_combined_data(municipioid, subpaths=None):
    # Dividir las rutas en una lista de servicios
    services = subpaths.split('/')

    geo_data, meteo_data, demo_data = None, None, None

    # Iterar sobre los servicios en la URL para hacer las solicitudes correspondientes
    for service in services:
        if service == "geo":
            # Realizar la solicitud al microservicio de Geo
            print(f"Haciendo solicitud GET a: {MS1_URL}/{municipioid}/geo")
            response = requests.get(f"{MS1_URL}/{municipioid}/geo")
            print("Respuesta de MS1:", response.status_code, response.text)

            if response.status_code == 200:
                geo_data = response.json()
            else:
                return jsonify({'error': 'Error al obtener datos Geo'}), 404

        elif service == "meteo":
            # Realizar la solicitud al microservicio de Meteo
            print(f"Haciendo solicitud GET a: {MS2_URL}/{municipioid}/meteo")
            response = requests.get(f"{MS2_URL}/{municipioid}/meteo")
            print("Respuesta de MS2:", response.status_code, response.text)

            if response.status_code == 200:
                meteo_data = response.json()
            else:
                return jsonify({'error': 'Error al obtener datos Meteo'}), 404

        elif service == "demo":
            # Realizar la solicitud al microservicio de Demo
            print(f"Haciendo solicitud GET a: {MS3_URL}/{municipioid}/demo")
            response = requests.get(f"{MS3_URL}/{municipioid}/demo")
            print("Respuesta de MS3:", response.status_code, response.text)

            if response.status_code == 200:
                demo_data = response.json()
            else:
                return jsonify({'error': 'Error al obtener datos Demogra'}), 404

        else:
            return jsonify({'error': f"Servicio no válido: {service}"}), 400

    # Retornar los datos obtenidos de los microservicios
    return jsonify({
        "geo": geo_data,
        "meteo": meteo_data,
        "demo": demo_data
    }), 200

if __name__ == '__main__':
    app4.run(port=5003)
