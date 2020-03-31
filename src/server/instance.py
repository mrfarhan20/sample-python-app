from flask import Flask
from flask_restplus import Api, Resource, fields
from environment.instance import environment_config

class Server:
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app,
            version=1.0,
            title="Halal Guys API",
            description="This a simple food menu API",
            doc=environment_config['swagger_url']
        )
        
    
    def run(self):
        self.app.run(
            port = environment_config['port'],
            debug = environment_config['debug']
        )

server = Server()

