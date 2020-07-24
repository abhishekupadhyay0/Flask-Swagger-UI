from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
app.config['SECRET_KEY'] = '0e56ff1ccced7825c18d9ae3a250b491'

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.yml'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL,
    config={
        'app_name': "This is test API to demo swagger"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


@app.route('/inventory')
def inventory():
    return {
            "id": "d290f1ee-6c54-4b01-90e6-d701748f0851",
            "name": "Widget Adapter",
            "releaseDate": "2016-08-29T09:12:33.001Z",
            "manufacturer": {
              "name": "Fiserv Corporation",
              "homePage": "https://www.acme-corp.com",
              "phone": "408-867-5309"
            }
    }
