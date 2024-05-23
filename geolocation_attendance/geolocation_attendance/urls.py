from django.contrib import admin
from django.urls import path, include
from attendance.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('attendance/', include('attendance.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # Include authentication URLs
    path('', home, name='home'),  # Home view
]
