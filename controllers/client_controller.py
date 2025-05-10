from flask import Blueprint, render_template, request
from services.client_service import ClientService
from database import SessionLocal

client_bp = Blueprint('client', __name__)

@client_bp.route('/')
def list_clients():
    try:
        # Cria uma nova sessão para o serviço
        db_session = SessionLocal()
        client_service = ClientService(db_session)

        # Chama o serviço para listar os clientes
        clients = client_service.list_clients()

        # Fecha a sessão
        db_session.close()

        return render_template('clients.html', clients=clients)
    except Exception as e:
        return render_template('error.html', message=str(e)), 500
