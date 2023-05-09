# Generated by Django 4.2.1 on 2023-05-09 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_usercontent'),
    ]

    operations = [
        migrations.AddField(
            model_name='codecontent',
            name='label',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='codecontent',
            name='submit',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='imagecontent',
            name='label',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='imagecontent',
            name='submit',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='textcontent',
            name='label',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='textcontent',
            name='submit',
            field=models.IntegerField(default=0),
        ),
    ]
