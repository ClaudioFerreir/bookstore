from rest_framework import serializers

from product.models.category import Category


class CategorySerializer(serializers.ModelSerializer):  # here I don't wanna customize my fields
    class Meta:
        model = Category
        fields = [
            'title',
            'slug',
            'description',
            'active',
        ]
