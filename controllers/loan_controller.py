from flask import Blueprint, render_template, request
from services.loan_service import LoanService
from database import SessionLocal

loan_bp = Blueprint('loan', __name__)

@loan_bp.route('/')
def list_loans():
    try:
        # Cria uma nova sessão para o serviço
        db_session = SessionLocal()
        loan_service = LoanService(db_session)

        # Chama o serviço para listar os empréstimos
        loans = loan_service.list_loans()

        # Fecha a sessão
        db_session.close()

        return render_template('loans.html', loans=loans)
    except Exception as e:
        return render_template('error.html', message=str(e)), 500
