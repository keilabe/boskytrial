import json
from django.http import HttpResponse
import requests
from requests.auth import HTTPBasicAuth
from myapp.credentials import MpesaC2bCredential, MpesaAccessToken, LipanaMpesaPpassword
from django.shortcuts import render, redirect
from myapp.models import User, Destinations
from myapp.forms import DestinationForm


# Create your views here.
def login(request):
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        user = User(firstname=request.POST['firstname'], lastname=request.POST['lastname'],
                    username=request.POST['username'], email=request.POST['email'], password=request.POST['password'])
        user.save()
        return redirect('/')
    else:
        return render(request, 'register.html')


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def services(request):
    return render(request, 'services.html')


def testimonials(request):
    return render(request, 'testimonials.html')


def rsv1(request):
    return render(request, 'reservation1.html')


def rsv2(request):
    return render(request, 'reservation2.html')


def rsv3(request):
    return render(request, 'reservation3.html')


# nyd to mean new year details
def nyd(request):
    return render(request, 'newyeardeals.html')


# vln to mean valentine details
def vln(request):
    return render(request, 'valentinedeals.html')


def est(request):
    return render(request, 'easterdeals.html')


def lbd(request):
    return render(request, 'labordeals.html')


def mad(request):
    return render(request, 'madarakadeals.html')


def hud(request):
    return render(request, 'hudumadaydeals.html')


def jam(request):
    return render(request, 'Jamhuri.html')


def mash(request):
    return render(request, 'mashujaa.html')


def xmas(request):
    return render(request, 'christmas.html')


# hdl to mean holiday details
# holiday-detailsmhk to mean holiday-details of mountain hike category
# holiday-detailssb to mean holiday-details of sandy beaches category
# holiday-detailswld to mean holiday-details of wild category
def hdl1(request):
    return render(request, 'holiday-detailsmhk1.html')


def hdl2(request):
    return render(request, 'holiday-detailsmhk2.html')


def hdl3(request):
    return render(request, 'holiday-detailsmhk3.html')


def hdl4(request):
    return render(request, 'holiday-detailssb1.html')


def hdl5(request):
    return render(request, 'holiday-detailssb2.html')


def hdl6(request):
    return render(request, 'holiday-detailssb3.html')


def hdl7(request):
    return render(request, 'holiday-detailswld1.html')


def hdl8(request):
    return render(request, 'holiday-detailswld2.html')


def hdl9(request):
    return render(request, 'holiday-detailswld3.html')


def book(request):
    return render(request, 'Reservation.html')


def kesafaris(request):
    return render(request, 'Kenyasafaris.html')


def tzsafaris(request):
    return render(request, 'Tzsafaris.html')


def Ugsafaris(request):
    return render(request, 'Ugsafaris.html')


def Rwsafaris(request):
    return render(request, 'Rwandasafaris.html')


def pay(request):
    return render(request, 'pay.html.html')


def proposal(request):
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/proposal')
    else:
        form = DestinationForm()
        return render(request, 'proposals.html', {'form': form})


def delete(request, id):
    destination = Destinations.objects.get(id=id)
    destination.delete()
    return redirect('/show')


def edit(request, id):
    destination = Destinations.objects.get(id=id)
    return render(request, 'edit.html', {'destination': destination})


def show(request):
    destinations = Destinations.objects.all()
    return render(request, 'show.html')


def token(request):
    consumer_key = 'yW35kAbwReh5gtEsfdFpoJ9erzlznpCe'
    consumer_secret = '2eLxwvqPTaA9mNNM'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token": validated_mpesa_access_token})


def stk(request):
    if request.method == "POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "Wunderkind Co.",
            "TransactionDesc": "Web Development Charges"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse(response)
