from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class Home(models.Model):
    name = models.CharField(max_length=45)
    slug = models.SlugField()
    text = models.TextField()
    pic = models.ImageField(upload_to='home/')
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.name
    def save_home(self):
        self.save()
    @classmethod
    def all_home(cls):
        all1 = cls.objects.order_by('-pub_date')
        return all1
    def get_absolute_url(self):
        return reverse('detail',kwargs={"slug":self.slug})
    @classmethod
    def url11(request,slug):
        url1 = Home.objects.get(slug=slug)
        return url1
class produce(models.Model):
    name = models.CharField(max_length=45)
    slug = models.SlugField()
    text = models.TextField()
    pic = models.ImageField(upload_to='home/')
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.name
    def save_home(self):
        self.save()
    @classmethod
    def all_produce(cls):
        all7 = cls.objects.order_by('-pub_date')
        return all7
    @classmethod
    def get_absolute_url(request,slug):
        return reverse('details',kwargs={"slug":self.slug})
class market(models.Model):
    name = models.CharField(max_length=45)
    slug = models.SlugField()
    text = models.TextField()
    pic = models.ImageField(upload_to='home/')
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.name
    def save_market(self):
        self.save()
    @classmethod
    def all_mkt(cls):
        all9 = cls.objects.order_by('-pub_date')
        return all9
    @classmethod
    def get_absolute_url(request,slug):
        return reverse('details',kwargs={"slug":self.slug})
class Sell(models.Model):
    sold_by = models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=45)
    slug = models.SlugField()
    text = models.TextField()
    price = models.DecimalField(decimal_places=2,max_digits=999)
    available = models.BooleanField()
    pic = models.ImageField(upload_to='home/')
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    def save_sell(self):
        self.save()
    @classmethod
    def all_sell(cls):
        all90 = cls.objects.order_by('-pub_date')
        return all90
    @classmethod
    def get_absolute_url(request,slug):
        return reverse('details',kwargs={"slug":self.slug})
class Help(models.Model):
    #name = models.OneToOneField(User,on_delete=models.CASCADE)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
    def save_help(self):
        self.save()
