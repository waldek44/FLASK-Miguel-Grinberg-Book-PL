from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
# importy dla formularza
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'CZEGO TO NIE MA NA NETFLIX'
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.errorhandler(404)
def page_not_found():
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error():
    return render_template('500.html'), 500


# definiuję klasę formularza
class NameForm(FlaskForm):
    name = StringField('Jak masz na imię?', validators=[DataRequired()])
    submit = SubmitField('Wyślij')


@app.route('/', methods=['GET', 'POST'])
# gdy użytkownik pierwszy raz wejdzie na stronę funkcja otrzyma żądanie GET bez danych z formularza, więc funkcja
# validate_on_submit() zwraca False. If zostanie pominięte, żądanie wyrenderuje szablon. Szablon pobierze form i
# przypisze name = None
def index():
    form = NameForm()  # renderuję formularz jak przekażę zmienną form do szablonu

    # funkcja validate_on_submit() zwraca True po przesłaniu formularza i zaakceptowaniu danych przez walidatory
    # od kiedy użytkownik wyśle formularz, wprowadzone przez niego dane dostępne są w atrybucie data
    if form.validate_on_submit():
        old_name = session.get('name')
        # if dla przykładowego wyświetlania flash
        if old_name is not None and old_name != form.name.data:
            flash('Wygląda na to, że zmieniłeś imię. Szok!')
        # if był tylko dla przykładowego wyświetlania flash
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', current_time=datetime.utcnow(), form=form, name=session.get('name'))


# wprowadzam do paska http://127.0.0.1:5000/user/superman
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)
