from typing import Any
from django.db.models import Q
from rest_framework import serializers
from rest_framework.validators import (
    UniqueTogetherValidator,
    UniqueValidator,
)

from .models import (
    Product, Customer, Insurance
)
from .validators import phone_number_validator


class ProductSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(max_length=255)
    product_category = serializers.CharField(max_length=255)
    product_description = serializers.CharField(max_length=255)
    product_price = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = Product
        fields = (
            "id",
            "product_name",
            "product_category",
            "product_description",
            "product_price",
        )
        validators = [
            UniqueTogetherValidator(
                queryset=Product.objects.all(),
                fields=["product_name", "product_category"],
                message="Product already exists",
            )
        ]

class CustomerSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    phone_number = serializers.CharField(
        max_length=20,
        validators=[
            phone_number_validator,
            UniqueValidator(
                queryset=Customer.objects.all(),
                message="This phone number already exists",
                lookup="iexact",
            ),
        ],
    )
    id_number = serializers.IntegerField(
        required=True,
        validators=[UniqueValidator(queryset=Customer.objects.all())],
    )
    email = serializers.EmailField(
        required=False,
        validators=[UniqueValidator(queryset=Customer.objects.all())],
    )
    kin_first_name = serializers.CharField(max_length=255)
    kin_last_name = serializers.CharField(max_length=255)
    kin_phone_number = serializers.CharField(
        max_length=20,
        validators=[
            phone_number_validator,
            UniqueValidator(
                queryset=Customer.objects.all(),
                message="This phone number already exists",
                lookup="iexact",
            ),
        ],
    )
    kin_id_number = serializers.IntegerField(
        required=False,
        validators=[UniqueValidator(queryset=Customer.objects.all())],
    )
    kin_relationship = serializers.CharField(max_length=255)


    class Meta:
        model = Customer
        fields = (
            "id",
            "first_name",
            "last_name",
            "phone_number",
            "id_number",
            "email",
            "kin_first_name",
            "kin_last_name",
            "kin_phone_number",
            "kin_id_number",
            "kin_relationship",
        )

    def validate_phone_number(self, phone_number: Any) -> Any:
        if not Customer.objects.filter(
                Q(phone_number=phone_number)
        ).exists():
            return phone_number

        raise serializers.ValidationError("This phone number already exists")




class InsuranceSerializer(serializers.ModelSerializer):
    product_issued = serializers.SlugRelatedField(
        queryset=Product.objects.all(), slug_field="product_name"
    )
    customer = serializers.SlugRelatedField(
        queryset=Customer.objects.all(), slug_field="id_number"
    )
    policy_number = serializers.CharField(max_length=255)

    class Meta:
        model = Insurance
        fields = (
            "id",
            "product_issued",
            "customer",
            "policy_number",
        )