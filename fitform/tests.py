from django.test import TestCase
from .models import WorkoutCategory, Exercise, Fitness, UserQuery
from django.contrib.auth.models import User


class FitnessModelsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            email='test@example.com'
        )
        self.category = WorkoutCategory.objects.create(
            name='Test Category',
            image='test_image.png'
        )
        self.exercise = Exercise.objects.create(
            name='Test Exercise',
            category=self.category,
            description='Test description',
            image='exercise_image.png'
        )
        self.fitness = Fitness.objects.create(
            title='Test Fitness',
            description='Test description',
            image='fitness_image.png'
        )
        self.user_query = UserQuery.objects.create(
            user=self.user,
            subject='Test Query',
            message='Test message'
        )

    def test_workout_category_model(self):
        self.assertEqual(self.category.name, 'Test Category')
        self.assertEqual(str(self.category), 'Test Category')

    def test_exercise_model(self):
        self.assertEqual(self.exercise.name, 'Test Exercise')
        self.assertEqual(self.exercise.category, self.category)
        self.assertEqual(str(self.exercise), 'Test Exercise')

    def test_fitness_model(self):
        self.assertEqual(self.fitness.title, 'Test Fitness')
        self.assertEqual(str(self.fitness), 'Test Fitness')

    def test_user_query_model(self):
        self.assertEqual(self.user_query.subject, 'Test Query')
        self.assertEqual(self.user_query.user, self.user)
        self.assertEqual(str(self.user_query), 'Test Query - testuser')
