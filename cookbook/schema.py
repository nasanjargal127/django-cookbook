import graphene
from graphene_django import DjangoObjectType

from cookbook.ingredients.models import Category, Ingredient
from cookbook.users.models import User


class UserType(DjangoObjectType):
    class Meta: 
        model = User
        fields = ("id", "name", "email")        

class CategoryType(DjangoObjectType):
    class Meta: 
        model = Category
        fields = ("id", "name", "ingredients")

class IngredientsType(DjangoObjectType):
    class Meta: 
        model = Ingredient
        fields = ("id", "name", "category")

class Query(graphene.ObjectType):
    all_ingredients = graphene.List(IngredientsType)
    users = graphene.List(UserType)
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))

    def resolve_all_ingredients(root, info):
        return Ingredient.objects.select_related("category").all()
    
    def resolve_users(root, info):
            return User.objects.all() 
    
    def resolve_category_by_name(root, info, name): 
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None
        
schema = graphene.Schema(query=Query)