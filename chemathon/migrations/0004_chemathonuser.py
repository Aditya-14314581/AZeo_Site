# Generated by Django 3.2.3 on 2022-03-10 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chemathon', '0003_chemathon_questions_submitted_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chemathonuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member1', models.CharField(max_length=100)),
                ('member2', models.CharField(max_length=100)),
                ('team_id', models.CharField(max_length=100)),
            ],
        ),
    ]