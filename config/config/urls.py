from django.contrib import admin; from django.urls import path, re_path, include
from django.http import HttpResponse
from django.views.static import serve
from django.conf import settings
from config.inline_content import I
def spa(r):
    return HttpResponse(I, content_type='text/html; charset=utf-8')
urlpatterns = [path('admin/',admin.site.urls), path('api/',include('main.urls'))]
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += [re_path(r'^(?P<path>favicon\.ico)$', serve, {'document_root': settings.FRONTEND_DIST_DIR})]
urlpatterns += [re_path(r'^(?P<path>logo\.png)$', serve, {'document_root': settings.FRONTEND_DIST_DIR})]
urlpatterns += [re_path(r'^carousel/(?P<path>.*)$', serve, {'document_root': settings.FRONTEND_DIST_DIR.parent / 'public' / 'carousel'})]
urlpatterns += [re_path(r'^products/(?P<path>.*)$', serve, {'document_root': settings.FRONTEND_DIST_DIR / 'products'})]
urlpatterns += [re_path(r'^assets/(?P<path>.*)$', serve, {'document_root': settings.FRONTEND_DIST_DIR / 'assets'})]
urlpatterns += [re_path(r'^(?!admin|api|static|assets|products|carousel|favicon|logo).*$', spa)]

