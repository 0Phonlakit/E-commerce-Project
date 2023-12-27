from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from product.models import Product 
# Create your views here.

# สร้างหน้า home page

def home_page (request) :
    return render(request, "home-page.html")

def index (request):
    
    # ดึงข้อมูลจากตาราง Product ในช่อง is_trending มาใช้
    is_product = Product.objects.filter(is_trending=True)

    # {"product" : is_product} จะดึงข้อมูลจาก is_product เพื่อไปใช้ใน html โดยอ้างอิงจาก trending_product
    return render(request, "index.html", {"trending_product" : is_product} )

def product_detail (request, id) :

    # ดึงข้อรายการสินค้าแค่ 1 ชิ้นตาม id
    product_details = Product.objects.get(pk=id)
    return render(request, "details.html", {"product_details" : product_details})

def all_product (request) :

    # ดึงข้อมูลทั้งหมดจากฐานข้อมูลมาใช้ โดยข้อมูลมาจาก admin 
    # .order_by เป็นฟังก์ชันไว้สำหรับจัดเรียงสินค้า โดยอิงจากชื่อสินค้า a-z 
    all_products = Product.objects.all().order_by("name")

    # Paginater เป็นฟังก์ชันควบคุมการแสดงผลข้อมูลสินค้า
    page = request.GET.get("page")

    # เลข 6 หมายถึง 1 หน้าเว็บไซต์แสดงข้อมูลสินค้า 6 ชิ้น
    paginator = Paginator(all_products, 6)
    all_products = paginator.get_page(page) 

    # {"all_products" : all_products} จะดึงข้อมูลจาก all_products เพื่อไปใช้ใน html โดยอ้างอิงจาก all_products
    return render(request, "products.html", {"all_products" : all_products})

def cpu_products (request):
    
    # ดึงข้อมูลจากตาราง Product ในช่อง is_trending มาใช้
    is_cpu = Product.objects.filter(cpu=True)

    # {"product" : is_cpu} จะดึงข้อมูลจาก is_cpu เพื่อไปใช้ใน html โดยอ้างอิงจาก cpu_product
    return render(request, "cpu_product.html", {"cpu_product" : is_cpu} )

def gpu_products (request):
    is_gpu = Product.objects.filter(gpu=True)
    return render(request, "gpu_product.html", {"gpu_product" : is_gpu} )

def mboard_products (request):
    is_mboard = Product.objects.filter(main_board=True)
    return render(request, "main_board_product.html", {"mboard_product" : is_mboard} )

def memory_products (request):
    is_memory = Product.objects.filter(memory=True)
    return render(request, "memory_product.html", {"memory_product" : is_memory} )

def ssd_products (request):
    is_ssd = Product.objects.filter(ssd=True)
    return render(request, "ssd_product.html", {"ssd_product" : is_ssd} )

def hdrive_products (request):
    is_hdrive = Product.objects.filter(hard_drive=True)
    return render(request, "hard_drive_product.html", {"hdrive_product" : is_hdrive} )

def psupply_products (request):
    is_psupply = Product.objects.filter(power_supply=True)
    return render(request, "power_supply_product.html", {"psupply_product" : is_psupply} )

def cases_products (request):
    is_case = Product.objects.filter(cases=True)
    return render(request, "case_product.html", {"case_product" : is_case} )

def ccooler_products (request):
    is_cooler = Product.objects.filter(cpu_cooler=True)
    return render(request, "cpu_cooler_product.html", {"cpu_cooler_product" : is_cooler} )

def monitor_products (request):
    is_monitor = Product.objects.filter(monitor=True)
    return render(request, "monitor_product.html", {"monitor_product" : is_monitor} )

def search_product(request):
    # ดึงชื่อสินค้าจาก query parameter
    product_name = request.GET.get('name', None)

    try:
        # ดึงข้อมูลสินค้าตามชื่อ
        search_product = Product.objects.get(name=product_name)

        # ส่งข้อมูลสินค้าไปยังเทมเพลต
        return render(request, "searchs.html", {"search_product": search_product})

    except Product.DoesNotExist:
        # หากไม่พบสินค้าจะทำการ handle ได้ตามต้องการ
        return render(request, "not_found.html")


