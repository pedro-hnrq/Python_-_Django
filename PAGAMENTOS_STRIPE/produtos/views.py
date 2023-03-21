from importlib.metadata import metadata
from django.shortcuts import render
from django.http.response import HttpResponse
import stripe, json
from django.conf import settings
from .models import Produto, Pedido
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

stripe.api_key = settings.STRIPE_SECRET_KEY

@csrf_exempt
def create_payment(request, id):
    produto = Produto.objects.get(id=id)

    email = json.loads(request.body)['email']
        # data = json.loads(request.data)
        # Create a PaymentIntent with the order amount and currency
    intent = stripe.PaymentIntent.create(
        amount=int(produto.preco),
        currency='BRL',
        metadata={
            'produto_id': produto.id,
            'email': email
        }
        
    )
    return JsonResponse({
     'clientSecret': intent['client_secret']
    })
    

# def create_checkout_session(request, id):
#     produto = Produto.objects.get(id = id)

#     #Verificar o domínio
#     # if settings.DEBUG:
#     YOUR_DOMAIN = "http://127.0.0.1:8000"
#     # else:
#         # Verificar e traz o ID do pagamento
#     checkout_session = stripe.checkout.Session.create(
#         line_items=[
#                 {
#                     'price_data': {
#                     'currency': 'BRL',
#                     'unit_amount': int(produto.preco),
#                         'product_data': {
#                             'name': produto.nome
#                         }

#                     },
#                     'quantity': 3,
#                 },
#             ],
#             payment_method_types=[
#                 'card',
#                 'boleto',
#             ],
#             metadata={
#                 'id_produto': produto.id,
#                 'nome': 'Henrique',
#                 'endereco': 'Rua Balviro, 778',

#             },
#             mode='payment',
#             success_url=YOUR_DOMAIN + '/sucesso',
#             cancel_url=YOUR_DOMAIN + '/erro',
#         )
#     return JsonResponse({'id': checkout_session.id})

def home(request):
    # print(stripe.api_key)
    produto = Produto.objects.get(id=2)
    return render(request, 'home.html', {'produto': produto, 'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY})

def sucesso(request):
    return HttpResponse('Sucesso!')

def erro(request):
    return HttpResponse('Erro!')

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
    
    print(event)
    
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        pedido = Pedido(produto_id=session['metadata']['id_produto'], 
                        email=session['customer_details']['email'],
                        nome=session['metadata']['nome'],
                        endereco=session['metadata']['endereco'],
                        status=event['type'])
        pedido.save()
        print(session)

    return HttpResponse(status=200)
