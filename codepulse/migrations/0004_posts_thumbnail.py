# Generated by Django 4.2.4 on 2023-08-05 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codepulse', '0003_alter_posts_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='home/thumbnail'),
        ),
    ]