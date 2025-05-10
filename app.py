from flask import Flask, render_template
from controllers.book_controller import book_bp
from controllers.client_controller import client_bp
from controllers.loan_controller import loan_bp
from controllers.login_controller import login_bp




app = Flask(__name__)
app.register_blueprint(login_bp, url_prefix='/login')
# Blueprints (rotas)
app.register_blueprint(book_bp, url_prefix='/books')
app.register_blueprint(client_bp, url_prefix='/clients')
app.register_blueprint(loan_bp, url_prefix='/loans')

@app.route('/')
def home():
    return render_template("login.html")

if __name__ == '__main__':
    app.run(debug=True)
