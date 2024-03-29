# Generated by Django 2.2.4 on 2019-08-17 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EscapeRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('passwordHash', models.CharField(max_length=255)),
                ('visited', models.ManyToManyField(to='application.EscapeRoom')),
            ],
        ),
        migrations.CreateModel(
            name='GoingOut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('decision', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.EscapeRoom')),
                ('participants', models.ManyToManyField(to='application.User')),
            ],
        ),
    ]
