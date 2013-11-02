from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'nuevoAutor/$', 'pendientes.views.nuevoAutor', name='nuevoAutor'),
    
)