from django.http.response import HttpResponse
from django.shortcuts import render
import stripe
from django.conf import settings
from .models import Produto, Pedido
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.messages import constants

stripe.api_key = settings.STRIPE_SECRET_KEY 

@csrf_exempt
def create_payment(request, id):
    produto = Produto.objects.get(id=id)
    
    # Create a PaymentIntent with the order amount and currency
    intent = stripe.PaymentIntent.create(
        amount=int(produto.preco),
        currency='BRL',
        
        )
    return JsonResponse({
            'clientSecret': intent['client_secret']
        })
    
    
def home(request):
    produto = Produto.objects.get(id=3)
    # produto = Produto.objects.all()
    # all_produt = { 'produt':produt }
    return render(request, 'home.html', {'produto':produto, 'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY})

def sucesso(request):
    messages.add_message(request, constants.SUCCESS, 'Pagamento confiamado com Sucesso!')
    return render(request, 'sucesso.html')

def erro (request):
    messages.add_message(request, constants.ERROR, 'Erro na procedimento de pagamento')
    return render(request, 'erro.html')


# @csrf_exempt
# def stripe_webhook(request):
#   payload = request.body

#   # For now, you only need to print out the webhook payload so you can see
#   # the structure.
#   print(payload)

#   return HttpResponse(status=200)

# @csrf_exempt= isento de verificação ou validação.
@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None
    endpoint_secret = settings.STRIPE_WEBHOOK_SECRET

    try:
        event = stripe.Webhook.construct_event(
        payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)
    
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object'] 
        print(session)       
        pedido = Pedido(produto_id=session['metadata']['id_produto'], 
                        email=session['customer_detail']['email'],
                        nome=session['metadata']['nome'],
                        status=event['type'])
        pedido.save()
        
    # print(event)
    return HttpResponse(status=200)

