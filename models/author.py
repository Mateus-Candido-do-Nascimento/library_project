# model/author.py

from flask_sqlalchemy import SQLAlchemy
from datetime import date

# Criação da instância db, que será usada para conectar com o banco
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'  # Nome da tabela no banco de dados

    # Definindo as colunas da tabela
    id = db.Column(db.Integer, primary_key=True)  # Chave primária
    name = db.Column(db.String(100), nullable=False)  # Nome do autor
    biography = db.Column(db.Text, nullable=False)  # Biografia do autor

    def __init__(self, name, biography):
        """
        Inicializa um autor com os dados fornecidos, com validação.

        Args:
        name (str): Nome do autor.
        biography (str): Biografia do autor.

        Raises:
        ValueError: Se o nome ou biografia forem inválidos.
        """
        if not name or not isinstance(name, str):
            raise ValueError("O nome do autor deve ser uma string não vazia.")
        if not biography or len(biography) < 10:
            raise ValueError("A biografia deve ser uma string com pelo menos 10 caracteres.")

        self.name = name
        self.biography = biography

    @property
    def get_biography(self):
        """Retorna a biografia do autor."""
        return self.biography

    @get_biography.setter
    def update_biography(self, new_biography):
        """Atualiza a biografia do autor, garantindo que tenha pelo menos 10 caracteres."""
        if not new_biography or len(new_biography) < 10:
            raise ValueError("A biografia deve ser uma string com pelo menos 10 caracteres.")
        self.biography = new_biography

    def __repr__(self):
        """
        Representação em string do autor, com seu nome e ID.
        """
        return f'<Author {self.name} (ID: {self.id})>'
