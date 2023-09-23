from flask import Flask, render_template
from mongo import MongoConnection
import pymongo

app = Flask(__name__)

# Configura la conexión a la base de datos MongoDB
db_client = MongoConnection().client
db = db_client.get_database('despegar')
col = db.get_collection('flights')


@app.route('/')
def index():
    # Consulta todos los documentos en la colección 'flights'
    flights_data = col.find({})

    # Renderiza una plantilla HTML para mostrar los datos
    return render_template('index.html', flights=flights_data)


if __name__ == '__main__':
    app.run(debug=True)
