from flask import Blueprint, render_template, request, redirect, url_for, render_template, redirect, url_for, request, flash
from app.models.Liquidos import Liquidos
from app.models import Promotor
from flask_login import login_user, current_user, logout_user, login_required
from flask_bcrypt import Bcrypt
from app import db


bp = Blueprint('Liquidos', __name__)


@bp.route('/Planilla')
def index():
    data = Liquidos.query.all()
    print("Data ", data)
    return render_template('Administrador/index.html', data=data)


@bp.route('/Planilla/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        bcrypt = Bcrypt()
        nombre = request.form['nombre']
        numero = request.form['numero']
        Correo = request.form['correo']
        documento = request.form['documento']
        Contrasena = request.form['contrasena']
        hashed_password = bcrypt.generate_password_hash(Contrasena.encode('utf-8'))
        new_liq = Liquidos(nombreAdm=nombre,numeroAdm=numero,correoAdm=Correo, documentoAdm=documento,contrasenaAdm=hashed_password)
        print(new_liq)
        db.session.add(new_liq)
        db.session.commit()
        
        return redirect(url_for('Administrador.index'))

    return render_template('Administrador/add.html')

@bp.route('/Planilla/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    liq = Liquidos.query.get_or_404(id)

    if request.method == 'POST':
        liq.idLiquidos = request.form['correo']
        liq.nombreLiquido = request.form['nombre']
        liq.cantidadLiquido = request.form['numero']
        liq.precioLiquido = request.form['documento']
        liq.Contrasena = request.form['contrasena']
        liq.Contrasena = request.form['contrasena']
        liq.Contrasena = request.form['contrasena']
        liq.Contrasena = request.form['contrasena']
        liq.Contrasena = request.form['contrasena']
        liq.Contrasena = request.form['contrasena']
        liq.Contrasena = request.form['contrasena']
        liq.Contrasena = request.form['contrasena']
        liq.Contrasena = request.form['contrasena']
        liq.Contrasena = request.form['contrasena']
        liq.Contrasena = request.form['contrasena']
        liq.Contrasena = request.form['contrasena']
        liq.Contrasena = request.form['contrasena']
        liq.Contrasena = request.form['contrasena']
        liq.Contrasena = request.form['contrasena']
        liq.Contrasena = request.form['contrasena']
        liq.Contrasena = request.form['contrasena']
        db.session.commit()
        return redirect(url_for('Administrador.index'))

    return render_template('Administrador/edit.html',)

@bp.route('/Admin/delete/<int:id>')
def delete(id):
    
    admin = Liquidos.query.get_or_404(id)
    
    db.session.delete(admin)
    db.session.commit()

    return redirect(url_for('Administrador.index'))



@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('Administrador.login'))