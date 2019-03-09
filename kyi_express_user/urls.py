
from . import views

from rest_framework.routers import DefaultRouter
from django.urls import path, include



router = DefaultRouter()
router.register(r'keusers', views.Kyi_Express_User_ViewSet)

urlpatterns = [
    path('', include(router.urls)),
]