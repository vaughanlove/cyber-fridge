from .models import Recipe
from rest_framework.viewsets import ModelViewSet
from .serializer import RecipeSerializer
# Create your views here.

class RecipesViewSet(ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

