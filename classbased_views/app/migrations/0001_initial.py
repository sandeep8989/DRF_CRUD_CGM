# Generated by Django 4.0.5 on 2022-06-28 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empmodel',
            fields=[
                ('empid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('Address', models.CharField(max_length=50)),
            ],
        ),
    ]
