# Generated by Django 2.0.6 on 2018-06-15 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='loanrequest',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
