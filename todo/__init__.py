from flask import Flask 
import os


def create_app():
   app = Flask(__name__)

   # (1)
   app.config.from_mapping( 
      SECRET_KEY='mikey',
      DATABASE_HOST=os.environ.get('FLASK_DATABASE_HOST'),
      DATABASE_PASSWORD=os.environ.get('FLASK_DATABASE_PASSWORD'),
      DATABASE_USER=os.environ.get('FLASK_DATABASE_USER'),
      DATABASE=os.environ.get('FLASK_DATABASE')
   )

   # print(app.config)

   from . import db # de esta forma nos traemos el archivo completo

   db.init_app(app)

   from . import auth

   app.register_blueprint(auth.bp)

   @app.route('/hola')
   def hola():
      return 'Hola que tal'
   
   return app



# (1)
# from_mapping nos va a permitir definir variables de configuracion que despues 
# podremos usar en nuestra aplicacion
# (2) # export FLASK_APP=todo nos permitira correr la aplicacion.
