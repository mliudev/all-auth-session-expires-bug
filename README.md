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

Navigate to localhost:8000 and login with your created superuser.
You should see the session key, whether the key expires on browser
close, and when the expiration date is if it does.

You can modify the `SESSION_EXPIRES_AT_BROWSER_CLOSE` setting in
settings.py to verify that this setting is respected.
