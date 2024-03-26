import asyncio

import aiohttp

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
from mainapp.models import GiveHelp, GetHelp, News, ProjectCategory, AllYouNeedIs, Partners, Project, Report, \
    ReportYear, Images, ImagesProject, ImagesAllYouNeedIs


# # Контроллер страницы с анкетой
# class GiveHelpView(View):
#     model = GiveHelp
#     form_class = GiveHelpForm
#
#     def get(self, request):
#         form = GiveHelpForm()
#         return render(request, 'mainapp/give_help.html', {'form': form})
#
#     def post(self, request):
#         form = GiveHelpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/home/success/')  # перенаправление на страницу успешного заполнения анкеты
#
#         # return render(request, 'mainapp/success.html')
#         return render(request, 'mainapp/get_help.html', {'form': form})

class GiveHelpView(View):
    model = GiveHelp
    form_class = GiveHelpForm

    def get(self, request):
        form = GiveHelpForm()
        return render(request, 'mainapp/give_help.html', {'form': form})

    def post(self, request):
        form = GiveHelpForm(request.POST)
        if form.is_valid():
            # Проверяем, было ли отмечено согласие
            if form.cleaned_data['agreement']:
                form.save()
                return redirect('/home/success/')  # перенаправление на страницу успешного заполнения анкеты
            else:
                # Если согласие не было отмечено, добавляем сообщение об ошибке
                form.add_error('agreement', 'Пожалуйста, подтвердите свое согласие.')
        return render(request, 'mainapp/give_help.html', {'form': form})


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

        # return render(request, 'mainapp/get_help.html')
        return render(request, 'mainapp/get_help.html', {'form': form})


# # Контроллер страницы оферты
class PartnersView(ListView):
    model = Partners
    template_name = 'mainapp/partners.html'
    context_object_name = 'object'
    extra_context = {
        'title': 'Партнеры',
    }


logger = logging.getLogger(__name__)


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
                'map': 'https://yandex.ru/map-widget/v1/-/CDF44O-k',
                'city': 'МО, Королёв',
                'phone': '+7 (910)401-40-12',
                'email': 'org@fond-oknovmir.ru',
                'address': 'ул. Фрунзе 12',
                'manager': 'Шаройко Ольга Павловна'
            },
            {
                'map': 'https://yandex.ru/map-widget/v1/-/CDFaQOn3',
                'city': 'МО, Красноармейск',
                'phone': '+7(916)011-81-12',
                'email': 'krasnodobro@mail.ru',
                'address': 'пр. Испытателей 25/2',
                'manager': 'Березикова Ирина Владимировна'
            }, {

                'map': 'https://yandex.ru/map-widget/v1/-/CDFaQD-O',
                'city': 'МО, Подольск',
                'phone': '+7(910)000-78-52',
                'email': 'oknovmir.podolsk@mail.ru',
                'address': 'Адреса пока нет',
                'manager': 'Лебедева Ольга Владимировна'
            }, {

                'map': 'https://yandex.ru/map-widget/v1/-/CDFaQL4l',
                'city': 'МО, Апрелевка',
                'phone': '+7(903)247-47-06',
                'email': 'penzina_ys@mail.ru',
                'address': 'Республиканская ул. 13',
                'manager': 'Пензина Юлия Сергеевна'
            }
        ]

        return context

    # Метод отправляет сообщение в ТГ админу через бота

    @staticmethod
    async def send_feedback_to_email(message: str, message_from: int = None) -> None:
        TOKEN = os.getenv('TOKEN')
        CHAT_ID = os.getenv('CHAT_ID')
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        params = {
            "chat_id": CHAT_ID,
            "text": message,
            "parse_mode": "HTML"
        }

        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as response:
                if response.status == 200:
                    print("Message sent successfully")
                else:
                    print("Message failed to send")
                    print(await response.text())

    def post(self, *args, **kwargs):
        message_body = self.request.POST.get('message_body')
        asyncio.run(self.send_feedback_to_email(message_body))

        return HttpResponseRedirect(reverse_lazy('mainapp:success'))


