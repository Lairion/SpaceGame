from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from SpaceMap.models import StarSystem,Planet,City
# Create your models here.
class Character(models.Model):
    user_id = models.ForeignKey(User,null=True, blank=True)
    name_character = models.CharField(max_length=100)
    level = models.IntegerField(default = 1)
    exp = models.IntegerField(default = 0)
    points = models.IntegerField(default= 0)
    image = models.ImageField(null=True, blank=True, upload_to='character_image/%Y/%m/%d')
    credits = models.IntegerField(default= 1000)
    is_active = models.BooleanField(default=False)
    def __str__(self):
        return self.name_character
    def get_absolute_url(self):
        return reverse("Character:character", kwargs={"id": self.id})
    
    def buy_engine(self,engine):
        if self.credits >= engine.price:
            self.credits -= engine.price
            ship = Ship.objects.get(character_id = self)
            ship_engine = Engine_ship.objects.filter(ship_id = ship)
            if ship_engine != null:
                self.credits += ship_engine.price
                del ship_engine
            Engine_ship.create(ship_id = ship, 
                    price = engine.price,
                    name_engine = engine.name_engine,
                    power = engine.power,
                    durability = engine.durability,
                    tank = engine.tank,
                    weight = engine.weight
                 )
                

             

class Ship(models.Model):
    """docstring for Ship"""
    character_id = models.ForeignKey(Character,null=True, blank=True)
    system_id = models.ForeignKey(StarSystem,null=True, blank=True)
    planate_id = models.ForeignKey(Planet,null=True, blank=True)
    city_id = models.ForeignKey(City,null=True, blank=True)
    SHIP_CLASS = (("DR","DRAGUN"),
        ("HS","HeavyShip"),
        ("MD","Medical"),("CG","CargoShip"))
    name_ship = models.CharField(max_length=100)
    ship_class = models.CharField(max_length=3,choices=SHIP_CLASS,default="DR") 
    armor = models.IntegerField(default=400)
    load = models.IntegerField(default=10000)
    laser_count = models.IntegerField(default=1)
    evasion = models.IntegerField(default=0)

    def __str__(self):
        return self.name_ship
    def get_absolute_url(self):
        return reverse("Character:ship_interface", kwargs={"id": self.id})

    def change_characteristic(self):
        if self.ship_class == "DR":
            self.armor = 200
            self.evasion = 12
            self.laser_count = 6
            self.load = 400
        elif self.ship_class == "HS":
            self.armor = 1000
            self.evasion = 4
            self.laser_count = 10
            self.load = 1200
        elif self.ship_class == "MD":
            self.armor = 500 
            self.evasion = 10
            self.laser_count = 4
            self.load = 800
        elif self.ship_class == "CG":
            self.armor = 600 
            self.evasion = 8
            self.laser_count = 2
            self.load = 1500
        self.save()





class Engine_ship(models.Model):
    """docstring for Engine"""
    ship_id = models.ForeignKey(Ship,null=True, blank=True)
    price = models.DecimalField(max_digits=19, decimal_places=2)
    name_engine = models.CharField(max_length=100)
    power = models.IntegerField(default=1000)
    durability = models.IntegerField(default=1000)
    tank = models.IntegerField(default=0)
    weight = models.IntegerField(default=500)
    def __str__(self):
        return self.name_engine

class Engine(models.Model):
    """docstring for Engine"""
    price = models.DecimalField(max_digits=19, decimal_places=2)
    name_engine = models.CharField(max_length=100)
    power = models.IntegerField(default=1000)
    durability = models.IntegerField(default=1000)
    tank = models.IntegerField(default=0)
    weight = models.IntegerField(default=500)
    def __str__(self):
        return self.name_engine

class Laser_ship(models.Model):
    """docstring for Engine"""
    ship_id = models.ForeignKey(Ship,null=True, blank=True)
    price = models.DecimalField(max_digits=19, decimal_places=2)
    name_laser = models.CharField(max_length=100)
    power = models.IntegerField(default=1000)
    durability = models.IntegerField(default=1000)
    weight = models.IntegerField(default=500)
    def __str__(self):
        return self.name_laser

class Laser(models.Model):
    """docstring for Engine"""
    price = models.DecimalField(max_digits=19, decimal_places=2)
    name_laser = models.CharField(max_length=100)
    power = models.IntegerField(default=1000)
    durability = models.IntegerField(default=1000)
    weight = models.IntegerField(default=500)
    def __str__(self):
        return self.name_laser

        

