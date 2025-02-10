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
    app1.run(port=5000)





'''
1. para crear la carpeta venv1, que es donde se descragn las dependencias, en terminal de carpeta padre:
    python3 -m venv venv1

2. para que las cosas que se instalen solo dentro de venv1, en terminal de carpeta padre:  
    source venv1/bin/activate

3. crear el archivo "app.py" dentro de MS1

4. buscar en la api del tiempo un pueblo: 
    - https://www.el-tiempo.net/api/json/v2/provincias
    - buscar la provinicia y coger el numero: en el caso de granada es el 18
    - buscar en la ruta de los municipios con el codigo que se ha codigo
    - https://www.el-tiempo.net/api/json/v2/provincias/18/municipios

5. Se crea en la raiz de MS1, el archivo municipio.json, con los datos que se quiera, el id del municipio son los 5 nume primeros del "CODIGOINE"

6. Se pone en terminal: pip install Flask, para ello hay que estar dentro del entorno, en terminal tiene que salir:
    (venv1) carmen_gordo@pc124-8 venv1 %
    para que salga se pone en temrinal: carmen_gordo@pc124-8 MS1 % source venv1/bin/activate

7. En este archivo, se pone:
    7.0: importar flask y json en app.py, en terminal con entorno hecho:
        pip install Flask
    
    7.1:
        from flask import Flask, jsonify
        import json

        app1 = Flask(__name__)

    7.2: se pone la api
        API_URL = "https://www.el-tiempo.net/api/json/v2/provincias/18/municipios"

    7.3: se crea la funcion, para hacer el llamado
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

    7.4: se pone el puerto 500
        if __name__ == '__main__':
            app1.run(port=5000)

8. en terminal ((venv1) carmen_gordo@pc124-8 MS1 %) se pone python3 app.py y este da una url. en el navegador se abre esta
url, si se pone en nuestro caso: http://127.0.0.1:5000/18057/geo -> da una respuesta con el json, si se pone otro numero que 
no sea parecido al de "municipioid" (que esta en el .json) -> da error

9. En MS2: se crea el "venv2" poniendo en el temrinal: carmen_gordo@pc124-8 MS2 % python3 -m venv venv2

10. Se entra y se hace lo mismo que con el venv1. y se crea el app.py y su metodo, para ello ver ese archivo.
Este dará una nueva url y se le tendra que poner: http://127.0.0.1:5001/18057/meteo y te dara los resultados del meteo del
id que se quiera

11. 




'''