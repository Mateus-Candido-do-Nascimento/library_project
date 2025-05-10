from flask import Flask, render_template
from config.database import db
from controllers.book_controller import book_bp
from controllers.client_controller import client_bp
from controllers.loan_controller import loan_bp
from controllers.login_controller import login_bp

# ⬇️ Modelos precisam ser importados ANTES do create_all()
from models.book import Book
# (faça o mesmo para os outros modelos: Client, Loan, BookLoan, etc)

app = Flask(__name__)

# Configuração do banco
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Blueprints
app.register_blueprint(login_bp, url_prefix='/login')
app.register_blueprint(book_bp, url_prefix='/books')
app.register_blueprint(client_bp, url_prefix='/clients')
app.register_blueprint(loan_bp, url_prefix='/loans')

@app.route('/')
def home():
    return render_template("login.html")

# Criação das tabelas na primeira execução
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
