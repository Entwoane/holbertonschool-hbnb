from flask import Flask
from flask_restx import Api
from app.api.v1.users import api as users_ns
from app.api.v1.amenities import api as amenities_ns

def create_app():
    app = Flask(__name__)
    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API')

    # Register the users namespace
    api.add_namespace(users_ns, path='/api/v1/users')
    return app

app = Flask(__name__)
api = Api(app)

# Ajouter le namespace
api.add_namespace(amenities_ns, path="/api/v1/amenities")
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)  