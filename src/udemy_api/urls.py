from django.conf.urls import url, include

from rest_framework.authtoken import views as auth_views
from rest_framework.routers import DefaultRouter

from udemy_api.views import UserViewSet

router = DefaultRouter()
router.register('profile', UserViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^token/', auth_views.obtain_auth_token),
]