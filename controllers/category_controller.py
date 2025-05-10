from flask import Blueprint, render_template, request, redirect, url_for
from services.category_service import CategoryService

category_bp = Blueprint('category', __name__)

category_service = CategoryService()

# Listar categorias
@category_bp.route('/')
def list_categories():
    categories = category_service.list_categories()
    return render_template('categories.html', categories=categories)

# Adicionar categoria
@category_bp.route('/add', methods=['GET', 'POST'])
def add_category():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        category_service.add_category(name, description)
        return redirect(url_for('category.list_categories'))
    return render_template('add_category.html')

# Editar categoria
@category_bp.route('/edit/<int:category_id>', methods=['GET', 'POST'])
def edit_category(category_id):
    category = category_service.get_category(category_id)
    if request.method == 'POST':
        category.name = request.form['name']
        category.description = request.form['description']
        category_service.update_category(category)
        return redirect(url_for('category.list_categories'))
    return render_template('edit_category.html', category=category)

# Excluir categoria
@category_bp.route('/delete/<int:category_id>', methods=['POST'])
def delete_category(category_id):
    category_service.delete_category(category_id)
    return redirect(url_for('category.list_categories'))
