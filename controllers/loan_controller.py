from flask import Blueprint, render_template, request
from services.loan_service import LoanService


loan_bp = Blueprint('loan', __name__)

@loan_bp.route('/')
def list_loans():
    try:
        
     

        # Chama o serviço para listar os empréstimos
        

        # Fecha a sessão
        

        return render_template('loans.html', loans=loans)
    except Exception as e:
        return render_template('error.html', message=str(e)), 500
