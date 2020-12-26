from django.urls import path
from rest_framework import routers
from .views import RecipesViewSet

router = routers.DefaultRouter()
router.register('recipes', RecipesViewSet)

urlpatterns = router.urls