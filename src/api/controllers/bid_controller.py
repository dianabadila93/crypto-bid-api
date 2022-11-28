from flask import Blueprint, request
from flask_restplus import Namespace, Resource, fields
# http://127.0.0.1:5000/bids_api/swagger
blueprint = Blueprint('bids_api', __name__, url_prefix='/bids_api')

bidsNamespace = Namespace('BIDS', 'Bids related endpoints')
bid_example = {'id': 1, 'name': 'Bid 1', 'description': 'Bid 1 description'}
bids_model = bidsNamespace.model('Bid', {
    'id': fields.Integer(
        readonly=True,
        description='Bid identifier'
    ),
    'name': fields.String(
        required=True,
        description='Bid name'
    ),
    'description': fields.String(
        required=True,
        description='Description of the entity'
    )
})

@bidsNamespace.route('')
class Bids(Resource): 
    bidsNamespace.response(500, 'Internal Server Error')
    def get(self):
        return bid_example

    @bidsNamespace.expect(bid_example)
    @bidsNamespace.response(500, 'Internal Server error')
    def post(self):
        bid_example.name = 'Bid 2'
        return bid_example
