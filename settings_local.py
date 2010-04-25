# Django settings for local development environment of projectname project.

# Debugging output
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# For error emails
ADMINS = (
    ('Evan Culver', 'evan@evanculver.com'),
)

# For notification emails
MANAGERS = ADMINS

# Used for PayPal and in absolute URLs in JS
WEBSITE_DOMAIN = 'http://127.0.0.1:8000'

# Where to log on the local FS
LOGGING_FILENAME = '/Users/eculver/dev/testing/testing.log'