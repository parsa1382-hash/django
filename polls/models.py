from django.db import models

class Question(models.Model):
    qtext = models.CharField(max_length = 200)
    qdate = models.DateTimeField('date published')
    def __str__(self):
        return self.qtext


class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete = models.CASCADE)
    ctext = models.CharField(max_length = 100)
    votes = models.IntegerField(default = 0)
    def __str__(self):
        return self.ctext
'''


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()
    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField()
    number_of_pingbacks = models.IntegerField()
    rating = models.IntegerField()

'''


# Create your models here.
