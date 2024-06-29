from flask import Blueprint, render_template, request, redirect, url_for, render_template, redirect, url_for, request, flash
from app.models.Administrador import Administrador
from app.models.MetodosPago import MetodosPago
from flask_login import login_user, current_user, logout_user, login_required
from flask_bcrypt import Bcrypt
from app import db


bp = Blueprint('MetodosPago', __name__)




@bp.route('/MetodosPagoMein')
@login_required
def index():
    data = MetodosPago.query.all()
    print("Data ", data)
    return render_template('MetodosPago/index.html', data=data)


@bp.route('/MetodosPago/add', methods=['GET', 'POST'])
@login_required
def add():
    if request.method == 'POST':
        nombre = request.form['nombre']
        new_met = MetodosPago(nombreMetodo=nombre)
        db.session.add(new_met)
        db.session.commit()
        
        return redirect(url_for('MetodosPago.index'))

    return render_template('MetodosPago/add.html')

@bp.route('/MetodosPago/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    met = MetodosPago.query.get_or_404(id)

    if request.method == 'POST': 
        met.nombreMetodo = request.form['nombre']
        db.session.commit()
        return redirect(url_for('MetodosPago.index'))

    return render_template('MetodosPago/edit.html', met=met)

@bp.route('/MetodosPago/delete/<int:id>')
@login_required
def delete(id): 
    
    meto = MetodosPago.query.get_or_404(id)
    
    db.session.delete(meto)
    db.session.commit()

    return redirect(url_for('MetodosPago.index'))



@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('Administrador.login'))