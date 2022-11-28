from flask import Blueprint, request

blueprint = Blueprint('api', __name__, url_prefix='/basic_api')

@blueprint.route('/documented_api', methods=['GET'])
def hello_world():
    return {'message': 'Hello API!'}
