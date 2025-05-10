from flask import Blueprint, render_template, request, redirect, url_for
from models.client import Client
from services.client_service import ClientService
from config.database import db

client_bp = Blueprint('client', __name__)

# Inicializa o serviço de clientes
client_service = ClientService(db.session)

# Listar clientes
@client_bp.route('/')
def list_clients():
    clients = client_service.list_clients()
    return render_template('clients.html', clients=clients)

# Adicionar cliente
@client_bp.route('/add', methods=['GET', 'POST'])
def add_client():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        client = Client(name=name, email=email)
        client_service.add_client(client)
        return redirect(url_for('client.list_clients'))
    return render_template('add_client.html')

# Editar cliente
@client_bp.route('/edit/<int:client_id>', methods=['GET', 'POST'])
def edit_client(client_id):
    client = client_service.get_client(client_id)
    if request.method == 'POST':
        client.name = request.form['name']
        client.email = request.form['email']
        client_service.update_client(client)
        return redirect(url_for('client.list_clients'))
    return render_template('edit_client.html', client=client)

# Excluir cliente
@client_bp.route('/delete/<int:client_id>', methods=['POST'])
def delete_client(client_id):
    client_service.delete_client(client_id)
    return redirect(url_for('client.list_clients'))
