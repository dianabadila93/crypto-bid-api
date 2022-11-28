from flask import Blueprint, request
from flask_restx import Namespace, Resource, fields
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
class Bid(Resource): 
    @bidsNamespace.response(500, 'Internal Server Error')
    def get(self):
        '''List all bids'''
        return bid_example

    @bidsNamespace.expect(bid_example)
    @bidsNamespace.response(500, 'Internal Server error')
    def post(self):
        '''Create a new bid'''
        return bid_example


@bidsNamespace.route('/<int:id>')
class Bids(Resource):
    @bidsNamespace.response(400, 'Entity with the given name already exists')
    @bidsNamespace.response(404, 'Entity not found')
    @bidsNamespace.response(500, 'Internal Server error')
    @bidsNamespace.expect(bids_model, validate=True)
    @bidsNamespace.marshal_with(bids_model)
    def put(self, id):
        '''Update entity information'''

        if request.json['name'] == 'Bid name':
            bidsNamespace.abort(400, 'Bid with the given name already exists')

        return bid_example
    
    
    @bidsNamespace.response(204, 'Request Success (No Content)')
    @bidsNamespace.response(404, 'Entity not found')
    @bidsNamespace.response(500, 'Internal Server error')
    def delete(self, id):
        '''Delete a specific entity'''

        return '', 204
