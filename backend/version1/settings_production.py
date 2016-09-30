from settings import *


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3TEST'),
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Magnet',
        'USER': 'root',
        'PASSWORD': '09231314pl',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
