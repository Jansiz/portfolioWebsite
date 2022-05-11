# Generated by Django 4.0.4 on 2022-05-11 07:06

from django.db import migrations, models
import django.utils.timezone
import main.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_skills_skill_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='skills',
            name='skill_file',
            field=models.FileField(default=django.utils.timezone.now, upload_to='static/images/', validators=[main.validators.validate_file_extension]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='skills',
            name='skill_image',
            field=models.ImageField(upload_to='static/images/'),
        ),
    ]