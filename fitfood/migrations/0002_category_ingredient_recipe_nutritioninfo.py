# Generated by Django 4.2.5 on 2023-09-14 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fitfood', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('instructions', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('average_rating', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
                ('total_ratings', models.PositiveIntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fitfood.category')),
                ('ingredients', models.ManyToManyField(to='fitfood.ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='NutritionInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calories', models.DecimalField(decimal_places=2, max_digits=6)),
                ('protein', models.DecimalField(decimal_places=2, max_digits=6)),
                ('carbs', models.DecimalField(decimal_places=2, max_digits=6)),
                ('fat', models.DecimalField(decimal_places=2, max_digits=6)),
                ('recipe', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='fitfood.recipe')),
            ],
        ),
    ]
