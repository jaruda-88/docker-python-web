from flask import Flask
import views.login as login

app = Flask(__name__)
app.register_blueprint(login.bp)


if __name__ == '__main__':
    app.run(debug=True)