from flask import Flask, request, g
from flask_cors import CORS
from flask_jwt import JWT
from flask_restful_swagger_2 import Api

import logging
from logging.handlers import RotatingFileHandler

from support.jwt import authenticate, identity


app = Flask(__name__)
app.config['SECRET_KEY'] = '!owQzm[pn;?11K'
app.config['JWT_AUTH_URL_RULE'] = '/auth'
app.config['JWT_AUTH_USERNAME_KEY'] = 'id'
app.config['JWT_AUTH_PASSWORD_KEY'] = 'pw'
# For JWT authenticate

CORS(app)
# For swagger & AJAX
JWT(app, authentication_handler=authenticate, identity_handler=identity)

api = Api(app, api_version='1.0')


@app.before_first_request
def before_first_request():
    def make_logger():
        handler = RotatingFileHandler('server_log.log', maxBytes=100000, backupCount=5)
        handler.setFormatter(logging.Formatter("[%(asctime)s] %(levelname)s - %(message)s"))

        app.logger.addHandler(handler)
        app.logger.setLevel(logging.INFO)

        return app.logger

    g.logger = make_logger()
    g.logger.info('------ Logger Initialized ------')


@app.before_request
def before_request():
    if 'logger' in g:
        g.logger.info(f'Requested from {request.host} [ {request.method} {request.url} ]')
        g.logger.info(f'Request values : {request.values}')


@app.after_request
def after_request(response):
    if 'logger' in g:
        g.logger.info(f'Respond : {response.status}')

    return response


@app.teardown_request
def teardown_request(exception):
    if 'logger' in g and not exception:
        g.logger.info('Teardown request successfully.')


@app.teardown_appcontext
def teardown_appcontext(exception):
    if 'logger' in g and not exception:
        g.logger.info('Teardown appcontext successfully.')


def add_resources():
    def add_api():
        from routes.api.user.account import Signup
        from routes.api.post.post import Post

        api.add_resource(Signup, '/signup')
        api.add_resource(Post, '/post')

    def add_templates():
        pass

    add_api()
    add_templates()


if __name__ == '__main__':
    add_resources()
    app.run(debug=True)
