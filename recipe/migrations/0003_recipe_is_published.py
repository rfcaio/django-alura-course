# Generated by Django 2.2.10 on 2020-04-22 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_recipe_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]