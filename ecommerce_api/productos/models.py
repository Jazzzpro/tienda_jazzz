from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Producto(models.Model):
    CATEGORIAS = [
        ('Electrónica', 'Electrónica'),
        ('Ropa', 'Ropa'),
        ('Hogar', 'Hogar'),
    ]

    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.BooleanField(default=True)
    categoria = models.CharField(max_length=50, choices=CATEGORIAS)

    def __str__(self):
        return self.nombre

class Nota(models.Model):
    producto = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE,
        related_name='reseñas',
    )
    autor = models.CharField(max_length=100)
    texto = models.TextField()
    puntuacion = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )

    def __str__(self):
        return f"{self.autor} - {self.producto.nombre} - {self.puntuacion}"