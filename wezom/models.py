from django.db import models


class Brand(models.Model):
    """

    """
    name = models.CharField(max_length=200, db_index=True, unique=True)

    def __str__(self):
        return f"{self.name}"


class Model(models.Model):
    name = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True,  null=True,)


class LostAuto(models.Model):
    user = models.CharField(max_length=200)
    vin_code = models.CharField(max_length=200, db_index=True)
    number = models.CharField(max_length=200, db_index=True)
    color = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True,  null=True, related_name="brand_auto")
    model = models.ForeignKey(Model, on_delete=models.CASCADE, blank=True,  null=True, related_name="model_auto")

    class Meta:
        verbose_name = "Lost auto"
        verbose_name_plural = "Losts auto"
