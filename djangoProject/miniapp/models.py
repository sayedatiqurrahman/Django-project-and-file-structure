from django.db import models
from django.utils import timezone


# Create your models here.
class AppVariety(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="mini_apps/")
    app_type = models.CharField(
        max_length=2,
        choices=[
            ("FR", "Fresh App"),
            ("SO", "Somosa App"),
            ("JR", "Junior App"),
            ("SR", "Senior App"),
            ("GR", "Graduate App"),
        ],
    )
    date_added = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True, null=True, default="")
    is_active = models.BooleanField(default=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00, blank=True, null=True
    )

    def __str__(self):
        # return super().__str__()
        return self.name
