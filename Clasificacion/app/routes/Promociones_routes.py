from flask import Blueprint, render_template, request, redirect, url_for, render_template, redirect, url_for, request, flash
from app.models.Promotor import Promotor
from app.models.Promociones  import Promociones
from flask_login import login_user, current_user, logout_user, login_required
from flask_bcrypt import Bcrypt
from app import db


bp = Blueprint('Promociones', __name__)


@bp.route('/Promociones')
@login_required
def index():
    data = Promociones.query.all()
    print("Data ", data)
    return render_template('Promociones/index.html', data=data)


@bp.route('/Promociones/add', methods=['GET', 'POST'])
@login_required
def add():
    if request.method == 'POST':
        nombre = request.form['nombre']

        new_prom = Promociones(nombrePromocion=nombre) 
        db.session.add(new_prom)
        db.session.commit()
        
        return redirect(url_for('Promociones.index'))

    return render_template('Promociones/add.html')

@bp.route('/Promociones/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    prom = Promociones.query.get_or_404(id)

    if request.method == 'POST': 
        prom.nombrePromocion = request.form['nombre']
        db.session.commit()
        return redirect(url_for('Promociones.index'))

    return render_template('Promociones/edit.html', prom=prom)

@bp.route('/Promociones/delete/<int:id>')
@login_required
def delete(id): 
    
    prom = Promociones.query.get_or_404(id)
    
    db.session.delete(prom)
    db.session.commit()

    return redirect(url_for('Promociones.index'))



@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('Administrador.login'))