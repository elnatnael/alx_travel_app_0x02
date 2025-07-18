import requests
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Payment
import uuid

@api_view(['POST'])
def initiate_payment(request):
    amount = request.data.get('amount')
    booking_reference = str(uuid.uuid4())
    
    data = {
        "amount": amount,
        "currency": "ETB",
        "email": request.data.get('email'),
        "tx_ref": booking_reference,
        "callback_url": "http://your-domain.com/payment/verify/",
        "return_url": "http://your-domain.com/payment/return/",
        "customization[title]": "Booking Payment"
    }

    headers = {
        "Authorization": f"Bearer {settings.CHAPA_SECRET_KEY}"
    }

    response = requests.post("https://api.chapa.co/v1/transaction/initialize", json=data, headers=headers)
    res_data = response.json()

    if response.status_code == 200 and res_data.get("status") == "success":
        Payment.objects.create(
            booking_reference=booking_reference,
            amount=amount,
            transaction_id=res_data['data']['tx_ref'],
            status='Pending'
        )
        return Response({
            "checkout_url": res_data['data']['checkout_url'],
            "booking_reference": booking_reference
        })
    else:
        return Response(res_data, status=400)

@api_view(['GET'])
def verify_payment(request, tx_ref):
    url = f"https://api.chapa.co/v1/transaction/verify/{tx_ref}"
    headers = {
        "Authorization": f"Bearer {settings.CHAPA_SECRET_KEY}"
    }
    response = requests.get(url, headers=headers)
    res_data = response.json()

    try:
        payment = Payment.objects.get(transaction_id=tx_ref)
        if res_data["status"] == "success" and res_data["data"]["status"] == "success":
            payment.status = "Completed"
        else:
            payment.status = "Failed"
        payment.save()
        return Response({"status": payment.status})
    except Payment.DoesNotExist:
        return Response({"error": "Payment not found"}, status=404)
