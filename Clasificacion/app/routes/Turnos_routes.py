from flask import Blueprint, render_template, request, redirect, url_for, render_template, redirect, url_for, request, flash
from app.models.Turnos import Turnos
from app.models import Promotor
from flask_login import login_user, current_user, logout_user, login_required
from flask_bcrypt import Bcrypt
from app import db


bp = Blueprint('Turnos', __name__)


@bp.route('/Turnos')
@login_required
def index():
    data = Turnos.query.all()
    print("Data ", data)
    return render_template('Turnos/index.html', data=data)


@bp.route('/Turnos/add', methods=['GET', 'POST'])
@login_required
def add():
    if request.method == 'POST':
        turno = request.form['turno']
        new_turn = Turnos(numeroTur=turno) 
        db.session.add(new_turn)
        db.session.commit()
        
        return redirect(url_for('Turnos.index'))

    return render_template('Turnos/add.html')

@bp.route('/Turnos/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    turn = Turnos.query.get_or_404(id)

    if request.method == 'POST': 
        turn.numeroTur = request.form['nombre']
        db.session.commit()
        return redirect(url_for('Turnos.index'))

    return render_template('Turnos/edit.html', turn=turn)

@bp.route('/Turnos/delete/<int:id>')
@login_required
def delete(id): 
    
    turn = Turnos.query.get_or_404(id)
    
    db.session.delete(turn)
    db.session.commit()

    return redirect(url_for('Turnos.index'))



@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('Administrador.login'))