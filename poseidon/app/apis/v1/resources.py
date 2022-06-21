import os

from flask.views import MethodView
from flask import jsonify, request, send_file, send_from_directory, current_app

from app.apis.v1 import api_v1
from app.utils import rename_file
from app.models import FileManager
from app.extensions import db



class FileServerAPI(MethodView):
    def get(self, file_id):
        if file_id is None:
            files = FileManager.query.all()
            all_files = [{
                'id':f.id,
                'file_oname':f.file_oname,
                'file_fname':f.file_fname,
                'file_size':f.file_size,
                'uploader_name': f.uploader_name,
                'uploader_email': f.uploader_email,
                'upload_time':f.upload_time,
                'file_oname_only': f.file_oname_only,
                'meta': f.meta
            } for f in files]
            return jsonify({
                'status':'ok',
                'files': all_files
            })
        elif request.url.endswith('download'):
            return jsonify({
                'status': 'ok',
                'file': {
                    'name': f'download-{file_id}'
                }
            })
        else:
            return jsonify({
                'status': 'ok',
                'file':{
                    'name': 'get one'
                }
            })
    # 上传文件
    def post(self):
        f = request.files.get('file')
        file_oname = f.filename
        file_fname = rename_file(f.filename)
        file_path = os.path.join(current_app.config['FILE_STORE'], file_fname)
        f.save(file_path)
        content_length = os.path.getsize(file_path)
        new_file = FileManager(
            file_oname = file_oname,
            file_fname = file_fname,
            uploader_name = 'yijie',
            file_size = content_length,
            uploader_email = 'yijie.wu@apple.com'
        )

        db.session.add(new_file)
        db.session.commit()
        return jsonify({
            'status': 'ok',
            'file': {
                'file_oname': new_file.file_oname,
                'file_fname': new_file.file_fname,
                'uploader_name': new_file.uploader_name,
                'file_size':new_file.file_size,
                'uploader_email': new_file.uploader_email
            }
        })

    def delete(self, file_id):
            return jsonify({
                'status': 'ok',
                'file': {
                    'name': f'delete-{file_id}'
                }
            })



fileapi = FileServerAPI.as_view('file_api')

api_v1.add_url_rule('/files/',defaults={'file_id': None}, view_func=fileapi, methods=['GET'])
api_v1.add_url_rule('/files/upload', view_func=fileapi, methods=['POST'])
api_v1.add_url_rule('/files/<int:file_id>', view_func=fileapi, methods=['GET', 'DELETE'])
api_v1.add_url_rule('/files/<int:file_id>/download', view_func=fileapi, methods=['GET'])
