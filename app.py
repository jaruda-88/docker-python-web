from flask import Flask
import views.login as login

app = Flask(__name__)
app.register_blueprint(login.bp)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5050', debug=True)