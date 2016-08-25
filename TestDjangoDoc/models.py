from django.db import models


class Persons(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),

    )
    # Auto incrementing primary key
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Person(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.name


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)


class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=50)


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_star = models.IntegerField()


    # Use of meta tag for model inheritance


class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True


class Student(CommonInfo):
    home_group = models.CharField(max_length=5)


# Meta Inheritance
class CommonInfos(models.Model):
    # ...
    class Meta:
        abstract = True
        ordering = ['name']


class Students(CommonInfo):
    # ...
    class Meta(CommonInfo.Meta):
        db_table = 'student_info'


# One to one
class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):  # __unicode__ on Python 2
        return "%s the place" % self.name


class Restaurant(models.Model):
    place = models.OneToOneField(
            Place,
            on_delete=models.CASCADE,
            primary_key=True,
    )
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):  # __unicode__ on Python 2
        return "%s the restaurant" % self.place.name


class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):  # __unicode__ on Python 2
        return "%s the waiter at %s" % (self.name, self.restaurant)


# Proxy Models

class Personss(models.Model):
    first_name= models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class MyPerson(Personss):
    class Meta:
        proxy = True

    def do_something(self):
        # ...
        pass
