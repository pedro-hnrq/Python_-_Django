from django.contrib import admin
from .models import Produto, Pedido


admin.site.register(Produto)
admin.site.register(Pedido)


# from django.contrib.admin.decorators import action
# import stripe
# from django.conf import settings

# stripe.api_key = settings.STRIPE_SECRET_KEY

# @admin.action(description="Reembolsar cliente")
# def reembolsar_cliente(modeladmin, request, queryset):
#     for pedido in queryset:
#         refund = stripe.Refund.create(
#             payment_intent=pedido.payment_intent,
#         )
#         if refund['status'] == 'succeeded':
#             pedido.status = "reembolsado"
#             pedido.save()

# admin.site.register(Produto)

# @admin.register(Pedido)
# class PedidoAdmin(admin.ModelAdmin):
#     list_display = ('produto', 'email', 'name', 'endereco','valor_pago', 'status')
#     list_filter = ('status',)
#     actions = [reembolsar_cliente]