from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Signup(models.Model):
    email = models.EmailField()
    business = models.BooleanField(default=False)
    category = models.CharField(max_length=300)
    customer_size = models.IntegerField(default=0)
    online_spend = models.IntegerField(default=0)
    spend_commitment = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

# Create your models here.
class Customer(models.Model):
    company_name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now=True)
    contact_person = models.ManyToManyField(User, null=True, blank=True)

    def __unicode__(self):
        return self.company_name

class Ambassador(models.Model):
    name = models.ForeignKey(User)
    brand = models.ForeignKey(Customer)
    twitter = models.CharField(max_length=140, null=True, blank=True)
    facebook = models.CharField(max_length=140, null=True, blank=True)
    google_plus = models.CharField(max_length=140, null=True, blank=True)
    instagram = models.CharField(max_length=140, null=True, blank=True)
    snapchat = models.CharField(max_length=140, null=True, blank=True)
    pinterest = models.CharField(max_length=140, null=True, blank=True)

    def __unicode__(self):
        return ('%s %s') % (self.name.first_name, self.name.last_name)

class Campaign(models.Model):
    company = models.ForeignKey(Customer, null=True, blank=True)
    money_pool = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return ('%s %s campaign' ) % (self.company.company_name, self.id)


class FacebookPoint(models.Model):
    campaign = models.ForeignKey(Campaign)
    ambassador = models.ForeignKey(Ambassador)
    points = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return ('%s points earned for %s') % (self.points, self.campaign)


class TwitterPoint(models.Model):
    campaign = models.ForeignKey(Campaign)
    ambassador = models.ForeignKey(Ambassador)
    points = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return ('%s points earned for %s') % (self.points, self.campaign)
