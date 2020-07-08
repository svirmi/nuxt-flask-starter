from flask import Flask
from flask_restful import Resource, Api
import dask.array as da

app = Flask(__name__)
api = Api(app)


class Product(Resource):
    def get(self):
        x = da.random.random((4, 4), chunks=(4, 4))
        return {
            'product' : [
                "Product 1",
                "Product 2",
                "Product 3"
            ],
            'dask' : x.compute().tolist()
        }
api.add_resource(Product, '/api')

if __name__ == '__main__':
    app.run(host = '0.0.0.0',port=5000)