# Import some utility functions
from os.path import join
# Fetch our common settings
from common import *

# #########################################################

# ##### DEBUG CONFIGURATION ###############################
DEBUG = True


# ##### DATABASE CONFIGURATION ############################
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'detexian',
        'USER': 'detexian',
        'PASSWORD': 'detexian',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# ##### APPLICATION CONFIGURATION #########################

INSTALLED_APPS = DEFAULT_APPS + \
					[
					'allauth',
				    'allauth.account',
				    'allauth.socialaccount',
                    'alerts',
                    'dashboard',
                    'hosts',
                    'rest_framework'
                    ]

# Django-allAuth Configuration
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False

LOGIN_URL='/accounts/login/'
LOGIN_REDIRECT_URL='/'