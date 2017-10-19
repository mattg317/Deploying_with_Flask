# Deploy Flask Application

1. Create Repo

2. Add requirements.txt and make sure it includes:

  * gunicorn
  * mysqlclient
  * sqlalchemy
  * flask
  * numpy

3. Add Procfile

  * include `web: gunicorn app:app'
