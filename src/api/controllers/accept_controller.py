from flask import Blueprint, request
from flask_restx import Namespace, Resource, fields
#http://127.0.0.1:5000/accept_api/swagger

blueprint = Blueprint('accept_api', __name__, url_prefix='/accept_api')

acceptNamespace = Namespace('Accept', 'accept related endpoints')
accept_example = {'id': 1, 'name': 'accept 1', 'description': 'accept 1 description'}


@acceptNamespace.route('')
class accept(Resource): 
    @acceptNamespace.response(500, 'Internal Server Error')
    def get(self):
        '''List all acceptions'''
        return accept_example