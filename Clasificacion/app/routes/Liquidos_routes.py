from flask import Blueprint, render_template, request, redirect, url_for, render_template, redirect, url_for, request, flash
from app.models.Liquidos import Liquidos
from app.models import Promotor
from flask_login import login_user, current_user, logout_user, login_required
from flask_bcrypt import Bcrypt
from app import db


bp = Blueprint('Liquidos', __name__)


@bp.route('/Liquidos')
def index():
    data = Liquidos.query.all()
    print("Data ", data)
    return render_template('Liquidos/index.html', data=data)


@bp.route('/Liquidos/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        bcrypt = Bcrypt()
        nombre = request.form['nombre']
       
        new_liq = Liquidos(nombreLiquido=nombre)
        print(new_liq)
        db.session.add(new_liq)
        db.session.commit()
        
        return redirect(url_for('Liquidos.index'))

    return render_template('Liquidos/add.html')

@bp.route('/Liquidos/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    liq = Liquidos.query.get_or_404(id)

    if request.method == 'POST':
        liq.idLiquidos = request.form['nombre']
       
        db.session.commit()
        return redirect(url_for('Liquidos.index'))

    return render_template('Liquidos/edit.html',)

@bp.route('/Liquidos/delete/<int:id>')
def delete(id):
    
    admin = Liquidos.query.get_or_404(id)
    
    db.session.delete(admin)
    db.session.commit()

    return redirect(url_for('Liquidos.index'))



@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('Administrador.login'))