from flask import Flask, jsonify
import requests

app2 = Flask(__name__)

'''funcion: La función deberá hacer un fetch a la API del tiempo devolviendo la temperatura, temperaturas máxima y mínima, humedad, viento, precipitación, lluvia.
Deberá controlarse los errores correspondientes.
'''

@app2.route('/<int:municipioid>/meteo', methods=['GET'])
def get_meteo(municipioid):
    """
    Obtiene información meteorológica de un municipio usando su ID.
    """
    try:
        # Construir la URL para la solicitud
        url = f"{API_BASE_URL}/{municipioid}"
        
        # Realizar la petición a la API del tiempo
        response = requests.get(url)
        response.raise_for_status()  # Detectar errores HTTP

        # Procesar la respuesta JSON
        data = response.json()
        tiempo_actual = data.get("today", {})
        
        # Extraer los datos relevantes
        resultado = {
            "Temperatura Actual": tiempo_actual.get("temperatura_actual"),
            "Temperatura Máxima": tiempo_actual.get("temperatura_maxima"),
            "Temperatura Mínima": tiempo_actual.get("temperatura_minima"),
            "Humedad": tiempo_actual.get("humedad"),
            "Viento": tiempo_actual.get("viento", {}).get("velocidad"),
            "Precipitación": tiempo_actual.get("precipitacion", "Desconocida"),
            "Lluvia": tiempo_actual.get("lluvia", "No especificada")
        }

        return jsonify(resultado), 200

    except requests.RequestException as e:
        return jsonify({"error": f"Error al conectar con la API: {str(e)}"}), 500
    except (ValueError, KeyError):
        return jsonify({"error": "Error al procesar la respuesta de la API"}), 500


if __name__ == '__main__':
    app2.run(port=5001)