from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone
from uuid import uuid4

from apps.landing.models import *

class Website(models.Model):
    section1Title = models.CharField(null=True, blank=True, max_length=200)
    section1Description = models.TextField(null=True, blank=True)
    callToAction = models.CharField(null=True, blank=True, max_length=100)
    section1Image = models.ImageField(default='default.jpg', upload_to='landing_page_images')

    section3Title = models.CharField(null=True, blank=True, max_length=200)
    section3Description = models.TextField(null=True, blank=True)
    section3Image = models.ImageField(default='default.jpg', upload_to='landing_page_images')

    ##RELATED FIELDS
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    #Utility Variable
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.section1Title, self.uniqueId)

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]

        self.slug = slugify('{} {}'.format(self.section1Title, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())
        super(Website, self).save(*args, **kwargs)



class WebsiteService(models.Model):
    title = models.CharField(null=True, blank=True, max_length=200)
    description = models.TextField(null=True, blank=True)
    icon = models.CharField(null=True, blank=True, max_length=200)

    ##RELATED FIELDS
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    #Utility Variable
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.title, self.uniqueId)

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]

        self.slug = slugify('{} {}'.format(self.title, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())
        super(WebsiteService, self).save(*args, **kwargs)


class WebsiteFeatures(models.Model):
    title = models.CharField(null=True, blank=True, max_length=200)
    description = models.TextField(null=True, blank=True)
    icon = models.CharField(null=True, blank=True, max_length=200)
    image = models.ImageField(default='default.jpg', upload_to='landing_page_images')

    ##RELATED FIELDS
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    #Utility Variable
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.title, self.uniqueId)

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]

        self.slug = slugify('{} {}'.format(self.title, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())
        super(WebsiteFeatures, self).save(*args, **kwargs)
        
        
#########################
# WEATHER API
#########################

class Storms(models.Model):
    storm = models.CharField(null=True, blank=True, max_length=200)
    date_search_query = models.TextField(null=True, blank=True)


    #Utility Variable
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.title, self.uniqueId)

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]

        self.slug = slugify('{} {}'.format(self.title, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())
        super(Storms, self).save(*args, **kwargs)