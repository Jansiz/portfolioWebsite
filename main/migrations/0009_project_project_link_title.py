# Generated by Django 4.0.4 on 2022-05-05 21:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_project_project_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_link_title',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]