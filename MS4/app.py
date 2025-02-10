from flask import Flask, jsonify
import requests
import json

app2 = Flask(__name__)

API_BASE_URL = "https://www.el-tiempo.net/api/json/v2/provincias/18/municipios"


# Función para obtener los datos meteorológicos
def get_meteo_data(municipioid):
    try:
        # Hacer la petición a la API del tiempo
        url = f"{API_BASE_URL}/{municipioid}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json().get("today", {})
        meteo = {
            "Temperatura Actual": data.get("temperatura_actual"),
            "Temperatura Máxima": data.get("temperatura_maxima"),
            "Temperatura Mínima": data.get("temperatura_minima"),
            "Humedad": data.get("humedad"),
            "Viento": data.get("viento", {}).get("velocidad"),
            "Precipitación": data.get("precipitacion", "Desconocida"),
            "Lluvia": data.get("lluvia", "No especificada")
        }
        return meteo, None
    except requests.RequestException as e:
        return None, f"Error al conectar con la API: {str(e)}"


# Función para obtener los datos del municipio desde municipio.json
def get_municipio_data(municipioid):
    try:
        with open("municipio.json", "r") as file:
            municipio = json.load(file)
            if municipio["municipioid"] == municipioid:
                return municipio, None
            return None, "Municipio no encontrado"
    except FileNotFoundError:
        return None, "Archivo municipio.json no encontrado"
    except json.JSONDecodeError:
        return None, "Error al procesar el archivo municipio.json"


# Función para obtener los datos de demografía desde demografia.json
def get_demografia_data(municipioid):
    try:
        with open("demografia.json", "r") as file:
            demografia = json.load(file)
            if demografia["municipioid"] == municipioid:
                return demografia, None
            return None, "Demografía no encontrada"
    except FileNotFoundError:
        return None, "Archivo demografia.json no encontrado"
    except json.JSONDecodeError:
        return None, "Error al procesar el archivo demografia.json"


@app2.route('/<int:municipioid>/meteo', methods=['GET'])
def get_meteo(municipioid):
    """
    Devuelve los datos meteorológicos de un municipio.
    """
    meteo, error = get_meteo_data(municipioid)
    if meteo:
        return jsonify(meteo), 200
    return jsonify({"error": error}), 500


@app2.route('/<int:municipioid>/geo', methods=['GET'])
def get_geo(municipioid):
    """
    Devuelve los datos geográficos (municipio) de un municipio.
    """
    municipio, error = get_municipio_data(municipioid)
    if municipio:
        return jsonify(municipio), 200
    return jsonify({"error": error}), 500


@app2.route('/<int:municipioid>/demografia', methods=['GET'])
def get_demografia(municipioid):
    """
    Devuelve los datos demográficos de un municipio.
    """
    demografia, error = get_demografia_data(municipioid)
    if demografia:
        return jsonify(demografia), 200
    return jsonify({"error": error}), 500


@app2.route('/<int:municipioid>/<string:x>/<string:y>', methods=['GET'])
def get_meteo_and_other_data(municipioid, x, y):
    """
    Devuelve los datos de `x` primero y luego los de `y`.
    Se pueden pasar como `meteo`, `geo` o `demografia`.
    """
    result = {}

    # Procesar la primera parte de la ruta (x)
    if x == "meteo":
        meteo, error = get_meteo_data(municipioid)
        result[x] = meteo if meteo else {"error": error}
    elif x == "geo":
        municipio, error = get_municipio_data(municipioid)
        result[x] = municipio if municipio else {"error": error}
    elif x == "demografia":
        demografia, error = get_demografia_data(municipioid)
        result[x] = demografia if demografia else {"error": error}

    # Procesar la segunda parte de la ruta (y)
    if y == "meteo":
        meteo, error = get_meteo_data(municipioid)
        result[y] = meteo if meteo else {"error": error}
    elif y == "geo":
        municipio, error = get_municipio_data(municipioid)
        result[y] = municipio if municipio else {"error": error}
    elif y == "demografia":
        demografia, error = get_demografia_data(municipioid)
        result[y] = demografia if demografia else {"error": error}

    return jsonify(result), 200


if __name__ == '__main__':
    app2.run(port=5003)
