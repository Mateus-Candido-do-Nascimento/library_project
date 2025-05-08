from flask import Blueprint, render_template
from services.client_service import ClientService
import logging

logger = logging.getLogger(__name__)

client_bp = Blueprint('client', __name__)

@client_bp.route('/')
def list_clients(service=None):
    try:
        client_service = service or ClientService()
        clients = client_service.list_clients()
        return render_template('clients.html', clients=clients)
    except Exception as e:
        logger.error(f'Erro ao listar clientes: {e}')
        return render_template('error.html', message="Erro ao carregar lista de clientes."), 500