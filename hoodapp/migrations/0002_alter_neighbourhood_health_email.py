# Generated by Django 4.0.5 on 2022-06-19 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoodapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighbourhood',
            name='health_email',
            field=models.EmailField(default='default', max_length=100),
        ),
    ]