from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class About(models.Model):
    """ Author information"""
    name = models.CharField(max_length=250, blank=False)
    title = models.CharField(max_length=250, blank=False)
    greatings = models.CharField(max_length=250, blank=False)
    description = models.TextField()
    image = models.ImageField(upload_to='static/images/author')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=250, blank=False)
    phone_number = models.IntegerField(blank=False)
    email = models.EmailField(max_length=250, blank=True)
    fb_link = models.URLField(max_length=250, blank=True)
    twitter_link = models.URLField(max_length=250, blank=True)
    linkedin_link = models.URLField(max_length=250, blank=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    """Skills information"""
    skill_name = models.CharField(max_length=250, blank=False)
    skill_icon = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.skill_name


class Education(models.Model):
    """Educations information"""
    educations_name = models.CharField(max_length=250, blank=False)
    instituet_name = models.CharField(max_length=250, blank=False)
    start_time = models.DateField(auto_now_add=False)
    end_time = models.DateField(auto_now_add=False)
    cartificate_image = models.ImageField(
        upload_to='static/images/educations', blank=True)

    def __str__(self):
        return self.educations_name


class Experience(models.Model):
    """Experience information"""
    job_name = models.CharField(max_length=250, blank=False)
    company_name = models.CharField(max_length=250, blank=False)
    designation = models.CharField(max_length=250, blank=False)
    start_time = models.DateField(auto_now_add=False)
    end_time = models.DateField(auto_now_add=False)

    def __str__(self):
        return self.job_name


class Recommendation(models.Model):
    """Recommend information"""
    recomender_name = models.CharField(max_length=250, blank=False)
    recomender_position = models.CharField(max_length=250, blank=False)
    recomender_url = models.URLField(unique=True, blank=True)
    recomender_mail = models.EmailField(unique=True, blank=False)
    recomender_say = models.TextField()

    def __str__(self):
        return self.recomender_name


class Interested(models.Model):
    """Interested information"""
    title = models.CharField(max_length=250, blank=False)
    why_interested = models.TextField()
    interested_thinks = models.TextField()

    def __str__(self):
        return self.title


class Client(models.Model):
    """Clients information"""
    client_name = models.CharField(max_length=250, blank=True)
    project_image = models.ImageField(
        upload_to='static/images/educations', blank=False)

    def __str__(self):
        return self.client_name


class Article(models.Model):
    """Article information"""
    article_title = models.CharField(max_length=250, blank=False)
    article_details = models.TextField()
    article_image = models.ImageField(
        upload_to='static/images/articles', blank=True)
    article_category = models.CharField(max_length=100, blank=False)
    publish_time = models.DateField(auto_now_add=True)
    update_time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.article_title
