from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from product.models import Product
from cart.models import Cart, CartItem
# Create your views here.

def create_cart_id (request) :
    
    # เป็นฟังก์ชันที่เรียกใช้ cart สำหรับ user ที่ login แล้วใน cart มีสินค้าก็จะนำสินค้าใน cart ที่เพื่มมาแล้วถูก backup มาใส่ใน cart
    cart = request.session.session_key

    # หาก user เพิ่ม register จะสร้าง cart เปล่าขึ้นมา 
    if not cart :
        cart = request.session.create()
    return cart

# เป็นฟังก์ชันในการตรวจสอบว่า user ต้อง login ก่อนถึงจะเพิ่มสินค้าลง cart ได้
@login_required(login_url="/login")
def carts (request) :
    amount = 0
    total = 0

    # เป็นตัวคำนวนจำนวนสินค้า และราคาสินค้า
    try :

        # ดึงข้อมูล cart_id 
        cart = Cart.objects.get(cart_id=create_cart_id(request), customer=request.user)

        # ดึงข้อมูล product ใน cart 
        cart_Item = CartItem.objects.filter(cart=cart)
        for item in cart_Item :
            amount += item.quantity
            total += (item.product.price * item.quantity)

    except  (Cart.DoesNotExist, CartItem.DoesNotExist) :
        cart = None
        cart_Item = None 

    return render(request, "carts.html", {"cart_Item" : cart_Item, "total" : total, "amount" : amount})

@login_required(login_url="/login")
def add_product_to_cart (request, product_id) :

    # เพิ่มสินค้าลงใน cart ได้ต้อง login ก่อน
    add_product = Product.objects.get(pk = product_id) 

    # เป็นตัวตรวจสอบว่าภายใน cart ของ user มีสินค้าหรือไม่
    try :
        # หากเคยมีสินค้าอยู่ใน cart จะ ถูกเรียกใช้ผ่าน session แล้วข้อมูลสินค้าจะถูก restore
        cart = Cart.objects.get(cart_id=create_cart_id(request))
    except Cart.DoesNotExist :
        # หากไม่มีสินค้าอยู่ใน cart จะทำการเก็บ cart_id และ customer ไว้ใน cart
        cart = Cart.objects.create(
            cart_id = create_cart_id(request),
            customer = request.user
        )
        cart.save()

    # เป็นตัวตรวจสอบว่า user มีการเพิ่มสินค้าใหม่หรือหยิบสินค้าเดิม
    try :

        # หาก user มีสินค้าอยู่แล้ว และต้องการซื้อเพิ่มเป็น 2 ชิ้น ก็จะนำข้อมูลสินค้าเก่าไปเพิ่มกับข้อมูลสินค้าใหม่
        cart_item =CartItem.objects.get(product = add_product, cart = cart)

        # เช็คว่าสินค้าที่ user เพิ่มลง cart ยังมีเหลือใน stock หรือไม่
        if cart_item.quantity < cart_item.product.stock :
            cart_item.quantity += 1
            cart_item.save()

    # หากหยิบสินค้าใหม่ให้ทำการเพิ่มข้อมูลสินค้าลงใน cart และให้จำนวนสินค้า (quantity) เป็น 1 
    except CartItem.DoesNotExist :
        cart_item = CartItem.objects.create(
            product = add_product,
            cart = cart,
            quantity = 1
        )
        cart_item.save()
    # เช็คสินค้าที่หยิบและจำนวนสินค้าที่หยิบ ใน terminal  
    #print(cart_item)
    return redirect("/carts") 

@login_required(login_url="/login")
def remove_cart (request, product_id) :

    # รับ input เกี่ยวกับการลบสินค้าจาก users
    cart = Cart.objects.get(cart_id=create_cart_id(request), customer=request.user)

    # ตรวจสอบว่าใน cart มี id สินค้าที่ต้องการลบอยู่ตำแหน่งใด
    product = Product.objects.get(pk=product_id)

    # สินค้าที่ต้องการลบใน cart
    cart_item = CartItem.objects.get(product=product, cart=cart)

    # ลบสินค้าออกจาก cart
    cart_item.delete()
    return redirect("/carts")