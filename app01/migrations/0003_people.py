# Generated by Django 2.2.1 on 2019-09-11 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20190911_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('age', models.IntegerField()),
                ('birthday', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'people',
            },
        ),
    ]
