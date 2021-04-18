from django.db import models


class Food(models.Model):
    SOUP = "SO"
    OTHER = "OT"
    PIZZA = "PI"
    SALAD = "SA"
    FRESH_JUICE = "FJ"
    DRINKS = "DR"
    WINE = "WI"

    FOOD_TYPE_CHOICES = [
        (SOUP, "Polievky"),
        (PIZZA, "Pizza"),
        (SALAD, "Šaláty"),
        (OTHER, "Iné"),
        (FRESH_JUICE, "Fresh štavy"),
        (DRINKS, "Nápoje"),
        (WINE, "Vína")
    ]

    name = models.CharField(max_length=100)
    weight = models.IntegerField(default=None, null=True, verbose_name="Weight of food in grams", blank=True)
    allergens = models.TextField(default=None, null=True, verbose_name="List of integers separated by comma", blank=True)
    ingredients = models.TextField(default=None, null=True, blank=True)
    category = models.CharField(max_length=2, default=OTHER, choices=FOOD_TYPE_CHOICES)
    image = models.ImageField(default=None, null=True, upload_to="upload", blank=True)
    price = models.DecimalField(verbose_name="Price in EUR", decimal_places=2, max_digits=6)

    @property
    def category_display_name(self):
        for choice_code, choice_name in self.FOOD_TYPE_CHOICES:
            if choice_code == self.category:
                return choice_name
