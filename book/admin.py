from django.contrib import admin

# Register your models here.
#from book.models import User
#admin.site.register(User)


from django.contrib.auth.models import User

from django.contrib.auth.admin import UserAdmin 
from book.models import UserProfile
 
class UserProfileInline(admin.StackedInline):
    """ As you are noticed your profile will be edited as inline form """
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'userprofile'
 
class UserAdmin(UserAdmin):
    """ Just add inlines to the original UserAdmin class """
    inlines = [UserProfileInline, ]
 

    admin.site.unregister(User)

    admin.site.register(User, UserAdmin)