from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from repositories.client_repository import ClientRepository
from database import db_session

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        client_repo = ClientRepository(db_session)
        client = client_repo.get_client_by_email(email)

        if client:
            session['client_id'] = client.id
            session['client_name'] = client.name
            return redirect(url_for('book.list_books'))
        else:
            flash('E-mail não encontrado. Verifique e tente novamente.', 'error')

    return render_template('login.html')
