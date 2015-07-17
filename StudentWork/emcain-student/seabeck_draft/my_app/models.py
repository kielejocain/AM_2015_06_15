from django.db import models

# Classes:
# Registrant



class Registrant(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)  # will create validation later
    total_owed = models.DecimalField(max_digits=20, decimal_places=4)
    total_paid = models.DecimalField(max_digits=20, decimal_places=4)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def __unicode__(self):
        return self.first_name + " " + self.last_name



# Campers
class Camper(models.Model):
    registrant = models.ForeignKey(Registrant)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    under_18 = models.BooleanField()
    dob = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def __unicode__(self):
        return self.first_name + " " + self.last_name

class Attendance(models.Model):  # i.e. Campers by year
    year = models.IntegerField(max_length=4)
    camper = models.ForeignKey(Camper)
    grade = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.camper.first_name + " " + self.camper.last_name

    def __unicode__(self):
        return self.camper.first_name + " " + self.camper.last_name

class Shirt(models.Model):
    shirt_size_key = models.IntegerField(max_length=2)
    number_required = models.IntegerField(max_length=4)

    shirt_sizes = {
        1: "no shirt",
        2: "Small",
        4: "Medium",
        5: "Large",
        6: "Extra Large"
    }

    def size(self):
        return self.shirt_sizes[self.shirt_size_key]

    # instead make 6 instances of shirt with size assigned



class ShirtOrder(models.Model):
    attendance = models.ForeignKey(Attendance)
    shirt = models.ForeignKey(Shirt)

    def __str__(self):
        return "Camper: " + str(self.attendance.camper) \
               + " shirt order: " + self.shirt.size_name

    def __unicode__(self):
        return "Camper: " + unicode(self.attendance.camper) \
               + " shirt order: " + self.shirt.size_name

class FoodPreference(models.Model):
    camper = models.ForeignKey(Camper)
    meat_preference = models.TextField()  # limited options --change eventually to new table
    gluten_free = models.BooleanField()
    dairy_free = models.BooleanField()
    other = models.TextField()
    severity = models.TextField()  # change eventually to new table.

# Rates
class Rate(models.Model):
    # find out how to restrict this to preset types e.g. housing, registration, tshirt
    type = models.CharField(max_length=20)
    # e.g. SM (if tshirt), Pines (if housing)
    item = models.IntegerField()
    cost_per = models.DecimalField(max_digits=20, decimal_places=4)  # do as dollars or as cents???

    def __str__(self):
        return "type: " + self.type \
               + "item: " + self.item \
               + "rate: $" + str(self.cost_per)

    def __unicode__(self):
        return "type: " + self.type \
               + "item: " + self.item \
               + "rate: $" + str(self.cost_per)

