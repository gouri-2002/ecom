
from django.contrib import admin
from store.models import Brand,Tag,Size,Category,Product
from store.models import User

admin.site.register(User)
admin.site.register(Brand)
admin.site.register(Tag)
admin.site.register(Size)
admin.site.register(Category)
admin.site.register(Product)