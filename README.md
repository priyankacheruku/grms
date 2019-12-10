# Bill generation grms

This is a website built using DJANGO framework for bill generation of groceries

Who can access?

    -ADMIN(superuser)
    -USER(one who need to register ONSITE)
    
    ADMIN can "http://127.0.0.1:8000/admin/" use to access the interface.
    User can "http://127.0.0.1:8000/" use to access the interface.
 
INSTALLATIONSOFTWARE REQUIREMENTS:

    Virtual environment with

      -DJANGO 2.0+ 
      -PYTHON 3.0+
      -MYSQL(mysqlclient,mysqlserver)

COMMANDS REQUIRED before execution

    -for database
        $python manage.py makemigrations
        $python manage.py migrate
    -for staticfiles
        $python manage.py collectstatic
    -for mail
       change examplemail and password
