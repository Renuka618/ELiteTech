from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret123'
socketio = SocketIO(app)

# Store notes (shared text)
shared_text = ""

@app.route("/")
def index():
    return render_template("index.html")

# Handle incoming messages
@socketio.on("message")
def handle_message(msg):
    global shared_text
    shared_text = msg
    send(shared_text, broadcast=True)

if __name__ == "__main__":
    socketio.run(app, debug=True)
