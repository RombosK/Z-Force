# from django.http import HttpResponse
# from django.shortcuts import render
# from django.views.generic import View
#
#
# class HelloView(View):
#     def get(self, request, *args):
#         return HttpResponse("Hello, Z-Force!")
#
#
# def check_kwargs(request, **kwargs):
#     return HttpResponse(f"kwargs:<br>{kwargs}")


from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DetailView, DeleteView, View


class ContactsView(TemplateView):
    template_name = 'mainapp/contacts.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['contacts'] = [
            {
                'city': 'Random',
                'phone': 'random',
                'email': 'zov@test.ru',
                'adress': 'random'
            },
            {
                'city': 'Москва',
                'phone': 'digital',
                'email': 'z-force@msk.ru',
                'adress': 'Красная площадь, 7, Москва, Россия'
            }
        ]
        return context_data


class IndexView(TemplateView):
    template_name = 'mainapp/index.html'


class LoginView(TemplateView):
    template_name = 'mainapp/login.html'


class ContactsPageView(TemplateView):
    template_name = "mainapp/contacts.html"
