from datetime import datetime
from flask import render_template, session, redirect, url_for, current_app
from . import main
from .forms import NameForm
from .. import db
from ..models import User
from ..email import send_email


# gdy użytkownik pierwszy raz wejdzie na stronę funkcja otrzyma żądanie GET bez danych z formularza, więc funkcja
# validate_on_submit() zwraca False. If zostanie pominięte, żądanie wyrenderuje szablon. Szablon pobierze form i
# przypisze name = None
@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        # za każdym razem gdy przesyłane jest imię aplikacja sprawdza je w db za pomocą filtra filter_by()
        # Zmienna known jest zapisywana do sesji użytkownika
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
            if current_app.config['FLASKY_ADMIN']:
                send_email(current_app.config['FLASKY_ADMIN'], 'New User',
                           'mail/new_user', user=user)
        else:
            session['known'] = True
        session['name'] = form.name.data
        return redirect(url_for('.index'))
    return render_template('index.html',
                           form=form, name=session.get('name'),
                           known=session.get('known', False))
