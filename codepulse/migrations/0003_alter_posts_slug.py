# Generated by Django 4.2.4 on 2023-08-05 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codepulse', '0002_alter_posts_options_alter_posts_thead0'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='slug',
            field=models.SlugField(max_length=30, unique=True),
        ),
    ]
