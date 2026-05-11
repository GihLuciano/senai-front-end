"""
Esse arquivo é um exemplo de controller
"""

from flask import Blueprint, request, redirect, url_for, render_template, flash, session
from werkzeug.security import check_password_hash, generate_password_hash

from database import db
from models import User

bp = Blueprint(__name__, "HomeController")

@bp.route("/") # cria uma rota teste
def index(): # função que gerencia rota
    """ Página inicial"""
    if '_user_id' not in session:
        return redirect(url_for("auth.login"))
    
    return render_template("dashboard/index.html") # Renderiza um template
    
@bp.route("/dashboard") # cria uma rota
def dashboard(): # função que gerencia rota
    """ Painel de Vendas"""
    # if 'user' not in session:
    #     return redirect(url_for("auth.login"))

    import locale
    # Define para o padrão brasileiro
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

    vendas: list = [
        {"mes":"Janeiro", "total": 139519.19},
        {"mes":"Fevereiro", "total": 139594.99},
        {"mes":"Março", "total": 128519.31},
        {"mes":"Abril", "total": 114529.99},
        {"mes":"Maio", "total": 157893.22},
        {"mes":"Junho", "total": 139429.29},
        {"mes":"Julho", "total": 145893.17},
        {"mes":"Agosto", "total": 199519.19},
        {"mes":"Setembro", "total": 109549.60},
        {"mes":"Outubro", "total": 119519.19},
        {"mes":"Novembro", "total": 179519.19},
        {"mes":"Dezembro", "total": 209529.29},
    ] # fim lista vendas
    
    return render_template("dashboard/index.html", vendas=vendas, locale=locale) # Renderiza um template