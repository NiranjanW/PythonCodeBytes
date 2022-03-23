from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__,static_url_path = '/docs/static')

SWAGGER_URL = "/api/docs"  # URL for exposing Swagger UI (without trailing '/')
# API_URL = 'http://petstore.swagger.io/v2/swagger.json'  # Our API url (can of course be a local resource)
API_URL = "/docs/swagger.yml"


swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={"app_name": "Test application"},  # Swagger UI config overrides
)

app.register_blueprint(swaggerui_blueprint)

app.run()
