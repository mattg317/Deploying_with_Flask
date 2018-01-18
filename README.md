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

4. Go to (heroku)[https://www.heroku.com/].

  * Create a new app
  * From the **Deploy** tab, scroll down and link Github.
  * Click Deploy a GitHub branch.

### Setting environment variables for mySQL

1. In your code add the following code, replacing `mysql_connection` to any variable name you chose.

```python
import os
connection_var = os.environ.get("mysql_connection")
engine = create_engine(connection_var)
```
2. Back on Heroku go to settings  and click **Reveal Config Vars**.

3. Add the the variable string you made in step (so in this case `mysql_connection`) to the field on the left, and the your connect string to the field on the right. *Note* be sure no to add quotations.

4. Re-deploy app.

