from django.shortcuts import redirect, render
from HclsWebApi.models import AdminLogin, CheckLogin
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request, 'Admin/Anonymous/home.html')

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        phone = request.POST.get('phone', '')
        if CheckLogin.objects.filter(email=email).exists():
            return render(request, 'Admin/Anonymous/register.html', {'error': 'Email already exists. Please use a different email.'})

        CheckLogin.objects.create(email=email, username=username, password=password, phone=phone)
        return render(request, 'Admin/Anonymous/login.html', {'success': 'Registration successful! Please log in.'})
    return render(request, 'Admin/Anonymous/register.html')
        
    #     # Create AdminLogin record
    #     # Note: AdminType should be set based on your business logic (default to 1 for now)
    #     try:
    #         # Get the next available ID
    #         last_admin = AdminLogin.objects.order_by('-Id').first()
    #         next_id = (last_admin.Id + 1) if last_admin else 1
            
    #         AdminLogin.objects.create(
    #             Id=next_id,
    #             Name=username,
    #             Gender=gender,
    #             Password=password,
    #             Phone=phone,
    #             Email=email,
    #             Address=address,
    #             AdminType_id=1,  # Default AdminType ID
    #             Status=False
    #         )
    #         return render(request, 'Admin/Anonymous/login.html')
    #     except Exception as e:
    #         return render(request, 'Admin/Anonymous/register.html', {'error': str(e)})
    # return render(request, 'Admin/Anonymous/register.html')


def login(request):

    if request.method == "POST":

        email = request.POST.get("username")
        password = request.POST.get("password")

        try:
            admin = CheckLogin.objects.get(email=email, password=password)

            # If admin not active
            if admin.status == False:
                return render(request, "Admin/Anonymous/activate_admin.html", {"admin": admin})

            # If active
            else:
                return render(request, "Admin/ManagerialAdmin/madashboard.html")

        except CheckLogin.DoesNotExist:
            return render(request, "Admin/Anonymous/login.html", {
                "error": "Invalid Email or Password"
            })

    return render(request, "Admin/Anonymous/login.html")

def activate_admin(request, id):

    admin = CheckLogin.objects.get(id=id)

    if request.method == "POST":

        password = request.POST.get("password")

        # verify password
        if admin.password == password:

            admin.status = True
            admin.save()

            return redirect("login")

        else:
            return render(request, "Admin/Anonymous/activate_admin.html", {
                "admin": admin,
                "error": "Incorrect password"
            })

    return render(request, "Admin/Anonymous/activate_admin.html", {
        "admin": admin
    })

def dashboard(request):
    return render(request, 'Admin/MAdmin/dashboard.html')

def profile(request):
    return render(request, 'Admin/MAdmin/profile.html')

def add(request):
    return render(request, 'Admin/MAdmin/add.html')

def manage(request):
    return render(request, 'Admin/MAdmin/manage.html')

def OAdashboard(request):
    return render(request, 'Admin/OpAdmin/dashboard.html')

def OAprofile(request):
    return render(request, 'Admin/OpAdmin/profile.html')

def doctoradd(request):
    return render(request, 'Admin/OpAdmin/doctor/add.html')

def doctormanage(request):
    return render(request, 'Admin/OpAdmin/doctor/manage.html')

def helperadd(request):
    return render(request, 'Admin/OpAdmin/helper/add.html')

def helpermanage(request):
    return render(request, 'Admin/OpAdmin/helper/manage.html')

def receptionistadd(request):
    return render(request, 'Admin/OpAdmin/receptionist/add.html')    

def receptionistmanage(request):
    return render(request, 'Admin/OpAdmin/receptionist/manage.html')
