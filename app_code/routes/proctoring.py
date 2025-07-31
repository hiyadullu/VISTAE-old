#log saving and all
from flask import Blueprint, request, jsonify

bp = Blueprint('proctoring', __name__, url_prefix='/proctor')

@bp.route('/upload_snapshot', methods=['POST'])
def upload_snapshot():
    image_data = request.files['image']
    image_data.save(f'snapshots/snap_{image_data.filename}')
    return jsonify({'status': 'saved'})
