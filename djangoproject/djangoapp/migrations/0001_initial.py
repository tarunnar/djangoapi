# Generated by Django 2.2.4 on 2019-08-23 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('empid', models.IntegerField(primary_key=True, serialize=False)),
                ('empname', models.CharField(max_length=100)),
                ('empage', models.IntegerField()),
                ('empexp', models.IntegerField()),
            ],
        ),
    ]
