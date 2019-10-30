from django.db import models

# Create your models here.
class Blog(models.Model):
    blog_id=models.AutoField(primary_key=True)
    heading=models.CharField(max_length=300)
    blogTitle=models.CharField(max_length=200)
    blogText=models.TextField()
    img=models.ImageField(upload_to='blog/images',default="")
    blogDate=models.DateTimeField()

    def __str__(self):
        return self.blogTitle[0:20]+"............."
