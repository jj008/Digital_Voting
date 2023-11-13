from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.conf import settings
from EC_Admin.models import Voters
import requests

# Create your views here.
def home(request):
    return render(request, 'index.html')


def login(request):
    if (request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        loginas = request.POST['loginas']
        if loginas == "voter":
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_superuser == False:
                auth.login(request, user)
                request.session['v_id'] = username
                return redirect('vhome')
            else:
                messages.info(request, 'Invalid Credentials')
                return render(request, 'index.html')
        elif loginas == "admin":
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_superuser == True:
                auth.login(request, user)
                request.session['admin_id'] = username
                return redirect('adminhome')
            else:
                messages.info(request, 'Invalid Credentials')
                return render(request, 'index.html')
        else:
            return render(request, 'index.html')


def registervidpage(request):
    return render(request, 'registervid.html')


def forgotpassword(request):
    return render(request, 'forgotpassword.html')


def forgot_password(request):
    if request.method == "POST":
        forgot_password.voter_id = request.POST['vid']
        voter = User.objects.get(username=forgot_password.voter_id)
        if voter is not None:
            v = Voters.objects.get(voterid_no=forgot_password.voter_id)
            vmobno = str(v.mobile_no)
            url = "http://2factor.in/API/V1/" + settings.TWO_FACTOR_API_KEY + "/SMS/" + vmobno + "/AUTOGEN"
            response = requests.request("GET", url)
            data = response.json()
            request.session['otp_session_data'] = data['Details']
            messages.info(request, 'an OTP has been sent to registered mobile number ending with')
            mobno = vmobno[6:]
            return render(request, 'forgotpassotp.html', {'mno': mobno})
        else:
            messages.info(request, 'Invalid Voter ID')
            return render(request, 'forgotpassword.html')


def forgotpassotp(request):
    if (request.method == "POST"):
        userotp = request.POST['otp']
        url = "http://2factor.in/API/V1/" + settings.TWO_FACTOR_API_KEY + "/SMS/VERIFY/" + request.session['otp_session_data'] + "/" + userotp
        response = requests.request("GET", url)
        data = response.json()
        if data['Status'] == "Success":
            return render(request, 'newpassword.html')
        else:
            messages.info(request, 'Invalid OTP')
            return render(request, 'forgotpassotp.html')


def setnewpassword(request):
    if request.method == "POST":
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            u = User.objects.get(username=forgot_password.voter_id)
            if u is not None:
                u.set_password(password1)
                u.save()
                messages.info(request, 'New password updated')
                return render(request, 'index.html')


def logout(request):
    auth.logout(request)
    return redirect('/')