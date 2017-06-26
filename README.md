# expire-on-browser-close

Demo project to show that the `SESSION_EXPIRE_AT_BROWSER_CLOSE` setting is not
respected.

# how to test

First checkout `base-django` and follow the readme instructions there
in order to verify the behavior of a base django installation with
respect to session cookie handling.

Then checkout `all-auth` and follow the readme instructions there to
see that django-allauth ignores the `SESSION_EXPIRE_AT_BROWSER_CLOSE`
setting.
