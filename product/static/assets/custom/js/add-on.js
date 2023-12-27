function login_notification() {
    alert("Login successful. Redirecting to website.");
    setTimeout(function() {
        window.location.href = "/index/"; // ทำการ redirect ไปที่หน้า index
    }, 1000); // หน่วงเวลา 1 วินาที (1000 มิลลิวินาที)
}


function register_notification() {
    alert("Registration successful. Redirecting to login page.");
    setTimeout(function() {
        window.location.href = "/login";  // ทำการ redirect ไปที่หน้า login
    }, 1000); // หน่วงเวลา 1 วินาที (1000 มิลลิวินาที)
}