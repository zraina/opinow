from django.contrib import admin
from .models import Pano
from .models import Tour
from .models import Scene

# Register your models here.
admin.site.register(Pano)
admin.site.register(Tour)
admin.site.register(Scene)
