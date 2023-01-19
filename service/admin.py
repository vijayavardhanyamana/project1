from django.contrib import admin
from service.models import login1
from service.models import profilepatient

class login_log(admin.ModelAdmin):
    list_display=('selectoption','fname','lname','email','password','gender')
    
class patient_profile(admin.ModelAdmin):
    list_display=('fname','lname','bloodgroup','email','gender','phone','dateofbirth','address')
    
    
    
    
    

admin.site.register(login1,login_log)
admin.site.register(profilepatient,patient_profile)
# Register your models here.
