# Generated by Django 4.0.4 on 2022-05-10 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_project_project_link_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_FirstName', models.CharField(max_length=200)),
                ('contact_LastName', models.CharField(max_length=200)),
                ('contact_Email', models.CharField(max_length=200)),
                ('contact_Subject', models.CharField(max_length=200)),
                ('contact_body', models.TextField()),
            ],
        ),
    ]
