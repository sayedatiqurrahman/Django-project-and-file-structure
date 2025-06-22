from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from decimal import Decimal


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
    price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    def __str__(self):
        # return super().__str__()
        return self.name


# one to Many relationship with AppVariety


class AppReview(models.Model):
    app = models.ForeignKey(
        AppVariety,
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name="App Variety",
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_text = models.TextField(default="")
    rating = models.PositiveIntegerField(default=0)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} - {self.app.name}"


# many to many relationship with AppVariety
class AppStore(models.Model):
    name = models.CharField(max_length=100)
    mother_company = models.CharField(max_length=255)
    app_varieties = models.ManyToManyField(AppVariety, related_name="stores")
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name + " store of " + self.mother_company
    

# one to one relationship with AppVariety

class AppCertificates(models.Model):
    app = models.OneToOneField(
        AppVariety,
        on_delete=models.CASCADE,
        related_name="certificates",
        verbose_name="App Name",
    )
    certificate_name = models.CharField(max_length=255)
    certificate_number = models.CharField(max_length=100, unique=True)
    issued_by = models.CharField(max_length=255)
    issue_date = models.DateTimeField(default=timezone.now)
    expiry_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.certificate_name} for {self.app.name}"
