from flask import (
    Blueprint, request
)

from RasaBot import rasaAgentManager

bp = Blueprint('handler', __name__, url_prefix='/GelatoBot')


@bp.route('/Converse', methods=['POST'])
def bot_response():
    if request.json:
        request_data = request.json
        bot_message = rasaAgentManager.get_bot_response(request_data["userMsg"], request_data["sessionId"])
        return {"success": True, "bot_message": bot_message}, 200
    return {"success": False, "reason": "bad_request_format"}, 400
