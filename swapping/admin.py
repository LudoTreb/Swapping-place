from django.contrib import admin
from .models import SwappingProduct, SwappingAddress, SwappingPlace

admin.site.register(SwappingProduct)
admin.site.register(SwappingAddress)
admin.site.register(SwappingPlace)
