from django.db import models
from django.contrib.auth.models import User
from product.models import Product

# Create your models here.
class Cart (models.Model) :
    cart_id = models.CharField(max_length=200, blank=True, null=True)

    # เชื่อมความสัมพันธ์ระหว่าง customer กับ User (เป็นการระบุว่า cart นี้ เป็นของ user คนใด)
    # CASCADE ในกรณีที่ต้องการลบสินค้าออกจากฐานข้อมูลต้องตรวจสอบว่าไม่ได้เชื่อมไปถึง user ก่อนจะลบข้อมูลออกจาก cart
    # default ให้ค่าเริ่มต้น cart ของ customer แต่ละคนไม่มีสินค้า
    customer = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

class CartItem (models.Model) :
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    # ฟังก์ชันการคำนวนราคารวมสินค้าใน 1 ชิ้น Ex Pen = 30 B. ต้องการซื้อ Pen 3 ชิ้น = 30x3 = 90 B.
    def sub_total (self) :
        return self.product.price * self.quantity

    # เช็คสินค้าที่หยิบและจำนวนสินค้าที่หยิบ
    def __str__ (self):
        return self.product.name + " : " + str(self.quantity)