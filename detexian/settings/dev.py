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
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(PROJECT_ROOT, 'run', 'dev.sqlite3'),
    }
}

# ##### APPLICATION CONFIGURATION #########################

INSTALLED_APPS = DEFAULT_APPS + \
					[
					'allauth',
				    'allauth.account',
				    'allauth.socialaccount',
                    'alerts',
                    #'user_profile',
                    'rest_framework'
                    ]

# Django-allAuth Configuration
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False

LOGIN_URL='/accounts/login/'
LOGIN_REDIRECT_URL='/'