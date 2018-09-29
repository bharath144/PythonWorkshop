import flask
APP = flask.Flask(__name__)

@APP.route('/', methods=['GET'])
def hello_world():
    """Returning a simple message"""
    print("Breakpoint on this line...")
    return "Hello World!"

@APP.route('/surprise', methods=['GET'])
def surprise():
    """A specific endpoint"""
    return flask.render_template('surprise.html')

def main():
    """Main module method, starts up the flask APP"""
    APP.run()

if __name__ == '__main__':
    main()
