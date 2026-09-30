from django.db import models

class Producto(models.Model):
    CATEGORIAS = {
        ('Electrónica', 'Electrónica'),
        ('Ropa', 'Ropa'),
        ('Hogar', 'Hogar'),
    }

    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.BooleanField(default=True)
    categoria = models.CharField(max_length=50, choices=CATEGORIAS)

    def __str__(self):
        return self.nombre

        