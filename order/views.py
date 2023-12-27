from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.models import Cart, CartItem
from order.models import Order, OrderDetail
from product.models import Product
from cart.views import create_cart_id 

# Create your views here.

@login_required(login_url="/login")
def order (request) :
    # ใบสั่งซื้อสินค้า
    if request.method == "POST" :
        # POST จะรับข้อมูลจาก user ไปเก็บในฐานข้อมุล
        phone = request.POST["phone"]
        address = request.POST["address"]

        # ดึงข้อมูล cart ที่อิงจาก cart_id มาใช้
        cart = Cart.objects.get(cart_id=create_cart_id(request), customer=request.user)

        # ค้นหาสินค้าใน cart ถ้ามีให้นำสินค้าราคาสินค้ามารวมแล้วเก็บใน total
        cart_Item = CartItem.objects.filter(cart=cart)
        total=0

        for item in cart_Item :
            total += (item.product.price * item.quantity)

        # ฟังก์ชันสร้าง Order
        order = Order.objects.create(
            first_name = request.user.first_name,
            last_name =  request.user.last_name,
            phone=phone,
            address=address,
            total=total,
            customer=request.user,
        )

        order.save()

        # บันทึก order และทำการตัดสินค้าที่ซื้อสำเร็จ
        for item in cart_Item:
            order_detail = OrderDetail.objects.create(
                product = item.product.name,
                quantity = item.quantity,
                price = item.product.price,
                order = order
            )
        
            order_detail.save()

            # ตัดสินค้าออกจาก stock
            product = Product.objects.get(pk=item.product.id)
            product.stock = int(item.product.stock - order_detail.quantity)
            product.save()

            # ลบสินค้าออกจาก cart เมื่อซื้อสินค้าเสร็จสิ้น
            item.delete()

        #ลบ cart
        cart.delete()
        return render(request, "ordercomplete.html")
    
    else :
        return render(request, "order.html")

@login_required(login_url="/login") 
def order_history (request) :
    orders = Order.objects.filter( customer = request.user )
    return render (request, "order_history.html", {"orders" : orders})

@login_required(login_url="/login") 
def order_detail (request, order_id):
    order = Order.objects.get(pk=order_id)
    if order.customer==request.user :
        order_items = OrderDetail.objects.filter(order=order)
        return render (request, "orderdetails.html", {"order" : order, "order_items" : order_items})
    else :
        return redirect ("/orderhistory")