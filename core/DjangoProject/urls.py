import logging

from django.contrib import admin
from django.urls import path

logger = logging.getLogger(__name__)
logger.debug("This is a debug message")
logger.info("This is a info message")

urlpatterns = [
    path("admin/", admin.site.urls),
]
