from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.conf import settings
from accounts.models import Account
from django.utils.html import mark_safe
from store.models import Product
from django.utils import timezone
from decimal import Decimal
import uuid

class HomeLogo(models.Model):
    logo = models.ImageField(upload_to='logos')

    def __str__(self):
        return str(self.id)

class Pattern(models.Model):
    image = models.ImageField(upload_to='patterns')
    def __str__(self):
        return str(self.id)

class Designs(models.Model):
    image = models.ImageField(upload_to='designs')

    def __str__(self):
        return str(self.id)


class Tags(models.Model):
    name=models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.name

class FooterLink(models.Model):
    title=models.CharField(max_length=255)
    fontClass=models.CharField(max_length=255)
    link=models.CharField(max_length=255)
    allClasses=models.TextField(default='fb, googlePlus, pintrest, linkedin, insta, youtube, tiktok,tw')

    def __str__(self):
        return self.title

class CustomColor(models.Model):
    color=models.CharField(max_length=20)

    def __str__(self):
        return self.color

class CustomFonts(models.Model):
    font_name = models.CharField(max_length=255)
    font_file = models.FileField(upload_to='fonts/')

    def __str__(self):
        return self.font_name

class CustomLogos(models.Model):
    image = models.ImageField(upload_to="photos/custom_logos")

    def img_preview(self): #new
        return mark_safe(f'<img src = "{self.image.url}" width = "300"/>')

    def __str__(self):
        return self.image.url




class CustomProduct(models.Model):
    product_name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)  # Add slug field
    description = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.IntegerField(default=0)
    custom_text = models.CharField(max_length=200, blank=True, null=True)  # Field for custom text
    custom_logo = models.ImageField(upload_to='photos/logos/', blank=True, null=True)  # Field for custom logo
    images = models.ImageField(upload_to='photos/custom_products')
    images_hover = models.ImageField(upload_to='photos/custom_products_hover')
    images_three = models.ImageField(upload_to='photos/custom_products_hover')
    images_four = models.ImageField(upload_to='photos/custom_products_hover')
    images_five = models.ImageField(upload_to='photos/custom_products_hover')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_order_url(self):
        return reverse('order_product', args=[self.slug])

    def save(self, *args, **kwargs):
        # Generate slug before saving
        if not self.slug:
            self.slug = slugify(self.product_name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('custom_product_detail', args=[self.slug])

    def __str__(self):
        return self.product_name


class VariationManager_Custom(models.Manager):
    def colors(self):
        return super(VariationManager_Custom, self).filter(variation_category='color', is_active=True)

    def sizes(self):
        return super(VariationManager_Custom, self).filter(variation_category='size', is_active=True)


variation_category_choise_Custom = (
        ('color', 'color'),
        ('size', 'size'),
    )


class Variation_Custom(models.Model):
    product = models.ForeignKey(CustomProduct, on_delete=models.CASCADE)
    variation_category = models.CharField(max_length=100, choices=variation_category_choise_Custom)
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_date = models.DateField(auto_now=True)

    objects = VariationManager_Custom()

    def __str__(self):
        return self.variation_value



class ProductGallery_Custom(models.Model):
    product = models.ForeignKey(CustomProduct, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='store/custom_products/', max_length=255)

    def __str__(self):
        return self.product.product_name

    class Meta:
        verbose_name = 'productgallery'
        verbose_name_plural = 'product gallery'


class Cart_Custom(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id



class CartItem_Custom(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    custom_product = models.ForeignKey(CustomProduct, on_delete=models.CASCADE)
    variations = models.ManyToManyField(Variation_Custom, blank=True)
    cart = models.ForeignKey(Cart_Custom, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return str(self.custom_product)




class CustomOrder(models.Model):
    STATUS = (
        ("New", "New"),
        ("Accepted", "Accepted"),
        ("Completed", "Completed"),
        ("Cancelled", "Cancelled"),
    )
    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(CustomProduct, on_delete=models.CASCADE)
    sizes_s= models.IntegerField(default=0)
    sizes_m= models.IntegerField(default=0)
    sizes_l= models.IntegerField(default=0)
    sizes_xl= models.IntegerField(default=0)
    sizes_xxl= models.IntegerField(default=0)
    sizes_xxxl= models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    stuff = models.FileField(upload_to='custom_stuff', max_length = 100)
    order_number = models.CharField(max_length=255, unique=True, blank=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    address_line_1 = models.CharField(max_length=50)
    address_line_2 = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    order_note = models.TextField(blank=True)
    order_total = models.FloatField()
    tax = models.FloatField()
    status = models.CharField(max_length=10, choices=STATUS, default="New")
    ip = models.CharField(max_length=20, blank=True)
    is_ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def full_address(self):
        return f"{self.address_line_1} {self.address_line_2}"

    def calculate_total_price(self):
        # Assuming the product price is stored in the CustomProduct model
        # and is accessible via the product field in the CustomOrder model
        total_price = self.product.price * self.quantity
        return total_price

    def save(self, *args, **kwargs):
    # Debugging: Print sizes values
        print(f"Sizes S: {self.sizes_s}, M: {self.sizes_m}, L: {self.sizes_l}, XL: {self.sizes_xl}, XXL: {self.sizes_xxl}, XXXL: {self.sizes_xxxl}")

        # Calculate the total quantity based on the sizes
        self.quantity = (
            self.sizes_s +
            self.sizes_m +
            self.sizes_l +
            self.sizes_xl +
            self.sizes_xxl +
            self.sizes_xxxl
        )

        print(f"Total Quantity: {self.quantity}")  # Debugging: Print calculated quantity

        # Ensure order number is generated only once
        if not self.order_number:
            self.order_number = f"{timezone.now().strftime('%Y%m%d')}-{uuid.uuid4().hex[:8]}"

        # Calculate the tax (2%) and total order amount
        tax_rate = Decimal('0.02')
        self.tax = self.product.price * tax_rate * self.quantity
        self.order_total = self.product.price * self.quantity + self.tax

        # Call the parent class's save method to ensure the object is saved
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number




