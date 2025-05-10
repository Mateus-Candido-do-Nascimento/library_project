from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.author import Author
from services.author_service import AuthorService
from config.database import db

author_bp = Blueprint('author', __name__)

# Inicializa o serviço de autores
author_service = AuthorService(db.session)

# Listar autores
@author_bp.route('/')
def list_authors():
    authors = author_service.list_authors()
    return render_template('authors.html', authors=authors)

# Adicionar autor
@author_bp.route('/add', methods=['GET', 'POST'])
def add_author():
    if request.method == 'POST':
        name = request.form['name']
        biography = request.form['biography']  # Alterando de bio para biography para consistência

        if not name or not biography or len(biography) < 10:
            flash("Nome e biografia são obrigatórios. A biografia deve ter pelo menos 10 caracteres.", "error")
            return render_template('add_author.html')

        author = Author(name=name, biography=biography)
        try:
            author_service.add_author(author)
            flash("Autor adicionado com sucesso!", "success")
            return redirect(url_for('author.list_authors'))
        except ValueError as e:
            flash(str(e), "error")
            return render_template('add_author.html')

    return render_template('add_author.html')

# Editar autor
@author_bp.route('/edit/<int:author_id>', methods=['GET', 'POST'])
def edit_author(author_id):
    author = author_service.get_author(author_id)
    if not author:
        flash("Autor não encontrado.", "error")
        return redirect(url_for('author.list_authors'))

    if request.method == 'POST':
        author.name = request.form['name']
        author.biography = request.form['biography']  # Alterando de bio para biography para consistência

        if not author.name or not author.biography or len(author.biography) < 10:
            flash("Nome e biografia são obrigatórios. A biografia deve ter pelo menos 10 caracteres.", "error")
            return render_template('edit_author.html', author=author)

        try:
            author_service.update_author(author)
            flash("Autor atualizado com sucesso!", "success")
            return redirect(url_for('author.list_authors'))
        except ValueError as e:
            flash(str(e), "error")
            return render_template('edit_author.html', author=author)

    return render_template('edit_author.html', author=author)

# Excluir autor
@author_bp.route('/delete/<int:author_id>', methods=['POST'])
def delete_author(author_id):
    author_service.delete_author(author_id)
    flash("Autor excluído com sucesso!", "success")
    return redirect(url_for('author.list_authors'))
