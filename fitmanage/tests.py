
from django.test import TestCase
from .models import Type, Trainer, AddMember, WeeklyReport


class ModelTests(TestCase):

    def test_type_model(self):
        type_obj = Type.objects.create(title='Test Type', price=10.99, type_details='Test details')
        self.assertEqual(type_obj.title, 'Test Type')
        self.assertEqual(type_obj.price, 10.99)
        self.assertEqual(type_obj.type_details, 'Test details')

    def test_trainer_model(self):
        trainer_obj = Trainer.objects.create(name='Test Trainer', stars=4.5)
        self.assertEqual(trainer_obj.name, 'Test Trainer')
        self.assertEqual(trainer_obj.stars, 4.5)

    def test_add_member_model(self):
        type_obj = Type.objects.create(title='Test Type', price=10.99)
        trainer_obj = Trainer.objects.create(name='Test Trainer', stars=4.5)

        member_obj = AddMember.objects.create(
            first_name='John',
            last_name='Doe',
            date_of_birth='1990-01-01',
            start='2023-01-01',
            end='2023-12-31',
            phone_number='1234567890',
            address='123 Main St',
            type=type_obj,
            amount=99.99,
            trainers=trainer_obj,
            payment_status=True,
        )

        self.assertEqual(member_obj.first_name, 'John')
        self.assertEqual(member_obj.last_name, 'Doe')
        self.assertEqual(str(member_obj.date_of_birth), '1990-01-01')
        self.assertEqual(str(member_obj.start), '2023-01-01')
        self.assertEqual(str(member_obj.end), '2023-12-31')
        self.assertEqual(member_obj.phone_number, '1234567890')
        self.assertEqual(member_obj.address, '123 Main St')
        self.assertEqual(member_obj.type, type_obj)
        self.assertEqual(member_obj.amount, 99.99)
        self.assertEqual(member_obj.trainers, trainer_obj)
        self.assertTrue(member_obj.payment_status)

    def test_weekly_report_model(self):
        report_obj = WeeklyReport.objects.create(title='Test Report', content='Test content')
        self.assertEqual(report_obj.title, 'Test Report')
        self.assertEqual(report_obj.content, 'Test content')





        