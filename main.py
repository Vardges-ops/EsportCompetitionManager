from flask import Flask, request, make_response

SECRET_KEY = '18afb34edaf10eaa2bfcf5f03106123e'

app = Flask(__name__)


@app.route("/", methods=['GET'])
@app.route("/home")
def home_page():
    return "Welcome to homepage"


@app.route('/register', methods=['POST'])
def register_competition():
    if request.method != 'POST':
        err_resp = make_response('Method not allowed', 405)
        return err_resp
    else:
        payload = request.json()
        # TODO validate payload
        # TODO encrypt and tokenize
        # TODO send response


if __name__ == '__main__':
    app.run(port=8080)
