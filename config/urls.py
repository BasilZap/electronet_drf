from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('electronet.urls', namespace='electronet')),
    path('users/', include('users.urls', namespace='users')),
]
