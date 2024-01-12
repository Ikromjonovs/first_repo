from django.db import models
from django.contrib.auth.models import User


class Banner(models.Model):
    photo = models.ImageField()
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)


class AboutUs(models.Model):
    photo = models.ImageField()
    title = models.CharField(max_length=255)
    text = models.TextField()


class Feature(models.Model):
    icon = models.FileField()
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)


class Category(models.Model):
    name = models.CharField(max_length=255)
    icon = models.FileField()


class Description(models.Model):
    text = models.TextField()
    choice = models.IntegerField(choices=(
        (1, 'Catalog'),
        (2, 'Portfolio'),
        (3, 'Service'),
        (4, 'Contact'),
    ))


class Color(models.Model):
    name = models.CharField(max_length=255)


class ProductPhoto(models.Model):
    photo = models.ImageField()


class Info(models.Model):
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=522)
    photo = models.ManyToManyField(ProductPhoto)
    price = models.IntegerField()
    bonus = models.IntegerField(default=0)
    color = models.ManyToManyField(Color, blank=True)
    description = models.TextField()
    info = models.ManyToManyField(Info)
    file = models.FileField()
    min_quantity = models.IntegerField()
    quantity = models.IntegerField()
    code = models.CharField(max_length=255)


class Service(models.Model):
    photo = models.ImageField()
    icon = models.FileField()
    title = models.CharField(max_length=255)
    text = models.TextField()


class Feedback(models.Model):
    photo = models.ImageField()
    company_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    text = models.TextField()


class AboutUsNumber(models.Model):
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255)


class Blog(models.Model):
    photo = models.ImageField()
    title = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateField()


class Faq(models.Model):
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)


class Subscriber(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)


class Portfolio(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField()
    like = models.IntegerField()


class Comment(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)


class Partner(models.Model):
    photo = models.FileField()


class Production(models.Model):
    text = models.TextField()
    video = models.FileField()


class Job(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    salary = models.CharField(max_length=522)


class History(models.Model):
    text = models.CharField(max_length=255)
    info = models.ManyToManyField(Info, blank=True)


class HistoryInfo(models.Model):
    text = models.CharField(max_length=255)
    date = models.IntegerField()
    photo = models.ImageField()


class Contact(models.Model):
    text = models.TextField()
    location = models.ManyToManyField("Location")


class Location(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    phone1 = models.CharField(max_length=255)
    email = models.EmailField()
    rekvizit = models.FileField()
    working_hour = models.ManyToManyField('WorkingHours')
    image = models.ImageField()
    position = models.CharField(max_length=255)
    owner_phone = models.CharField(max_length=255)
    owner_email = models.CharField(max_length=255)
    lat = models.CharField(max_length=255)
    lng = models.CharField(max_length=255)


class WorkingHours(models.Model):
    days = models.CharField(max_length=255)
    opens = models.TimeField(null=True, blank=True)
    close = models.TimeField(null=True, blank=True)
    weekend = models.BooleanField(default=True)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    color = models.ForeignKey(Color, on_delete=models.CASCADE)

    def get_total(self):
        return self.quantity * self.product.bonus if self.product.bonus else self.product.price


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    inn = models.IntegerField()
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    status = models.IntegerField(choices=(
        (1, 'delivery'),
        (2, 'manual')
    ))
    address = models.CharField(max_length=255)
    comment = models.CharField(max_length=2556)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
