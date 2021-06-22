
SECRET_KEY = 'django-insecure-bzzz2^l^u+6d(=rwqka3gz*#a3)6$lc^-7cewi*ps-&pto-_l&'
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
DEBUG = True

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_ROOT = BASE_DIR / 'media'
STATIC_ROOT = '/home/ik1007/static'

# ALLOWED_HOSTS = ['ik1007.pythonanywhere.com']  # для сервера
# MEDIA_URL = '/media/' 
# MEDIA_ROOT = '/home/ik1007/media'        # коментировать при разраб