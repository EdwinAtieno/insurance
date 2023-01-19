from django.db import models
from app.abstracts import (
    IntegerIDModel,
    TimeStampedModel,
)
from app.validators import phone_number_validator
from django.utils.translation import gettext_lazy as _

class Product(IntegerIDModel, TimeStampedModel):
    product_name = models.CharField(max_length=255, unique=True)
    product_category = models.CharField(max_length=255, unique=True)
    product_description = models.TextField()
    product_price = models.DecimalField(max_digits=10, decimal_places=2)

    is_visible = models.BooleanField(
        default=False,
        help_text="Is the classification visible on the frontend",
    )

    def __str__(self) -> str:
        return self.product_name


class Customer(IntegerIDModel, TimeStampedModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(
        max_length=20,
        unique=True,
        verbose_name=_("Phone Number"),
        validators=[
            phone_number_validator,
        ],
    )
    email = models.CharField(max_length=255, unique=True)
    id_number = models.CharField(
        max_length=255, verbose_name=_("ID Number"), null=True, unique=True
    )
    kin_first_name = models.CharField(max_length=255)
    kin_last_name = models.CharField(max_length=255)
    kin_phone_number = models.CharField(
        max_length=20,
        unique=True,
        verbose_name=_("Phone Number"),
        validators=[
            phone_number_validator,
        ],
    )
    kin_id_number = models.IntegerField(
        verbose_name=_("ID Number"), null=True, unique=True
    )
    kin_relationship = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.first_name


class Insurance(IntegerIDModel, TimeStampedModel):
    product_issued = models.ForeignKey(Product, on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    policy_number = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.policy_number