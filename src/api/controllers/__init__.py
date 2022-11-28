from src.api.controllers.bid_controller import blueprint \
    as bids_blueprint
from flask import Blueprint
from flask_restx import Api
from src.api.controllers.bid_controller import bidsNamespace

api_extension = Api(
    bids_blueprint,
    title='BIDS API',
    version='1.0',
    description='BIDS API',
    doc='/swagger'
)

api_extension.add_namespace(bidsNamespace)