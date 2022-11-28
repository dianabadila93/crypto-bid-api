from flask import Flask
from flask_restplus import Api
from src.api.controllers.bid_controller import blueprint \
    as bids_blueprint
from src.api.documented_endpoints import blueprint \
    as documented_endpoints_blueprint

app = Flask(__name__)
app.config['RESTPLUS_MASK_SWAGGER'] = False

app.register_blueprint(documented_endpoints_blueprint)
app.register_blueprint(bids_blueprint)

if __name__ == "__main__":
    app.run()