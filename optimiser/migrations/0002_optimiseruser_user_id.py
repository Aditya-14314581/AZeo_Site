# Generated by Django 3.2.3 on 2022-01-16 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('optimiser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='optimiseruser',
            name='user_id',
            field=models.CharField(default='0000000', max_length=100),
        ),
    ]
