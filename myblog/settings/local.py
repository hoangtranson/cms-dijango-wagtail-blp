SECRET_KEY = 'lpt!ja!7y&wl#y-u$en&2h11b1#5gaxz=^t#8z&&j16+g^5qv='
ALLOWED_HOSTS = ['transonhoang.pythonanywhere.com']

STATIC_ROOT = '/home/transonhoang/cms-dijango-wagtail-blp/mysite/static'
MEDIA_ROOT = '/home/transonhoang/cms-dijango-wagtail-blp/media'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # do not change it
        'NAME': 'transonhoang$default',  # add database_name
        'USER' : 'transonhoang',  # add user_name
        'PASSWORD' : 'hoang123456789',  # add password_here
        'HOST' : 'transonhoang.mysql.pythonanywhere-services.com', # add host_name
        'PORT' : '', # leave blank
    }
}