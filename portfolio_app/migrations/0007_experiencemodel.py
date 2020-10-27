# Generated by Django 3.0.8 on 2020-07-30 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0006_jobskills_js_interest'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExperienceModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=120)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(default='Present')),
                ('job_title', models.CharField(max_length=120)),
                ('desrp', models.TextField()),
            ],
        ),
    ]