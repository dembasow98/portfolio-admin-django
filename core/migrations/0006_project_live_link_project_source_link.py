# Generated by Django 4.1.1 on 2023-06-14 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_image_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='live_link',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='source_link',
            field=models.TextField(blank=True, null=True),
        ),
    ]
