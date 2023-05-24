from flask import Flask, request, make_response

SECRET_KEY = '18afb34edaf10eaa2bfcf5f03106123e'

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home_page():
    return "Welcome to homepage"

@app.route('/register')
def register_competition():
    if request.method != 'POST':
        err_resp = make_response('Method not allowed', 405)
        return err_resp
    else:


if __name__ == '__main__':
    app.run(port=8080)