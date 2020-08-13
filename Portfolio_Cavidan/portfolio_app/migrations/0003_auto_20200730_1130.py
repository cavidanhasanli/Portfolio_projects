# Generated by Django 3.0.8 on 2020-07-30 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0002_auto_20200730_0902'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalmodel',
            name='comunity',
            field=models.FloatField(default=0.0, max_length=1.0),
        ),
        migrations.AddField(
            model_name='generalmodel',
            name='info',
            field=models.FloatField(default=0.0, max_length=1.0),
        ),
        migrations.AddField(
            model_name='generalmodel',
            name='safety',
            field=models.FloatField(default=0.0, max_length=1.0),
        ),
        migrations.AddField(
            model_name='generalmodel',
            name='solving',
            field=models.FloatField(default=0.0, max_length=1.0),
        ),
    ]
