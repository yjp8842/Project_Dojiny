# Generated by Django 3.2.13 on 2022-11-18 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('behinds', '0005_behind_like_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(),
        ),
    ]
