from flask.helpers import flash
from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.email import Email

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def process():
    if not Email.is_valid(request.form):
        return redirect('/')
    
    Email.submit_email(request.form)

    return redirect('/success')


@app.route('/success')
def results():
    flash("GREAT SUCCESS", "message")
    return render_template("success.html", all_emails=Email.get_emails())


@app.route('/delete/<int:id>')
def delete(id):
    data = {
        "id": id
    }
    Email.delete(data)

    return redirect('/success')