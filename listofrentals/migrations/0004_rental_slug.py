# Generated by Django 4.0.4 on 2022-12-09 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listofrentals', '0003_alter_rental_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='rental',
            name='slug',
            field=models.SlugField(default='djangodbmodelsfieldscharfield', max_length=30),
        ),
    ]
