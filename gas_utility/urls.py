from django.contrib import admin
from django.urls import path, include
from service_requests.views import home 

urlpatterns = [
    path('', home),  # <-- Add this
    path('admin/', admin.site.urls),
    path('requests/', include('service_requests.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
