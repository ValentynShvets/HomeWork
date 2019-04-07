import flask
import flask_restful
from resources.notes import Notes
from webargs.flaskparser import parser, abort

app = flask.Flask(__name__)
api = flask_restful.Api(app)


api.add_resource(Notes, '/')


@parser.error_handler
def handle_error(error, req, schema, *args):
    raise abort(422, errors=error.messages)

if __name__ == '__main__':
    app.run(debug=True)