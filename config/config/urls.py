from django.contrib import admin; from django.urls import path, re_path, include
from django.views.static import serve
from django.conf import settings
def spa(request):
    import os
    index_path = os.path.join(settings.FRONTEND_DIST_DIR, 'index.html')
    if os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
    else:
        content = '<html><body><h1>Frontend not built</h1><p>Run: cd frontend && npm run build</p></body></html>'
    from django.http import HttpResponse
    return HttpResponse(content, content_type='text/html; charset=utf-8')
urlpatterns = [path('admin/',admin.site.urls), path('api/',include('main.urls'))]
from django.conf.urls.static import static
urlpatterns += [re_path(r"^static/(?P<path>.+)$", serve, {"document_root": settings.STATIC_ROOT})]
urlpatterns += [re_path(r'^(?P<path>favicon\.ico)$', serve, {'document_root': settings.FRONTEND_DIST_DIR})]
urlpatterns += [re_path(r'^(?P<path>logo\.png)$', serve, {'document_root': settings.FRONTEND_DIST_DIR})]
urlpatterns += [re_path(r'^assets/(?P<path>.+)$', serve, {'document_root': settings.FRONTEND_DIST_DIR / 'assets'})]
urlpatterns += [re_path(r'^products/(?P<path>.+)$', serve, {'document_root': settings.FRONTEND_DIST_DIR / 'products'})]
urlpatterns += [re_path(r'^downloads/(?P<path>.+)$', serve, {'document_root': settings.FRONTEND_DIST_DIR / 'downloads'})]
urlpatterns += [re_path(r'^carousel/(?P<path>.+)$', serve, {'document_root': settings.FRONTEND_DIST_DIR.parent / 'public' / 'carousel'})]
urlpatterns += [re_path(r'^(?!admin|api|static|assets|favicon|logo).*$', spa)]
