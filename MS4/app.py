from flask import Flask, jsonify
import requests

app4 = Flask(__name__)

# Definir las URLs de los microservicios
MS1_URL = "http://host.docker.internal:5000"  # Microservicio Geo
MS2_URL = "http://host.docker.internal:5001"  # Microservicio Meteo
MS3_URL = "http://host.docker.internal:5003"  # Microservicio Demo

@app4.route('/<int:municipioid>/<string:parametro1>/<string:parametro2>', methods=['GET'])
def get_combined_data(municipioid, parametro1, parametro2):
    geo_data, meteo_data, demo_data = None, None, None
    
    # Llamar a los microservicios en función de los valores de parametro1 y parametro2
    if parametro1 == "geo" or parametro2 == "geo":
        print(f"Haciendo solicitud GET a: {MS1_URL}/{municipioid}/geo")
        response = requests.get(f"{MS1_URL}/{municipioid}/geo")
        if response.status_code == 200:
            geo_data = response.json()
        else:
            return jsonify({'error': 'Error al obtener datos Geo'}), 404
    
    if parametro1 == "meteo" or parametro2 == "meteo":
        print(f"Haciendo solicitud GET a: {MS2_URL}/{municipioid}/meteo")
        response = requests.get(f"{MS2_URL}/{municipioid}/meteo")
        if response.status_code == 200:
            meteo_data = response.json()
        else:
            return jsonify({'error': 'Error al obtener datos Meteo'}), 404
    
    if parametro1 == "demo" or parametro2 == "demo":
        print(f"Haciendo solicitud GET a: {MS3_URL}/{municipioid}/demo")
        response = requests.get(f"{MS3_URL}/{municipioid}/demo")
        if response.status_code == 200:
            demo_data = response.json()
        else:
            return jsonify({'error': 'Error al obtener datos Demogra'}), 404
    
    return jsonify({
        "geo": geo_data,
        "meteo": meteo_data,
        "demo": demo_data
    }), 200

if __name__ == '__main__':
    app4.run(port=5004)
