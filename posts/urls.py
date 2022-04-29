from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import PostViewSet, UserViewSet

router = SimpleRouter()
router.register('users', UserViewSet)
router.register('', PostViewSet)



urlpatterns = router.urls

