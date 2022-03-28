from flask import Flask
import views.index as index
import views.register as register
import views.board as board


app = Flask(__name__)
app.register_blueprint(index.bp)
app.register_blueprint(register.bp)
app.register_blueprint(board.bp)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5050', debug=True)