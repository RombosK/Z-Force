from mainapp.forms import GiveHelpForm, GetHelpForm
import logging
import os

import requests
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic import TemplateView, View

from mainapp.forms import GiveHelpForm, GetHelpForm
from mainapp.models import GiveHelp, GetHelp, News, ProjectCategory, AllYouNeedIs


# # Контроллер страницы с анкетой
class GiveHelpView(View):
    model = GiveHelp
    form_class = GiveHelpForm

    def get(self, request):
        form = GiveHelpForm()
        return render(request, 'mainapp/give_help.html', {'form': form})

    def post(self, request):
        form = GiveHelpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/success/')  # перенаправление на страницу успешного заполнения анкеты

        return render(request, 'mainapp/success.html')


#
# # Контроллер страницы с запросом на помощь
class GetHelpView(View):
    model = GetHelp
    form_class = GetHelpForm

    def get(self, request):
        form = GetHelpForm()
        return render(request, 'mainapp/get_help.html', {'form': form})

    def post(self, request):
        form = GetHelpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/success/')  # перенаправление на страницу успешного заполнения анкеты

        return render(request, 'mainapp/get_help.html')


# # Контроллер страницы оферты
class PartnersView(TemplateView):
    template_name = 'mainapp/partners.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Партнеры'

        return context


# from mainapp.forms import RequestFormVolunteer, RequestFormCharity
# from mainapp.models import News, ProjectCategory, AllYouNeedIs, RequestVolunteer, RequestCharity

logger = logging.getLogger(__name__)

''' в list.py в class MultipleObjectMixin(ContextMixin):
 изменено значение в переменной paginate_by = 3
 для пагинации'''


# Контроллер главной страницы
class IndexView(TemplateView):
    template_name = 'mainapp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Окно в Мир'

        return context


# Контроллер страницы контактов
class ContactsView(TemplateView):
    template_name = 'mainapp/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Cвязаться с нами'
        context['contacts'] = [
            {
                'city': 'Московская область, г. Королев',
                'phone': '+7 (910)401-40-12',
                'email': 'org@fond-oknovmir.ru',
                'address': '141075, г. Королев, ул. Фрунзе, д. 12'
            }, {

                'city': 'Красноармейск',
                'phone': '777777777',
                'email': 'zov@kz.ru',
                'address': 'Field'
            }, {

                'city': 'Подольск',
                'phone': '+5555555',
                'email': 'z-red@msk.ru',
                'address': 'Square'
            }
        ]

        return context

    # Метод отправляет сообщение в ТГ админу через бота
    @staticmethod
    def send_feedback_to_email(message: str, message_from: int = None) -> None:
        # user_from = 'Anonimus'
        TOKEN = os.getenv('TOKEN')  # в .env: токен, взятый в @BotFather ТГ
        CHAT_ID = os.getenv('CHAT_ID')  # в .env: id администратора в телеге

        # URL для отправки сообщения через телеграм API
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        # Параметры запроса
        params = {
            "chat_id": CHAT_ID,  # ID чата с администратором
            "text": message,  # Текст сообщения
            "parse_mode": "HTML"  # Форматирование сообщения
        }
        # Отправляем запрос
        response = requests.get(url, params=params)
        # Проверяем статус ответа
        if response.status_code == 200:
            # Все хорошо, сообщение отправлено
            print("Message sent successfully")
        else:
            # Что-то пошло не так, сообщение не отправлено
            print("Message failed to send")
            print(response.text)
        # redirect('/home/success/')

    def post(self, *args, **kwargs):
        message_body = self.request.POST.get('message_body')
        self.send_feedback_to_email(message_body)

        return HttpResponseRedirect(reverse_lazy('mainapp:success'))


# Контроллер страницы новостей
# родитель ListView для удобства работы со страницами где нужна пагинация
class NewsView(ListView):
    paginate_by = 3
    model = News
    template_name = 'mainapp/news.html'
    context_object_name = 'object'
    extra_context = {
        'title': 'Новости',
    }


class NewsDetail(DetailView):
    model = News
    template_name = 'mainapp/news_post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        return get_object_or_404(News, slug=self.kwargs[self.slug_url_kwarg])

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)


# def listing(request):
#     contact_list = News.objects.all()
#     paginator = Paginator(contact_list, 2) # отоброжение количества новостей на странице
#
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'News.html', {'page_obj': page_obj})

# Контроллер проектов
# родитель ListView для удобства работы со страницами где нужна пагинация
class ProjectView(ListView):
    paginate_by = 3
    template_name = 'mainapp/projects.html'
    model = ProjectCategory
    context_object_name = 'object'
    extra_context = {
        'title': 'Проекты',
    }

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #
    #     context['title'] = 'Проекты'
    #     context['object'] = ProjectCategory.objects.all()
    #
    #     return context


# Контроллер нуждающихся
# родитель ListView для удобства работы со страницами где нужна пагинация
class AllYouNeedIsView(ListView):
    paginate_by = 3
    template_name = 'mainapp/allyouneedis.html'
    model = AllYouNeedIs
    context_object_name = 'object'
    extra_context = {
        'title': 'Подопечные',
    }

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #
    #     context['title'] = 'Подопечные'
    #     context['object'] = AllYouNeedIs.objects.all()
    #
    #     return context


# Контроллер страницы О нас
class AboutView(TemplateView):
    template_name = 'mainapp/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'О нас'
        return context


# Контроллер страницы пожертвований
class DonationView(TemplateView):
    template_name = 'mainapp/donation.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Сделать пожертвование'
        return context


# Контроллер страницы политики сайта
class LegalView(TemplateView):
    template_name = 'mainapp/legal.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Политика сайта'

        return context


# Контроллер страницы о персональных данных
class PersonalDataView(TemplateView):
    template_name = 'mainapp/personal_data.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Политика обработки персональных данных'

        return context


# Контроллер страницы оферты
class OfferoView(TemplateView):
    template_name = 'mainapp/offero.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Оферта добровольного пожертвования'

        return context


class LoginView(TemplateView):
    template_name = 'mainapp/login.html'


