from flask import Flask, jsonify
import json

app1 = Flask(__name__)

'''funcion: La función deberá buscar en el JSON el municipio a través del id. 
En caso de que exista, devuelve 200 OK junto con los datos almacenados en el JSON
En caso de que no exista, devuelve 404'''

@app1.route('/<int:municipioid>/geo', methods=['GET'])
def get_geo(municipioid):
     try:
         # Abrimos el archivo JSON donde están los datos del municipio
         with open('municipio.json') as f:
             data = json.load(f)

         # Buscamos el municipio por su ID
         if data.get('municipioid') == municipioid:
             return jsonify(data), 200  # Municipio encontrado, retornamos 200 OK
         else:
             return jsonify({'error': 'Municipio no encontrado'}), 404  # Municipio no encontrado
     except FileNotFoundError:
         return jsonify({'error': 'Archivo JSON no encontrado'}), 500  # Error si el archivo no existe


if __name__ == '__main__':
    app1.run(port=5001)
