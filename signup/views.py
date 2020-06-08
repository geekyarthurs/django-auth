from django.shortcuts import render
from django.views import View
from .forms import BaseForm, ExtendedForm


class SignupPage(View):
    def get(self, request):

        context = {
            'baseform': BaseForm(),
            'extendedform': ExtendedForm(),
        }

        return render(request, "signup.html", context)

    def post(self, request):

        baseform = BaseForm(request.POST)
        extendedform = ExtendedForm(request.POST)

        if baseform.is_valid() and extendedform.is_valid():
            user = baseform.save()
            user.set_password(user.password)
            user.save()

            extendeduser = extendedform.save(commit=False)
            extendeduser.user = user
            extendeduser.save()

            return render(request, "signup.html")

        else:
            context = {'baseform': baseform, 'extendedform': extendedform}
            return render(request, "signup.html", context)
