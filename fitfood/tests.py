from django.test import TestCase
from .models import Category, Ingredient, Recipe, NutritionInfo, Comment
from django.contrib.auth.models import User

class RecipeModelTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')
        self.ingredient = Ingredient.objects.create(name='Test Ingredient')
        self.user = User.objects.create(username='testuser', password='testpassword')
        self.recipe = Recipe.objects.create(
            title='Test Recipe',
            category=self.category,
            describe='Test description',
            instructions='Test instructions',
        )
        self.recipe.ingredients.add(self.ingredient)
        self.nutrition_info = NutritionInfo.objects.create(
            recipe=self.recipe,
            calories=100,
            protein=10,
            carbs=20,
            fat=5,
        )
        self.comment = Comment.objects.create(
            user=self.user,
            recipe=self.recipe,
            text='Test comment text',
        )

    def test_recipe_model(self):
        self.assertEqual(self.recipe.title, 'Test Recipe')
        self.assertEqual(self.recipe.category, self.category)
        self.assertEqual(self.recipe.ingredients.count(), 1)
        self.assertEqual(self.recipe.nutritioninfo.calories, 100)
        self.assertEqual(self.recipe.comments.count(), 1)

    def test_comment_model(self):
        self.assertEqual(self.comment.user, self.user)
        self.assertEqual(self.comment.recipe, self.recipe)
        self.assertEqual(self.comment.text, 'Test comment text')
