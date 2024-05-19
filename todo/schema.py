instructions = [
   'SET FOREIGN_KEY_CHECKS=0;',
   'DROP TABLE IF EXISTS todo;',
   'DROP TABLE IF EXISTS user;',
   'SET FOREIGN_KEY_CHECKS=1;', # volvemos a activar nuestra validacion de llaves foraneas.
   """
      CREATE TABLE user (
         id INT PRIMARY KEY AUTO_INCREMENT,
         username VARCHAR(50) UNIQUE NOT NULL,
         password VARCHAR(255) NOT NULL
      )
   """,
   """
      CREATE TABLE todo (
      id INT PRIMARY KEY AUTO_INCREMENT,
      created_by INT NOT NULL,
      created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
      description TEXT NOT NULL,
      completed BOOLEAN NOT NULL,
      FOREIGN KEY (created_by) REFERENCES user (id)
      );
   """
]


#- id INT PRIMARY KEY AUTO_ICREMENT
# cada vez ingresemos un valor se le asignara un valor automaticamente y el valor 
# sera siempre un numero despues.

#- created_at
# mysql se encargara de asignarle un valor por defecto, que sera la fecha actual que tenga el servidor de mysql
