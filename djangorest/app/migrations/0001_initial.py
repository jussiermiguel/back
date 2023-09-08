# Generated by Django 4.2.5 on 2023-09-07 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120)),
                ('done', models.BooleanField(default=False)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]