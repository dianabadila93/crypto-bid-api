from flask import request
from flask_restplus import Namespace, Resource, fields

bidsNamespace = Namespace('Bids', 'Bids related endpoints')

bids_model = bidsNamespace.model('Bids', {
    'message': fields.String(
        readonly=True,
        description='Hello world message'
    )
})

hello_world_example = {'message': 'Hello World!'}

@bidsNamespace.route('')
class Bids(Resource):

    @bidsNamespace.marshal_list_with(bids_model)
    @bidsNamespace.response(500, 'Internal Server error')
    def get(self):
        '''Hello world message endpoint'''

        return hello_world_example