from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
#endpoint, view
router.register("cards", views.CardView)

urlpatterns = [
    path("",include(router.urls))
]
