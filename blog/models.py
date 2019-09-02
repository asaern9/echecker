from django.db import models

# Create your models here.
CHECKER_OPTION = (
    ('Checker 1', 'Checker 1'),
    ('Checker 2', 'Checker 2'),
    ('Checker 3', 'Checker 3')
)


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    checker = models.CharField(max_length=30, choices=CHECKER_OPTION, null=True, default='Checker 1')
    reference = models.CharField(max_length=50, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name