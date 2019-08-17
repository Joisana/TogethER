from django.contrib import admin

# Register your models here.


from .models import User, EscapeRoom, GoingOut


admin.site.register(User)
admin.site.register(EscapeRoom)
admin.site.register(GoingOut)