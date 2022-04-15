from flask import Flask
import views.index as index
import views.register as register
import views.board as board
import views.board_add as board_add


app = Flask(__name__)
app.register_blueprint(index.bp)
app.register_blueprint(register.bp)
app.register_blueprint(board.bp)
app.register_blueprint(board_add.bp)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5050', debug=True)