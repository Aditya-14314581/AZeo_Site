# Generated by Django 3.2.6 on 2022-03-18 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chemathon', '0007_auto_20220317_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chemathon_questions',
            name='question1',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='chemathon_questions',
            name='question2',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='chemathon_questions',
            name='question3',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='chemathon_questions',
            name='question4',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='chemathon_questions',
            name='question5',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='chemathon_questions',
            name='question6',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='chemathon_questions',
            name='question7',
            field=models.FloatField(null=True),
        ),
    ]