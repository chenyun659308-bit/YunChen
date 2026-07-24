from wsgiref.simple_server import make_server
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'
import django; django.setup()
from django.core.wsgi import get_wsgi_application
app = get_wsgi_application()
print("WSGI server on :5173")
make_server("0.0.0.0", 5173, app).serve_forever()