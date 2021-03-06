from flask import flash, redirect, url_for
from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def current_user(user_id):
    return User.query.get(user_id)

@login_manager.unauthorized_handler
def unauthorized_callback():
    flash('Você tem que estar logado!', 'danger')
    return redirect(url_for('auth.login'))


class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(84), nullable=False)
    email = db.Column(db.String(84), nullable=False, unique=True, index=True)
    password = db.Column(db.String(255), nullable=False)

    def __str__(self):
        return self.name