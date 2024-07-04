from flask import Blueprint, render_template, request, redirect, url_for, render_template, redirect, url_for, request, flash
from app.models.Varios import Varios
from app.models import Promotor
from flask_login import login_user, current_user, logout_user, login_required
from flask_bcrypt import Bcrypt
from app import db


bp = Blueprint('Varios', __name__)


@bp.route('/Varios')
def index():
    data = Varios.query.all()
    print("Data ", data)
    return render_template('Varios/index.html', data=data)


@bp.route('/Varios/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        bcrypt = Bcrypt()
        nombre = request.form['nombre']
        cantidad = request.form['cantidad']
       
        new_var = Varios(nombreVarios=nombre, cantidadVarios=cantidad )
        print(new_var)
        db.session.add(new_var)
        db.session.commit()
        
        return redirect(url_for('Varios.index'))

    return render_template('Varios/add.html')

@bp.route('/Varios/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    var = Varios.query.get_or_404(id)

    if request.method == 'POST':
        var.nombreVarios= request.form['nombre']
        var.cantidadVarios = request.form['cantidad']
       
        db.session.commit()
        return redirect(url_for('Varios.index')) 

    return render_template('Varios/edit.html', var=var)

@bp.route('/Varios/delete/<int:id>')
def delete(id):
    
    admin = Varios.query.get_or_404(id)
    
    db.session.delete(admin)
    db.session.commit()

    return redirect(url_for('Varios.index'))



@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('Administrador.login'))