# Bill generation grms

This is a website built using DJANGO framework.

Who can access?
  
  
    -ADMIN(superuser)
    -USER(one who need to register ONSITE)
 
 
 
ADMIN 
    
     "http://127.0.0.1:8000/admin/" is uses to access the interface.
     
     
SOFTWARE REQUIREMENTS:

    Virtual environment with
      -DJANGO 2.0+ 
      -PYTHON 3.0+
    MYSQL(mysqlclient,mysqlserver)
 
COMMANDS REQUIRED before execution

    -for database
      $python manage.py makemigrations
      $python manage.py migrate
    -for staticfiles
      $python manage.py collectstatic
