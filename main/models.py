from django.db import models





class Category(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    

class Author(models.Model):
    photo = models.ImageField()
    name = models.CharField(max_length=100)
    date = models.DateField()


class Posts(models.Model):
    photo = models.ImageField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    views = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)



class Video(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    video_link = models.URLField()



class AboutUs(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    video = models.URLField()



class NewsTeam(models.Model):
    position = models.CharField(max_length=100)
    name = models.CharField(max_length=100)



class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    addfile = models.FileField()




class SendPost(models.Model):
    title = models.CharField(max_length=100)
    tags = models.CharField(max_length=255)
    image = models.ImageField()
    explanation = models.TextField()



class SendVideo(models.Model):
    title = models.CharField(max_length=100)
    tags = models.CharField(max_length=255)
    video = models.URLField()
    explanation = models.TextField()



class Edit(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    oldpassword = models.IntegerField()
    password = models.IntegerField()
    email = models.EmailField()
    addbanner = models.ImageField()
    addimage = models.ImageField()
    explanation = models.CharField(max_length=100)