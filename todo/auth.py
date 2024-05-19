import functools

from flask import (
   Blueprint, flash, g, render_template, request, url_for, session, redirect
)

from werkzeug.security import check_password_hash, generate_password_hash

from todo.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['GET','POST'])
def register():
   if request.method == 'POST':
      username = request.form['username']
      password = request.form['password']
      db, c = get_db()
      error = None
      c.execute(
         'select id from user where username = %s',(username,)
      )
      if not username:
         error = 'Username es requerido'
      if not password:
         error = 'Password es requerido'
      elif c.fetchone() is not None:
         error = 'Usuario {} se encuentra registrado.'.format(username)
      
      if error is None:
         c.execute(
            'insert into user (username, password) values (%s, %s)',
            (username, generate_password_hash(password))
         )
         db.commit()

         return redirect(url_for('auth.login'))
      
      flash(error)

   return render_template('auth/register.html')

@bp.route('/login', methods=['GET','POST'])
def login():
   if request.method == 'POST': # si esto se cumple, es porque el usuario esta intentando iniciar sesion.
      username = request.form['username']
      password = request.form['password']
      db, c = get_db()
      error = None
      c.execute(
         'select * from user where username = %s', (username,)
      )
      user = c.fetchone()

      if user is None:
         error = 'Usuario y o contrasena invalida'
      elif not check_password_hash(user['password'], password):
         error = 'Usuario y o contrasena invalida'

      if error is None:
         session.clear()
         session['user_id'] = user['id']
         return redirect(url_for('index'))
      
      flash(error)

   return render_template('auth/login.html')











#- flash
# Nos va a permitir enviar mensajes de manera generica a nuestras plantillas.
#- render_template
# Para renderizar plantillas
#- request
# Para recibir datos de un formulario
#- url_for
# Para crear url's
#- session
# Para poder mantener una referencia del usuario que se encuentra en el contexto actual
# interactuando con nuestra aplicacion de Flask.
#- url_prefix=
# A todas las url's que se encuentran debajo, les va a colocar la url que nosotros
# le indicaremos en el string. Por ejemplo url_prefix='/auth'