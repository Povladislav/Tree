from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=50, verbose_name="name")
    in_menu = models.ForeignKey(
        "app.Menu", on_delete=models.CASCADE, related_name="items"
    )

    def __str__(self):
        return self.name


class Menu(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name="menu_name")

    def __str__(self):
        return self.name
