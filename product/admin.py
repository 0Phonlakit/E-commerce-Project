from django.contrib import admin
from product.models import Product

# เปลี่ยนโครงสร้างการแสดงผลของการเก็บ Product ในส่วนของ admin จาก object item เป็น list item ตามที่ได้ list_display
class ManageProduct (admin.ModelAdmin) :
    list_display = ["name", "price", "stock", "is_trending","cpu", "gpu", "main_board", 
                    "memory", "ssd", "hard_drive", "power_supply", "cases", "cpu_cooler", "monitor"]

    # ทำให้สามารถแก้ไขข้อมูลโดยที่ไม่ต้องเข้าไปแก้ที่หน้าต่างสินค้าโดยตรง 
    list_editable = ["price", "stock", "is_trending","cpu", "gpu", "main_board", "memory", 
                     "ssd", "hard_drive", "power_supply", "cases", "cpu_cooler", "monitor"]

    # ทำให้แบ่งหน้าต่างการแสดงผลออกเป็น 5 รายการต่อ 10 หน้า
    list_per_page = 10

    # ทำการค้นหาสินค้า โดยค้นหาจากชื่อสินค้า
    search_fields = ["name"]

    # ทำการกรองข้อมูลจากช่อง is_trending
    list_filter = ["is_trending", "cpu", "gpu", "main_board", "memory", "ssd", "hard_drive", "power_supply", "monitor"]

# Register your models here.
admin.site.register(Product, ManageProduct)
