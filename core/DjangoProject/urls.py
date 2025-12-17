from django.contrib import admin
from django.urls import path
from django.conf import settings

# print(settings.SECRET_KEY)
print(settings.DEBUG)


urlpatterns = [
    path('admin/', admin.site.urls),
]
