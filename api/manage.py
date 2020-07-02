from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Product(Resource):
    def get(self):
        return {
            'product' : [
                "Product 1",
                "Product 2",
                "Product 333"
            ]
        }
api.add_resource(Product, '/api')

if __name__ == '__main__':
    app.run(host = '0.0.0.0',port=5000)