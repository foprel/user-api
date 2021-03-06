from flask import Flask
from .routes.index import index
from .routes.register import register
from .routes.login import login
from .routes.logout import logout
from .routes.resource import resource
from .models.users import db
from .config import Development


api = Flask(__name__)
api.config.from_object(Development)
db.init_app(api)

api.register_blueprint(index)
api.register_blueprint(register)
api.register_blueprint(login)
api.register_blueprint(logout)
api.register_blueprint(resource)

@api.before_first_request
def initialize_database():
    #Todo: Create databases directory
    db.create_all()

if __name__ == '__main__':
    api.run(host='0.0.0.0', port='5000')