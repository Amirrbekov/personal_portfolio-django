# Generated by Django 4.1.2 on 2022-10-24 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='descriptions',
            field=models.TextField(verbose_name='Descriptions'),
        ),
    ]
