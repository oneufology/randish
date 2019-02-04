from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.views.generic.base import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout

# Create your views here.

class MainView(TemplateView):
    template_name = 'registration.html'

    def get(self, reguest):
        return render(reguest, self.template_name)



# Registration
class SignUpFormView(FormView):
    form_class = UserCreationForm
    success_url = "/registration/sign_in/"
    template_name = "signup.html"

    def form_valid(self, form):
        form.save()
        return super(SignUpFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(SignUpFormView, self).form_invalid(form)




# Login
class SignInFormView(FormView):
    form_class = AuthenticationForm
    success_url = "/"
    template_name = "signin.html"

    def form_valid(self, form):
        self.user = form.get_user()

        login(self.request, self.user)
        return super(SignInFormView, self).form_valid(form)


# Logout
class LogOutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/registration/")


























