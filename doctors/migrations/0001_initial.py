# Generated by Django 4.1 on 2022-08-13 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('degree', models.CharField(max_length=255)),
                ('specialization', models.CharField(max_length=255)),
                ('hospital', models.CharField(max_length=255)),
                ('experience', models.IntegerField()),
                ('awards', models.IntegerField(default=None)),
            ],
        ),
    ]
