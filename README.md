# django-tutorial
My first Django app following the Django tutorial.

## Set up
For the first time, `django-tutorial-app-container` fails
because there's no database. After the failure, database is created.
So press Ctrl-C after the "PostgreSQL init process complete" message
and set up the containers one more time.

```sh
$ docker-compose build
$ docker-compose up

# press Ctrl-C after "PostgreSQL init process complete" message

$ docker-compose up
$ docker exec -it django-tutorial-app-container bash
# python manage.py migrate
# python manage.py loaddata polls/fixtures/dumpdata.json
# exit
```

## pages
### polls app
Access `localhost:8888/polls/`.

### admin page
Access `localhost:8888/admin/` and log in with `admin/password123`.
