from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('chemia_main.urls')),
    path('admin/', admin.site.urls),
]
