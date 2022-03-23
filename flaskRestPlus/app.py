from flask import Flask
from flask_restplus import Api, Resource
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property

flask_app = Flask(__name__)
app = Api(app = flask_app)


name_space = app.namespace('main', description='Main APIs')

@name_space.route('/')
class MainClass(Resource):
    def get(self):
        return {
            "status" : "Got new Data"
        }
    
    def post(self):
        return {
			"status": "Posted new data"
		}

app.run(debug=True)