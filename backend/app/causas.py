from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required
from .models import db, Causa, Victima, Agresor
from .forms import CausaForm

causas_bp = Blueprint('causas', __name__)

@causas_bp.route('/causas', methods=['GET'])
@login_required
def index():
    causas = Causa.query.all()
    return render_template('causas/index.html', causas=causas)

@causas_bp.route('/causas/create', methods=['GET', 'POST'])
@login_required
def create():
    form = CausaForm()
    if form.validate_on_submit():
        victima = Victima.query.filter_by(dni=form.victima_dni.data).first()
        if not victima:
            victima = Victima(nombre=form.victima_nombre.data, apellido=form.victima_apellido.data, dni=form.victima_dni.data)
            db.session.add(victima)

        agresor = Agresor.query.filter_by(dni=form.agresor_dni.data).first()
        if not agresor:
            agresor = Agresor(nombre=form.agresor_nombre.data, apellido=form.agresor_apellido.data, dni=form.agresor_dni.data)
            db.session.add(agresor)
        else:
            agresor.reincidente = True
            flash('¡Alerta! El agresor es reincidente.', 'warning')

        causa = Causa(numero_causa=form.numero_causa.data, tipo_causa=form.tipo_causa.data, victima=victima, agresor=agresor)
        db.session.add(causa)
        db.session.commit()
        flash('Causa creada exitosamente.')
        return redirect(url_for('causas.index'))
    return render_template('causas/create.html', form=form)
