from django.db import models

# Create your models here.

class project(models.Model):
    project_title = models.CharField(max_length=200)
    project_content = models.TextField()
    project_link_title = models.CharField(max_length=100)
    project_link = models.URLField( 
        max_length=128)
    project_image = models.ImageField(upload_to = 'static/images/', height_field=None, width_field=None, max_length=100)


    def __str__(self):
        return self.project_title




class contact(models.Model):
    contact_FirstName = models.CharField(max_length=200)
    contact_LastName = models.CharField(max_length=200)
    contact_Email = models.CharField(max_length=200)
    contact_Subject = models.CharField(max_length=200)
    contact_body = models.TextField()

    


    def __str__(self):
        return self.contact_FirstName