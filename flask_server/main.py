from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api()

class Main(Resource):
    def get(self, my_str):
        print(my_str)
        return {'info': 'Some info', 'num': my_str}

    # def post(self, my_str):
    #     print(my_str)
    #     return my_str


api.add_resource(Main, '/api/main/<string:my_str>')
api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, port=3000, host='127.0.0.1')