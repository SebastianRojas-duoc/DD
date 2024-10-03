from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index,name="index"),
    path('noti', noti,name="noti"),
    path('add_noti', add_noti,name="add_noti"),
	path('nuevo',nuevo,name='nuevo'),
    path('regi', regi,name="regi"),
	path('login/', logins,name="login"),
    path('detalle_noti/<int:noticia_id>/', detalle_noti,name="detalle_noti"),
    path('detalle_noti1', detalle_noti1,name="detalle_noti1"),
    path('detalle_noti2', detalle_noti2,name="detalle_noti2"),
    path('detalle_noti3', detalle_noti3,name="detalle_noti3"),
	path('comen',comen,name='comen'),
	path('usuario',usuario,name='usuario'),
	path('mod_usuario',mod_usuario,name="mod_usuario"),
	path('list_usuario',list_usuario,name="list_usuario"),
	path('list_noti',list_noti,name="list_noti"),
	path('mod_noti/<int:noti_id>/',mod_noti,name="mod_noti"),
	path('eliminar_usuario/', eliminar_usuario, name='eliminar_usuario'),
	path('eliminar_noti/<int:noticia_id>/', eliminar_noti, name='eliminar_noti'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
