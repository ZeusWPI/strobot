from flask import Flask, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from email import message_from_string
from base64 import b64decode

from database import Email, Base, DATABASE_URL


engine = create_engine(DATABASE_URL)
Base.metadata.bind = engine
session = sessionmaker(bind=engine)()

app = Flask(__name__)


@app.route('/strobot', methods=["GET", "PUT", "DELETE"])
def strobot():
    if request.method == "GET":
        return redirect(url_for('static', filename='strozijnhaar.jpg'))
    elif request.method == "PUT":
        email_str = message_from_string(b64decode(request.data))
        email = Email(to=email_str['To'],
                      subject=email_str['Subject'],
                      datetime=email_str['Date'],
                      sender=email_str['From'])
        session.add(email)
        session.commit()
        return 'OK', 200
    elif request.method == "DELETE":
        # remove the email from db
        email_id = request.data
        session.querry(Email).filter(Email.id == email_id).delete()
        session.commit()
        return 'OK', 200
