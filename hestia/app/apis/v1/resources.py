from flask.views import MethodView
from flask import jsonify

from app.apis.v1 import api_v1


class HealthCheckAPI(MethodView):
    def get(self):
        return jsonify({'status': 'ok'})


health_api = HealthCheckAPI.as_view('health_api')

api_v1.add_url_rule('/health-check', view_func=health_api, methods=['GET'])
