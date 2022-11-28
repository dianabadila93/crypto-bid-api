from flask import Blueprint
from flask_restplus import Api
from src.api.documented_endpoints.bids import bidsNamespace as bidsNamespace


blueprint = Blueprint('documented_api', __name__, url_prefix='/documented_api')

api_extension = Api(
    blueprint,
    title='BIDS API',
    version='1.0',
    description='BIDS API',
    doc='/doc'
)

api_extension.add_namespace(bidsNamespace)