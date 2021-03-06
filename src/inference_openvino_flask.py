from src.service.openvino_network import OpenVinoNetwork
from src.service.api import Api
from flask import Flask, request
from src.service.system_track import SystemTrack

app = Flask(__name__)
api = Api(
    sys=SystemTrack(
        docker=True,
        cloud=True,
        processor_unit='CPU',
        inference_engine='openvino',
        web_engine='Flask'
    ),
    net=OpenVinoNetwork()
)


@app.route('/image', methods=['POST'])
def cloud_storage_handler():
    item = request.json
    api.cloud_storage_request(item)
    return '200'
