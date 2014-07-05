from book.models import Catagory
from django import forms
from datetime import date
import warnings


class UserRegistrationForm(forms.Form):
	username = forms.CharField(max_length=200, label=("User Name:"), required=True)
	password = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30)), label=("Password:"))
	fname = forms.CharField(max_length=10, label=("First Name:"), required=True)
	lname = forms.CharField(max_length=10, label=("Last Name:"), required=True)
	emailid = forms.EmailField(max_length=100, label=("Email Address:"), required=True)
	address=forms.CharField(max_length=200, widget=forms.Textarea,label=("Address:")) 
	phone =forms.IntegerField(label=("Phone"))



class UserProfileUpdateForm(forms.Form):
	fname = forms.CharField(max_length=10, label=("First Name:"), required=True)
	lname = forms.CharField(max_length=10, label=("Last Name:"), required=True)
	emailid = forms.EmailField(max_length=100, label=("Email Address:"), required=True)
	address=forms.CharField(max_length=200, widget=forms.Textarea,label=("Address:")) 
	phone =forms.IntegerField(label=("Phone"))


class ProductForm(forms.Form):
	cname = forms.ChoiceField()
	pname = forms.CharField(max_length=300, label=("Product Name:"), required=True)
	discription = forms.CharField(max_length=500, widget=forms.Textarea,label=("Discription:"), required=True)
	price = forms.IntegerField(label=("Price:"), required=True)
	noitem = forms.IntegerField(label=("No: Of Items:"), required=True)
	photo  = forms.ImageField(required=True)

	#def __init__(self):
		#forms.Form.__init__(self)
	def __init__(self, *args, **kwargs):
          super(ProductForm, self).__init__(*args, **kwargs)
          #print "...args...",args
          #print "....kwargs.....",kwargs
          #print "fffffffffff..........self.........fffffffffffffff",self   
          catgry = Catagory.objects.all()
          cname_choice_list = []
          for catgrys in catgry:
             cname_choice_list.append((catgrys.id,catgrys.cname))
          #cname_choice_list = ((1,1),(2,2))
          #cname_choice_list = (Catagory.objects.all())
          self.fields['cname'] = forms.ChoiceField(choices = cname_choice_list)


class CatagoryForm(forms.Form):
	cname = forms.CharField(max_length=200,label=("Catagory Name:"), required=True)

class ChangePasswordForm(forms.Form):
	newpassword= forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30)), label=("New Password"))
	renewpasssword=forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30)), label=("Retype New Password"))
		
class OrderCancelForm(forms.Form):
	oname = forms.CharField(label=("Order Id:"), required=True)

class DeliveyStatusForm(forms.Form):
    deliveryid = forms.CharField(label=("User Id:"), required=True)
    status = forms.ChoiceField()#label=("Status:"))#, required=True)
    def __init__(self, *args, **kwargs):
          super(DeliveyStatusForm, self).__init__(*args, **kwargs)
          status_choice_list = ((1,"Delivered"),(0,"Not delivered"))
          self.fields['status'] = forms.ChoiceField(choices = status_choice_list)
