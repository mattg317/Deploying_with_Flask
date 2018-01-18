# Deploy Flask Application

1. Create Repo

2. Write Python code in `app.py`. **Note** this can be named anything you want, just make to adjust the Procfile accordingly if another name is used.

3. Add requirements.txt and make sure it includes:

  * gunicorn
  * mysqlclient
  * sqlalchemy
  * flask
  * numpy

4. Add Procfile

  * include `web: gunicorn app:app'

5. Go to (heroku)[https://www.heroku.com/].

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
2. Back on Heroku, navigate to settings tab, scroll down and click **Reveal Config Vars**.

3. Add the variable string used in step 1 (so in this case `mysql_connection`) to the field on the left, and the connection string to the field on the right. *Note* be sure not to add quotations.

