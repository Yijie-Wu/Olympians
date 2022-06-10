from flask import jsonify, request
from flask.views import MethodView

from app.apis.v1 import api_v1


class IndexAPI(MethodView):
    def get(self):
        return jsonify({
            'v1': {
                'index-uri': {
                    'url': 'http://domain/api/v1',
                    'method': 'get',
                    'params': None
                }
            }
        })


class FileServerAPI(MethodView):
    def get(self):
        print('====================')
        print(request.values.get('name'))
        print('====================')
        return jsonify({
            'hello': 'world'
        })


api_v1.add_url_rule('/', view_func=IndexAPI.as_view('index'), methods=['GET'])
api_v1.add_url_rule('/file', view_func=FileServerAPI.as_view('file-server'), methods=['GET'])
