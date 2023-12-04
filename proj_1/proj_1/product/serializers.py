from rest_framework import serializers
from .models import *


class VarirtyImagesSerializer(serializers.ModelSerializer):
    
    class Meta:
        """meta info"""

        model = VarirtyImages
        fields = "__all__"

class ProductVarietySerializer(serializers.ModelSerializer):

    varity_images = VarirtyImagesSerializer(many=True, source='images')
    
    class Meta:
        """meta info"""

        model = ProductVariety
        fields = "__all__"


class ProductSerilaiser(serializers.ModelSerializer):
    
    class Meta:
        """meta info"""

        model = Product
        fields = "__all__"

    varity = ProductVarietySerializer(many=True,source='varieties')



class BaseProductSerializer(serializers.ModelSerializer):


    class Meta:
        """meta info"""

        model = BaseProduct
        fields = "__all__"

    product = ProductSerilaiser(many=True, source='products')


