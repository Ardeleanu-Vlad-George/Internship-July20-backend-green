USER = "root"
NAME = "AlinDB"
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