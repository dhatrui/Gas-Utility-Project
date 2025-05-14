from django.contrib import admin
from .models import ServiceRequest, RequestType

admin.site.register(ServiceRequest)
admin.site.register(RequestType)
