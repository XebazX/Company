from flask import Blueprint, render_template, request, redirect, url_for, render_template, redirect, url_for, request, flash
from app.models.Administrador import Administrador
# from app.models.Cliente import Cliente
from flask_login import login_user, current_user, logout_user, login_required
from flask_bcrypt import Bcrypt
from app import db


bp = Blueprint('Administrador', __name__)


@bp.route('/Administracion')
def index():
    data = Administrador.query.all()
    print("Data ", data)
    return render_template('Administrador/index.html', data=data)


@bp.route('/Admin/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        bcrypt = Bcrypt()
        Correo = request.form['correo']
        Contrasena = request.form['contrasena']
        hashed_password = bcrypt.generate_password_hash(Contrasena.encode('utf-8'))
        new_admin = Administrador(correoAdm=Correo, contrasenaAdm=hashed_password)
        print(new_admin)
        db.session.add(new_admin)
        db.session.commit()
        
        return redirect(url_for('Administrador.index'))

    return render_template('Administrador/add.html')

@bp.route('/Admin/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    admin = Administrador.query.get_or_404(id)

    if request.method == 'POST':
        admin.Correo = request.form['correo']
        admin.Contrasena = request.form['contrasena']
        db.session.commit()
        return redirect(url_for('Administrador.index'))

    return render_template('Administrador/edit.html', admin=admin)
    

@bp.route('/Admin/delete/<int:id>')
def delete(id):
    
    admin = Administrador.query.get_or_404(id)
    
    db.session.delete(admin)
    db.session.commit()

    return redirect(url_for('Administrador.index'))


@bp.route('/', methods=['GET', 'POST'])
def login():    
    global tipo
    
    
    if request.method == 'POST':
        bcrypt = Bcrypt()
        username = request.form['correo']
        password = request.form['password']
        
        # user = Cliente.query.filter_by(direccionCliente=username,contrasenaCliente=password).first()
        user = None
 
        if user :
            
            tipo = 0 
            login_user(user)
            flash("Login successful!", "success")
            return redirect(url_for('Productos.index'))
        
        else:
            user = Administrador.query.filter_by(correoAdm=username).first()
            if user:
                tipo = 1
                if bcrypt.check_password_hash(user.contrasenaAdm, password):
                    login_user(user)
                    flash("Login successful!", "success")
                    return redirect(url_for('Administrador.index'))
                
    return render_template("/Administrador/login.html")


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('Administrador.login'))


