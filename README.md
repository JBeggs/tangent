# tangent
Starting of test

Installation
------------
Ubuntu 16.04 running...



* Create Virtual Env
`virtualenv env`

* Activate env
`source env/bin/activate`

* Use pip to install Django
`pip install -r requirements.pip`

* Change directory
`cd tangent`

* Make Migration the database
`python manage.py makemigration`

* Migrate the database
`python manage.py migrate`

* You might need to clear the migrations already made
`rm review/migrations/00*`

* Collect static Files
`python manage.py collectstatic`

* Run the server
`python manage.py runserver`

* Go to http://localhost:8000
