from django.db import models

# Create your models here.

# สร้างตารางเก็บข้อมูล Products ต่างๆ
class Product (models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    stock = models.IntegerField()
    is_trending = models.BooleanField(default=False)
    image = models.ImageField(upload_to="images", blank=True)
    cpu = models.BooleanField(default=False)
    gpu = models.BooleanField(default=False)
    main_board = models.BooleanField(default=False)
    memory = models.BooleanField(default=False)
    ssd  = models.BooleanField(default=False)
    hard_drive = models.BooleanField(default=False)
    power_supply = models.BooleanField(default=False)
    cases = models.BooleanField(default=False)
    cpu_cooler = models.BooleanField(default=False)
    monitor = models.BooleanField(default=False)

    # ดูว่าข้อมูลสินค้าที่เพิ่มไปยัง cart มีชื่อว่าอะไร (ในไฟล์ views.py ของ carts)
    def __str__ (self):
        return self.name 

    