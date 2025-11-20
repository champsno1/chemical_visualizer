
SECRET_KEY='dev'
INSTALLED_APPS = ['django.contrib.contenttypes','django.contrib.auth','rest_framework','datasets']
ROOT_URLCONF='pipeline_visualizer.urls'
DEBUG=True
ALLOWED_HOSTS=['*']
import os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT=os.path.join(BASE_DIR,'media')
MEDIA_URL='/media/'
REST_FRAMEWORK={'DEFAULT_AUTHENTICATION_CLASSES':['rest_framework.authentication.SessionAuthentication']}
