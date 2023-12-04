from django.db import models

# Create your models here.


class AbstractBase(models.Model):
    """class to store basic details of objects"""

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


class Category(models.Model):

    """class to store deatils of product category"""

    name = models.CharField(max_length=150, default="", null=True, blank=True)
    description = models.TextField(default="", null=True, blank=True)

    def __str__(self):
        return f'{self.id} - {self.name}'


class SubCategory(models.Model):

    """class to store details of subcategory"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="sub_categories")
    name = models.CharField(max_length=150, default="", null=True, blank=True)
    description = models.TextField(default="", null=True, blank=True)

    def __str__(self):
        return f'{self.id} -{self.name}- {self.category.name}'


class BaseProduct(models.Model):

    name = models.CharField(max_length=150, default="", null=True, blank=True)
    description = models.TextField(default="", null=True, blank=True)
    brand_name = models.CharField(max_length=150, default="", null=True, blank=True)
    item_unit = models.CharField(max_length=150, default="", null=True, blank=True)
    category = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE, related_name="base_product")
    stock_maintain = models.BooleanField(default=False)
    alert_qnty = models.FloatField(null=True, blank=True)


class Product(models.Model):
    """model to store details of products"""

    base_product = models.ForeignKey(
        BaseProduct, null=True, blank=True, related_name="products",
        on_delete=models.CASCADE)
    item_hsn = models.IntegerField(null=True, blank=True)
    item_code = models.IntegerField(null=True, blank=True)
    mrp = models.IntegerField(null=True, blank=True)
    buy_rate = models.FloatField(null=True, blank=True)
    sale_rate = models.FloatField(null=True, blank=True)
    dis_percentage = models.FloatField(null=True, blank=True)
    gst_percentage = models.FloatField(null=True, blank=True)
    available_qty = models.IntegerField(null=True, blank=True)
    product_expiry = models.DateField()
    variant_stock_maintain = models.BooleanField(default=False)


class ProductVariety(AbstractBase):
    """moedl to store varieties of product"""

    product = models.ForeignKey(
        Product, null=True, blank=True, related_name="varieties",
        on_delete=models.CASCADE)
    variation_name = models.CharField(
        max_length=150, default="", null=True, blank=True)
    variation_value = models.FloatField(null=True, blank=True)
    variety = models.IntegerField( null=True, blank=True)


class VarirtyImages(AbstractBase):
    """model to store images of varies"""

    variety = models.ForeignKey(
        ProductVariety, null=True, blank=True, related_name="images",
        on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')





