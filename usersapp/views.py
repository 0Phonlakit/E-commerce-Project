from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

def register (request) :

    #ตรวจสอบว่าข้อมูลที่ส่งมา ได้จาก POST method ไหม
    if request.method == "POST" :

        # นำค่าที่ได้จากหน้า register.html ที่ได้มาเก็บ
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password1"]
        chack_password = request.POST["password2"]
        first_name = request.POST["firstname"]
        last_name = request.POST["lastname"]

        # ตรวจสอบเงื่อนไขต่างๆ
        if email == "" :

            # ข้อความจะปรากฎขึ้นเมื่อ user ไม่ได้กรอก email
            messages.warning(request, "Please fill out this email.")

            # กลับไปหน้า register
            return redirect("/register") 
        
        if username== "" :
            messages.warning(request, "Please fill out this username.")
            return redirect("/register")      
        if first_name== "" :
            messages.warning(request, "Please fill out this first name.")
            return redirect("/register")
        if last_name== "" :
            messages.warning(request, "Please fill out this last name.")
            return redirect("/register")                                    
        if password == "" :
            messages.warning(request, "Please fill out this password.")
            return redirect("/register")
        if chack_password =="" :
            messages.warning(request, "Please fill out this confirm password.")
            return redirect("/register")
        if password != chack_password :
            messages.warning(request, "The password and confirmation password must match.")
            return redirect("/register")
        else : 

            # เช็คว่าในฐานข้อมูลมี username ซ้ำกันหรือไม่
            if User.objects.filter(username=username).exists():
                messages.warning(request, "The username is already in use.")
                return redirect("/register")
            else :
                
                # เก็บข้อมูล user ในฐานข้อมูลของ admin
                user = User.objects.create_user(
                    email=email,
                    username=username,
                    password= password,
                    first_name = first_name,
                    last_name = last_name,
                )
                user.save()
                messages.success(request, "Account creation successful.")
                return render(request, 'register.html', {'register_complete': True})
    else :
        return render (request, "register.html")

def login (request) :

     #ตรวจสอบว่าข้อมูลที่ส่งมา ได้จาก POST method ไหม
    if request.method == "POST" :
        username = request.POST["username"]
        password = request.POST["password"]

        # ตรวจสอบเงื่อนไขต่างๆ
        if username== "" or password =="" :

            # ข้อความจะปรากฎขึ้นเมื่อ user ไม่ได้กรอก username และ password
            messages.warning(request, "Your username or password is incorrect. Please check and try again.")

            # กลับไปหน้า login
            return redirect("/login")
        else :

            # authenticate method เป็นฟังก์ชันที่จะนำข้อมูล user ที่กรอกไปตรวจสอบในฐานข้อมูล
            user = auth.authenticate(username=username, password=password)

            # ถ้าตรวจสอบแล้วว่าในฐานข้อมูลมี username และ password ก็จะเข้าสู่ระบบ
            if user is not None :
                auth.login(request, user)
                messages.success(request, "You have successfully logged in.")
                return render(request, 'login.html', {'login_complete': True})
            
            # ถ้าตรวจสอบแล้วว่า user กรอกข้อมูลครบแต่ข้อมูลนั้นไม่มีในฐานข้อมุล
            else :
                messages.warning(request, "Your username or password is incorrect. Please check and try again.")
                return redirect("/login")
    else :
        return render (request, "login.html")

def logout (request) :
    auth.logout(request)
    return redirect ("/")