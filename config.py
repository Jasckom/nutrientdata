import os
basedir = os.path.abspath(os.path.dirname(__file__))

#SQLALCHEMY_DATABASE_URI = 'mysql://jj1192:9Hic*zUd@warehouse.cims.nyu.edu/jj1192_mick_nutri'
#SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/nutri'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

if os.environ.get('DATABASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/nutri'
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

DEBUG = True

#For forms
CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

RESULTS_PER_PAGE = 50
