from django.db import models
from datetime import date


# Create your models here.
class Usertype(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Blogpost(models.Model):
    post_id=models.AutoField(primary_key=True,default=None)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    author_name = models.CharField(max_length=50, null=True)
    user_type = models.ForeignKey(Usertype, on_delete=models.CASCADE, default=1)
    description = models.TextField(max_length=2000, help_text="Enter you blog text here.")
    post_date = models.DateField(default=date.today)
    image = models.ImageField(upload_to='Uploads/images/')

    @staticmethod
    def get_all_post():
        return Blogpost.objects.all()

    @staticmethod
    def admin_all_post():
        return Blogpost.objects.filter(user_type=1)

    @staticmethod
    def user_all_post():
        return Blogpost.objects.filter(user_type=2)


