# Generated by Django 2.2.4 on 2019-08-24 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_auto_20190819_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='buddies',
            field=models.ManyToManyField(related_name='_user_buddies_+', to='application.User'),
        ),
    ]