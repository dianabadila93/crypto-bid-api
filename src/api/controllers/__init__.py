from src.api.controllers.bid_controller import blueprint \
    as bids_blueprint
from flask import Blueprint
from flask_restx import Api
from src.api.controllers.bid_controller import bidsNamespace
from src.api.controllers.interract_controller import interactNamespace
from src.api.controllers.accept_controller import acceptNamespace



api_extension = Api(
    bids_blueprint,
    title='BIDS API',
    version='1.0',
    description='BIDS API',
    doc='/swagger'
)


api_extension.add_namespace(bidsNamespace)
api_extension.add_namespace(interactNamespace)
api_extension.add_namespace(acceptNamespace)

