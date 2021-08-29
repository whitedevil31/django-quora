from django.db.models import query
from django.shortcuts import redirect, render,reverse
from django.http import HttpResponse
from django.views import generic
from .models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import userForm,CustomUserForm
from django.contrib.auth.mixins import LoginRequiredMixin
class signupView(generic.CreateView):
    template_name='registration/signup.html'
    form_class=CustomUserForm

    def get_success_url(self):
        return reverse('login')
class userCreateView(LoginRequiredMixin,generic.CreateView):
    template_name='users/add_user.html'
    form_class=userForm
    def get_success_url(self):
        return reverse('users:user-list')

class userListView(LoginRequiredMixin,generic.ListView):
    template_name='users/display_users.html'
    queryset=User.objects.all
    context_object_name='users'
    

class userDetailView(LoginRequiredMixin,generic.DetailView):
    template_name="users/user_profile.html"
    queryset=User.objects.all()
    context_object_name='user'


class userUpdateView(LoginRequiredMixin,generic.UpdateView):
    template_name='users/user_update.html'
    queryset=User.objects.all()
    form_class=userForm
    def get_success_url(self):
        return reverse('users:user-list')
class userDeleteView(LoginRequiredMixin,generic.DeleteView):
    template_name='users/user_delete.html'
    queryset=User.objects.all()
    context_object_name='user'
    def get_success_url(self):
        return reverse('users:user-list')

# def all_users(request):
#     users = User.objects.all()
#     context={
#         'users':users
#     }
#     return render(request,'users/display_users.html',context)

# def user_profile(request,pk ):
#     user = User.objects.get(id=pk)
#     context={
#         'user':user
#     }
#     return render(request,'users/user_profile.html',context)

# def create_user(request):
#     form = userForm()
#     if request.method=="POST":
#         form=userForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/users')
#     context={
#         'form':form 
#         }
#     return render(request,'users/create_user.html',context)

# def update_user(request,pk):
#     user = User.objects.get(id=pk)
#     form=userForm(instance=user)
#     if request.method=="POST":
#         form=userForm(request.POST,instance=user)
#         if form.is_valid():
#             form.save()
#             return redirect('/users')

#     context={
#         'user':user,
#         'form':form
#     }
#     return render(request,'users/user_update.html',context)



# def delete_user(request,pk):
#     user = User.objects.get(id=pk)
#     user.delete()
#     return redirect('/users')

# def lead_create(request):
#     form=userForm()
#     if request.method =='POST':
#         if form.is_valid():
#             field1 = form.cleaned_data['field1']
#             field2 = form.cleaned_data['field2']
#             User.objects.create(field1,field2)
#             return redirect('/home')

#     context={"form":form}
#     return render(request,'/xuab/fkndk.html')
