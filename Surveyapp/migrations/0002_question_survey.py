# Generated by Django 2.1.5 on 2019-02-13 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Surveyapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='survey',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Surveyapp.Survey'),
        ),
    ]