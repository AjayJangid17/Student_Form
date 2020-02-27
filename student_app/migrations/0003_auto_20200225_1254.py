# Generated by Django 3.0.3 on 2020-02-25 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0002_auto_20200225_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentform',
            name='dob',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='studentform',
            name='gender',
            field=models.CharField(default=None, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='studentform',
            name='mobile',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='studentform',
            name='address',
            field=models.TextField(default=None, null=True),
        ),
    ]
