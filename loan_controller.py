from flask import Blueprint, render_template
from services.loan_service import LoanService
import logging

logger = logging.getLogger(__name__)

loan_bp = Blueprint('loan', __name__)

@loan_bp.route('/')
def list_loans(service=None):
    try:
        loan_service = service or LoanService()
        loans = loan_service.list_loans()
        return render_template('loans.html', loans=loans)
    except Exception as e:
        logger.error(f'Erro ao listar empréstimos: {e}')
        return render_template('error.html', message="Erro ao carregar lista de empréstimos."), 500
