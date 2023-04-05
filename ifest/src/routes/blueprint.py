from flask import Blueprint
from controllers.chatController import testeChat

blueprint = Blueprint('blueprint', __name__)

blueprint.route('/teste', methods=['GET'])(testeChat)