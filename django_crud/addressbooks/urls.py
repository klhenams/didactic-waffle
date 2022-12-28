from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from .views import ContactViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("contacts", ContactViewSet)

urlpatterns = router.urls
