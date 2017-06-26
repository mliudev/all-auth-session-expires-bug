# expire-on-browser-close

Demo project to show that the `SESSION_EXPIRE_AT_BROWSER_CLOSE` setting is not
respected.

# how to test

Quick setup:

```
python manage.py migrate
python manage.py createsuperuser

python manage.py runserver
```

Navigate to `localhost:8000` and login. You should see a page showing
your session id as well as whether the session will expire once the
browser closes.

Next modify the `SESSION_EXPIRE_AT_BROWSER_CLOSE` setting in the
settings.py file. Notice that the setting is not respected after you
logout and back in.
