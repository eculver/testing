# Django settings for production environment of projectname project.

# Debugging output
DEBUG = False
TEMPLATE_DEBUG = DEBUG

# For error emails
ADMINS = (
    ('Evan Culver', 'evan@evanculver.com'),
)

# For notification emails
MANAGERS = (
    ('Evan Culver', 'evan@evanculver.com'),
    # Add client emails here
)

# Used for PayPal and in absolute URLs in JS
WEBSITE_DOMAIN = 'http://www.testing.com'

# Where to log on the local FS
LOGGING_FILENAME = '/var/log/testing/testing.log'