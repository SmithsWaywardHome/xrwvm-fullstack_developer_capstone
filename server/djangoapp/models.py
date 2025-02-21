# Uncomment the following imports before adding the Model code

from django.db import models
# from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object


class CarMake(models.Model):
    ORIGIN_CHOICES = [
        ("DOMESTIC","Domestic"),
        ("IMPORT","Import")
    ]

    name = models.CharField(
        max_length=64
    )

    description = models.TextField()

    origin = models.CharField(
        max_length=8,
        choices=ORIGIN_CHOICES,
        default='0'
    )

    def __str__(self):
        return f'name: {self.name}' 

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
# - Name
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object


class CarModel(models.Model):
    TYPE_CHOICES = [
        ("COUPE","Coupe"), 
        ("CROSSOVER","Crossover"), 
        ("DELIVERY VAN","Delivery Van"), 
        ("HATCHBACK","Hatchback"), 
        ("MINIVAN","Minivan"), 
        ("PICKUP","Pickup"), 
        ("SEDAN","Sedan"), 
        ("SUV","SUV"), 
        ("WAGON","Wagon")
    ]

    DRIVETRAIN_CHOICES = [
        ("DIESEL","Diesel"), 
        ("ELECTRIC","Electric"), 
        ("GAS","Gas"), 
        ("HYBRID","Hybrid"), 
        ("HYDROGEN","Hydrogen"), 
        ("MULTIFUEL","Mulitfuel")
    ]

    name = models.CharField(
        max_length=64
    )

    car_make = models.ForeignKey(
        CarMake,
        on_delete=models.CASCADE
    )

    dealer_id = models.IntegerField(
        default=0
    )

    type = models.CharField(
        max_length=12,
        choices=TYPE_CHOICES,
        default='SUV'
    )

    year = models.IntegerField(
        default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ]
    )

    drivetrain = models.CharField(
        max_length=10,
        choices=DRIVETRAIN_CHOICES,
        default='ELECTRIC'
    )

    def __str__(self):
        return f'name: {self.name}'
