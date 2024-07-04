from flask import Blueprint, render_template, request, redirect, url_for, render_template, redirect, url_for, request, flash
from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models.Promotor import Promotor
from app.models.MetodosPago import MetodosPago
from flask_login import login_user, current_user, logout_user, login_required
from flask_bcrypt import Bcrypt

bp = Blueprint('Promotores', __name__)

@bp.route('/Promotores')
def index():
    data = Promotor.query.all()
    return render_template('Promotores/index.html', data=data)
 
#mamahuevo estais ahi?
@bp.route('/Promotores/add', methods=['GET', 'POST']) 
@login_required
def add():
    if request.method == 'POST':
        nombre = request.form['nombre']
        celular = request.form['celular'] 
        correo = request.form['correo']
        documento = request.form['documento']
        contrasena = request.form['contrasena'] 
        
        NPromotor = Promotor(nombrePro=nombre, numeroPro=celular, correoPro=correo, documentoPro=documento, contrasenaPro=contrasena)
        db.session.add(NPromotor)
        db.session.commit()
        
        return redirect(url_for('Administrador.Admpromotor'))

    return render_template('Administrador/promotor.html')


@bp.route('/Promotores/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        celular = request.form['celular'] 
        correo = request.form['correo']
        documento = request.form['documento']
        contrasena = request.form['contrasena']
        
        #En teoria el celular y documento debeían ser string por que no planea hacer operaciones con ellos, ahora el celular es str y la columna es int, no se si eso genera un error. ya 
        print(type(celular)) #<- aqui es tipo string
        
        # No se si funcione -> convertir el celular a int try
        
        #como seria convertirlo
        
        celular = int(celular) #<- like this, repito no se si funciona intentemosle po
        
        NPromotor = Promotor(nombrePro=nombre, numeroPro=celular, correoPro=correo, documentoPro=documento, contrasenaPro=contrasena)
        db.session.add(NPromotor)
        db.session.commit()
        
    
        
       #vamono pibeeeeeeeeeeeeeeeee vamo
        return redirect(url_for('Administrador.login'))

    return render_template('Promotores/registro.html')

@bp.route('/Promotores/edit/<int:id>', methods=['GET', 'POST']) # coño la ptm with you why here usted debe utilizar el nombre de las columas que está en la base de datos coño 
@login_required
def edit(id):
    pro = Promotor.query.get_or_404(id)

    if request.method == 'POST': 
        pro.nombrePro = request.form['nombre']
        pro.documento = request.form['documento']
        pro.correo = request.form['correo']
        pro.numero = request.form['numero']
        db.session.commit()
        return redirect(url_for('Promotores.index'))

    return render_template('Promotores/edit.html', pro=pro)
    

@bp.route('/Promotores/delete/<int:id>')
@login_required
def delete(id):
    promoto = Promotor.query.get_or_404(id)
    
    db.session.delete(promoto)
    db.session.commit()

    return redirect(url_for('Administrador.Admpromotor'))


#<a href="{{ url_for('Promotores.delete', id=Promotor.idPromotor) }}" class="btn btn-danger">Eliminar</a> , el eliminar del promotor