# Generated by Django 4.2.4 on 2023-08-27 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_sample_age_alter_sample_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='age',
            field=models.IntegerField(),
        ),
    ]
