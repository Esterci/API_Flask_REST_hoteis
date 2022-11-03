from flask import Flask
from flask_restful import Api
from resources.hotel import Hoteis, Hotel, HotelRegister
from flask_cors import CORS
from sqlalchemy import create_engine
from config import DATABASE_URI

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

api = Api(app)
cors = CORS(app)
engine = create_engine(DATABASE_URI)

@app.route("/")
def index():
    return "<h1>Bem vindo ao teste da STEMIS!!!</h1>"

@app.before_first_request
def cria_banco():
    banco.create_all()

api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')
api.add_resource(HotelRegister, '/registrar-hoteis/')

if __name__ == '__main__':
    from sql_alchemy import banco
    
    banco.init_app(app)
    with app.app_context():
        banco.create_all()
    app.run(host="0.0.0.0", debug=True, port="5000")
