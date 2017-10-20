from django.contrib import admin
from .models import Post
from .models import Color
from .models import Cat

# Register your models here.
admin.site.register(Post)
admin.site.register(Color)
admin.site.register(Cat)