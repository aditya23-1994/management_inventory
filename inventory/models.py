from django.db import models


class Product(models.Model):
    
    choices = [
        ('ele','electronics'),
        ('book','books'),
        ('apperals','clothings')
    ]

    name = models.CharField(max_length=55)
    category = models.CharField(max_length=50,
                                choices=choices,
                                default = 'electronics')
    description = models.TextField()
    price = models.IntegerField()
    is_available = models.BooleanField(default=True)
    quantity = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):  
        return self.name 



    class Meta:
        
        ordering = ('-created',)
    
    def get_total_cost(self):

        get_cost =self.price * self.quantity
        return get_cost  

class Customer(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    house = models.CharField(max_length=20)

    def __str__(self):

        return 'paid {} &  {}'.format(self.name,self.email)
        