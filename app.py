from flask import Flask, request, redirect, url_for
app = Flask(__name__)

@app.route('/strobot', methods=["GET", "PUT", "DELETE"])
def strobot():
    if request.method == "GET":
        return redirect(url_for('static', filename='strozijnhaar.jpg'))
