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

**NOTE**
Django allauth actually forces the session expire setting depending on
if the user clicks 'Remember me'. The `ACCOUNT_SESSION_REMEMBER`
setting controls whether or not to allow this behavior.
