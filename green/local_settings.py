USER = "root"
NAME = "Alindb"
PASSWORD = ""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': NAME,
        'USER': USER,
        'PASSWORD': PASSWORD,
        'HOST': 'localhost',
        'PORT': '3306',
    }
}