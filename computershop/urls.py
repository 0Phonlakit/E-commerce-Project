"""computershop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from product import views as product_views
from usersapp import views as users_views
from cart import views as cart_views
from order import views as order_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", product_views.home_page, name="Home_page"),
    path("index/", product_views.index, name='Index'),
    path("register/", users_views.register, name='Register'),
    path("login/", users_views.login, name='Login'),
    path("logout/", users_views.logout, name='Logout'),
    path("product/detail/<int:id>", product_views.product_detail, name='Product_Detail'),
    path("category/graphiccard", product_views.gpu_products, name = "GPU_Product"),
    path("category/cpu", product_views.cpu_products, name = "CPU_Product"),
    path("category/mainboard", product_views.mboard_products, name = "Main_Board_Product"),
    path("category/memory", product_views.memory_products, name = "Memory_Product"),
    path("category/ssd", product_views.ssd_products, name = "Solid_State_Drive_Product"),
    path("category/harddrive", product_views.hdrive_products, name = "Hard_Drive_Product"),
    path("category/case", product_views.cases_products, name = "Case_Product"),
    path("category/cooler", product_views.ccooler_products, name = "CPU_Cooler_Product"),
    path("category/powersupply", product_views.psupply_products, name = "Power_Supply_Product"),
    path("category/monitor", product_views.monitor_products, name = "Monitor_Product"),
    path("products/", product_views.all_product, name="All_Products"),
    path("carts/", cart_views.carts, name="Carts"),
    path("carts/addproduct/<int:product_id>", cart_views.add_product_to_cart, name= "Add_Product"),
    path("carts/removeproduct/<int:product_id>", cart_views.remove_cart, name= "Remove_Product"),
    path("order/", order_views.order, name= "Order"),
    path("orderhistory/", order_views.order_history, name="Order_History"),
    path("orderdetail/<int:order_id>", order_views.order_detail, name="Order_Detail"),
    path("product/search/", product_views.search_product, name='Search_Product'),

]

# ตั้งค่า urlpatterns เพื่อเข้าถึงไฟล์ media โดยอ้างอิงจาก MEDIA_URL และ MEDIA_ROOT
urlpatterns += static(settings.MEDIA_URL,
                      document_root = settings.MEDIA_ROOT)