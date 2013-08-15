import os
basedir = os.path.abspath(os.path.dirname(__file__))

#SQLALCHEMY_DATABASE_URI = 'mysql://jj1192:9Hic*zUd@warehouse.cims.nyu.edu/jj1192_mick_nutri'
SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/nutri'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

#For forms
CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

RESULTS_PER_PAGE = 50

#For full-text search
#WHOOSH_BASE = os.path.join(basedir, 'search.db')
#MAX_SEARCH_RESULTS = 100