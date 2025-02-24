from flask import Flask, jsonify
import requests

app2 = Flask(__name__)

# URL de ejemplo para obtener datos meteorológicos sin API key
WEATHER_API_URL = "https://www.el-tiempo.net/api/json/v2/provincias/{}/municipios/{}"

@app2.route('/<int:municipioid>/meteo', methods=['GET'])
def get_meteo(municipioid):
    try:
        # Convertir el municipioid en provincia y municipio según la API
        provincia_id = str(municipioid)[:2]  # Suponiendo que los primeros 2 dígitos son la provincia
        municipio_str = str(municipioid)
        url = WEATHER_API_URL.format(provincia_id, municipio_str)
        
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            return jsonify({
                "municipioid": municipioid,
                "temperatura": data.get("temperatura_actual", "N/A"),
                "maxima": data.get("temperaturas", {}).get("max", "N/A"),
                "minima": data.get("temperaturas", {}).get("min", "N/A"),
                "humedad": data.get("humedad", "N/A"),
                "viento": data.get("viento", "N/A"),
                "precipitacion": data.get("precipitacion", "N/A")
            }), 200
        else:
            return jsonify({"error": "No se pudo obtener información del tiempo"}), response.status_code
    
    except requests.exceptions.RequestException:
        return jsonify({"error": "Error al conectar con el servicio meteorológico"}), 500

if __name__ == '__main__':
    app2.run(port=5002)