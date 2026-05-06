from flask import Blueprint, request
from controllers.jogo_controllers import get_jogos, create_jogo, get_jogo_by_id

jogo_routes = Blueprint('jogo_routes', __name__)

@jogo_routes.route('/Jogo', methods=['GET'])
def jogos_get():
    return get_jogos()

@jogo_routes.route('/Jogo/<int:jogo_id>', methods=['GET'])
def jogo_get_by_id(jogo_id):
    return get_jogo_by_id(jogo_id)

@jogo_routes.route('/Jogo', methods=['POST'])
def jogos_post():
    return create_jogo(request.json)