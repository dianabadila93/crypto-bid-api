from flask import Blueprint, request
from flask_restx import Namespace, Resource, fields
#http://127.0.0.1:5000/interact_api/swagger

blueprint = Blueprint('interact_api', __name__, url_prefix='/interact_api')

interactNamespace = Namespace('Interact', 'Interact related endpoints')
interact_example = {'id': 1, 'name': 'Interact 1', 'description': 'Interact 1 description'}


@interactNamespace.route('')
class Interact(Resource): 
    @interactNamespace.response(500, 'Internal Server Error')
    def get(self):
        '''List all interactions'''
        return interact_example

