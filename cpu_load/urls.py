from django.contrib import admin
from django.urls import path, include
from catcher.views import table

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', table, name='table'),
    path('api/', include('catcher.urls')),
]