from django.contrib import admin
from accounts.models import User, Technology, IntermediateUserTech

# Register your models here.

admin.site.register(User)
admin.site.register(Technology)
admin.site.register(IntermediateUserTech)
