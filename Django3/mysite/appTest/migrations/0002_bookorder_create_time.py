# Generated by Django 3.0.4 on 2020-03-22 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appTest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookorder',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]