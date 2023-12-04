from rest_framework import serializers
from .models import *



class BaseProductSerializer(serializers.ModelSerializer):

    class Meta:
        """meta info"""

        model = BaseProduct
        fields = "__all__"

    products = serializers.SerializerMethodField(required=False)

    def get_products(self, instance):

        """function to get details of a product"""

        products = instance.products.all()

        product_list = []

        for item in products:
            data = {
                "id": item.id,
                "item_hsn": item.item_hsn,
                "item_code": "100", 
                "mrp": "85.00",
                "varity": []
                }
            varieties = item.varieties.all()
            for variety in varieties:
                prod_variety = {
                    "variation_name": variety.variation_name,
                    "variation_value": variety.variation_value,
                    "created_at": variety.created_at,
                    "updated_at": variety.updated_at,
                    "varity": variety.variety,
                    "varity_images": []
                }
                images = variety.images.all()
                for image in images:
                    image_data = {
                        "id": image.id,
                        "variantproduct_image": image.image.url,
                        "created_at":image.created_at,
                        "updated_at": image.updated_at,
                        "varity_images": 24
                    }

                    prod_variety['varity_images'].append(image_data)
                data["varity"].append(prod_variety)

            product_list.append(data)

        return product_list








