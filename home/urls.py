from django.contrib import admin
from django.urls import path
from home import views

#Django admin customization
admin.site.site_title="CRUD Operations"
admin.site.site_header="Login to your admin"
admin.site.index_title="Welcome to this portal"

urlpatterns = [
    path('admin/', admin.site.urls ),
    path('',views.student_form,name="student_insert"),  #get and post request for insert operation
    path('<int:id>/',views.student_form,name="student_update"), #get and post request for update operation
    path('delete/<int:id>',views.student_delete,name="student_delete"),
    path('list/',views.student_list,name="student_list")

]