# Контроллер страницы новостей
# родитель ListView для удобства работы со страницами, где нужна пагинация
class NewsView(ListView):
    paginate_by = 6
    model = News
    template_name = 'mainapp/news.html'
    context_object_name = 'object'
    extra_context = {
        'title': 'Новости',
    }

    # В --get_queryset-- переопределяется --object_list-- который отоброжает список новостей
    # фильтруется чере менеджер --order_by-- по дате создания и реверсируется
    def get_queryset(self):
        queryset = News.objects.order_by('created_at').reverse()
        return queryset


class NewsDetailView(DetailView):
    model = News
    template_name = 'mainapp/news_post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        return get_object_or_404(News, slug=self.kwargs[self.slug_url_kwarg])

    # В get_context_data добовляем  context['image'] фотографии которые сортируються по id через slug
    # slug пренодлежит опреджеленной новости которая имеет опред id
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        item = Images.objects.filter(post=News.objects.filter(slug=self.kwargs[self.slug_url_kwarg]).get())
        context['image'] = item
        return context


    # def get_queryset(self):
    #     queryset = Images.objects.all()
    #     print(queryset)
    #     return queryset
    #
    # queryset = 'post'


# Контроллер проектов
# родитель ListView для удобства работы со страницами где нужна пагинация
class ProjectCategoryView(ListView):
    # paginate_by = 3
    template_name = 'mainapp/projects_category.html'
    model = ProjectCategory
    # pk_url_kwarg = 'pk'
    context_object_name = 'post'
    extra_context = {
        'title': 'Наши проекты',
    }

    # def get_object(self, queryset=None):
    #     return get_object_or_404(ProjectCategory, pk=self.kwargs[self.pk_url_kwarg])


class ProjectView(ListView):
    paginate_by = 6
    template_name = 'mainapp/projects.html'
    model = Project
    pk_url_kwarg = 'pk'
    context_object_name = 'post'
    extra_context = {
        'title': 'Проекты',
    }
    # В get_queryset переопределяется object_list в котором содержится наименование проектов отсортированный по
    # категориям

    def get_queryset(self):
        queryset = Project.objects.filter(category=self.kwargs[self.pk_url_kwarg])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = ProjectCategory.objects.filter(id=self.kwargs[self.pk_url_kwarg]).get()
        # print(context)
        return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'mainapp/projects_post.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        return get_object_or_404(Project, slug=self.kwargs[self.slug_url_kwarg])

    # смотреть 206 строку
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        item = ImagesProject.objects.filter(post=Project.objects.filter(slug=self.kwargs[self.slug_url_kwarg]).get())
        context['image'] = item
        return context


# Контроллер нуждающихся
# родитель ListView для удобства работы со страницами где нужна пагинация
class AllYouNeedIsView(ListView):
    paginate_by = 6 
    # в дальнейшем нужно поставить 9
    template_name = 'mainapp/allyouneedis.html'
    model = AllYouNeedIs
    slug_url_kwarg = 'post'
    context_object_name = 'object'
    extra_context = {
        'title': 'Наши подопечные',
    }


class AllYouNeedIsDetailView(DetailView):
    model = AllYouNeedIs
    template_name = 'mainapp/allyouneedis_post.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'post'
    extra_context = {
        'title': 'Наши подопечные',
    }

    def get_object(self, queryset=None):
        return get_object_or_404(AllYouNeedIs, slug=self.kwargs[self.slug_url_kwarg])

    # смотреть 206 строку
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        item = ImagesAllYouNeedIs.objects.filter(post=AllYouNeedIs.objects.filter(slug=self.kwargs[self.slug_url_kwarg]).get())
        context['image'] = item
        return context


# Контроллер страницы О нас
class AboutView(TemplateView):
    template_name = 'mainapp/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'О нас'
        return context


# Контроллер страницы Цели фонда
class TargetsView(TemplateView):
    template_name = 'mainapp/targets.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Цели фонда'
        return context


# Контроллер страницы История фонда
class HistoryView(TemplateView):
    template_name = 'mainapp/history.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'История фонда'
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


# Контроллер страницы с отчетами
class ReportView(ListView):
    template_name = 'mainapp/report.html'
    model = Report
    context_object_name = 'object'
    extra_context = {
        'title': 'Отчеты',
    }

