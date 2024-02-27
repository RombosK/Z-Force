import logging
import os

import requests
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.core.cache import cache
from django.core.paginator import Paginator
from django.http import JsonResponse, FileResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template.context_processors import request
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DetailView, DeleteView, View
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View

from mainapp.forms import RequestFormVolunteer, RequestFormCharity
from mainapp.models import News, ProjectCategory, AllYouNeedIs, RequestVolunteer, RequestCharity
from dotenv import load_dotenv

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
        user_from = 'Anonimus'
        TOKEN = os.getenv('TOKEN')       # в .env: токен, взятый в @BotFather ТГ
        CHAT_ID = os.getenv('CHAT_ID')   # в .env: id администратора в телеге

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
#родитель ListView для удобства работы со страницами где нужна пагинация
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
#родитель ListView для удобства работы со страницами где нужна пагинация
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
#родитель ListView для удобства работы со страницами где нужна пагинация
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


# Контроллер страницы волонтера
class RequestVolunteerEditView(View):
    model = RequestVolunteer
    form_class = RequestFormVolunteer

    def get(self, request):
        form = RequestFormVolunteer()
        return render(request, 'mainapp/request_volunteer.html', {'form': form})

    def post(self, request):
        form = RequestFormVolunteer(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/success/')  # перенаправление на страницу успешного заполнения анкеты

        return render(request, 'mainapp/success.html')


# Контроллер страницы благотворителя
class RequestCharityEditView(View):
    model = RequestCharity
    form_class = RequestFormCharity

    def get(self, request):
        form = RequestFormCharity()
        return render(request, 'mainapp/request_charity.html', {'form': form})

    def post(self, request):
        form = RequestFormCharity(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/success/')  # перенаправление на страницу успешного заполнения анкеты

        return render(request, 'mainapp/success.html')


class LoginView(TemplateView):
    template_name = 'mainapp/login.html'
#
# class DocSiteView(TemplateView):
#     template_name = 'mainapp/doc_site.html'
#


# class NewsListView(ListView):
#     model = News
#     paginate_by = 2
#
#     def get_queryset(self):
#         return super().get_queryset().filter(deleted=False)
#
#
# class NewsDetailView(DetailView):
#     model = News
#
#     def get_object(self, queryset=None):
#         return get_object_or_404(News, pk=self.kwargs.get('pk'), deleted=False)
#
#
# class NewsCreateView(PermissionRequiredMixin, CreateView):
#     model = News
#     fields = '__all__'
#     success_url = reverse_lazy('mainapp:news')
#     permission_required = ('mainapp.add_news',)
#
#
# class NewsUpdateView(PermissionRequiredMixin, UpdateView):
#     model = News
#     fields = '__all__'
#     success_url = reverse_lazy('mainapp:news')
#     permission_required = ('mainapp.change_news',)
#
#
# class NewsDeleteView(PermissionRequiredMixin, DeleteView):
#     model = News
#     success_url = reverse_lazy('mainapp:news')
#     permission_required = ('mainapp.delete_news',)


# class NewsWithPagination(NewsListView):
#
#     def get_context_data(self, page, **kwargs):
#         context = super().get_context_data(page=page, **kwargs)
#         context["page_num"] = page
#         return context


# class ContactsPageView(TemplateView):
#     template_name = "mainapp/contacts.html"
#
#     def get_context_data(self, **kwargs):
#         context = super(ContactsPageView, self).get_context_data(**kwargs)
#         if self.request.user.is_authenticated:
#             context["form"] = forms.CourseFeedbackForm(
#                 user=self.request.user
#             )
#         return context

# def post(self, *args, **kwargs):
#     if self.request.user.is_authenticated:
#         cache_lock_flag = cache.get(
#             f"mail_feedback_lock_{self.request.user.pk}"
#         )
#
#         if not cache_lock_flag:
#             cache.set(
#                 f"mail_feedback_lock_{self.request.user.pk}",
#                 "lock",
#                 timeout=300,
#             )
#             messages.add_message(
#                 self.request, messages.INFO, f"Message sended"
#             )
#             tasks.send_feedback_mail.delay(
#                 {
#                     "user_id": self.request.POST.get("user_id"),
#                     "message": self.request.POST.get("message"),
#                 }
#             )
#         else:
#             self.message = messages.add_message(self.request, messages.WARNING,
#                                                 f"You can send only one message per 5 minutes", )
#     return HttpResponseRedirect(reverse_lazy("mainapp:contacts"))


# class DocSitePageView(TemplateView):
#     template_name = "mainapp/doc_site.html"


# class CoursesListView(TemplateView):
#     template_name = "mainapp/courses_list.html"
#     model = Courses
#     paginate_by = 2
#
#     def get_context_data(self, **kwargs):
#         context = super(CoursesListView, self).get_context_data(**kwargs)
#         context['objects'] = Courses.objects.all()
#
#         return context
#
#
# class CourseDetailView(TemplateView):
#     template_name = "mainapp/courses_detail.html"
#
#     def get_context_data(self, **kwargs):
#         context_data = super().get_context_data(**kwargs)
#         context_data['course_object'] = get_object_or_404(Courses, pk=self.kwargs.get('pk'))
#         context_data['lessons'] = Lesson.objects.filter(course=context_data['course_object'])
#         context_data['teachers'] = CourseTeachers.objects.filter(course=context_data['course_object'])
#         feedback_list_key = f"course_feedback{context_data['course_object'].pk}"
#         cached_feedback_list = cache.get(feedback_list_key)
#         if cached_feedback_list is None:
#             context_data['feedback_list'] = CourseFeedback.objects.filter(course=context_data['course_object'])
#             cache.set(feedback_list_key, context_data['feedback_list'], timeout=300)
#         else:
#             context_data['feedback_list'] = cached_feedback_list
#
#         if not self.request.user.is_anonymous:
#             if not CourseFeedback.objects.filter(
#                     course=context_data["course_object"],
#                     user=self.request.user).count():
#                 context_data['feedback_form'] = CourseFeedbackForm(
#                     course=context_data['course_object'],
#                     user=self.request.user
#                 )
#
#         return context_data
#
#
# class CourseFeedbackFormView(CreateView):
#     model = CourseFeedback
#     form_class = CourseFeedbackForm
#
#     def form_valid(self, form):
#         self.object = form.save()
#         rendered_card = render_to_string('mainapp/includes/feedback_block.html', context={'item': self.object})
#         return JsonResponse({'card': rendered_card})


# class LogView(UserPassesTestMixin, TemplateView):
#     template_name = 'mainapp/logs.html'
#
#     def test_func(self):
#         return self.request.user.is_superuser
#
#     def get_context_data(self, **kwargs):
#
#         context = super(LogView, self).get_context_data(**kwargs)
#         log_slice = []
#         logs_line = 1000  # Заданное кол-во строк последних логов
#         last_line = sum(1 for line in open(settings.LOG_FILE))
#         with open(settings.LOG_FILE, "r") as log_file:
#             for i, line in enumerate(log_file):
#                 cnt = (last_line - logs_line)
#                 if i < cnt:
#                     continue
#                 log_slice.insert(0, f'{i} {line}')
#             context["logs"] = log_slice
#         return context



# class LogDownloadView(UserPassesTestMixin, View):
#
#     def test_func(self):
#         return self.request.user.is_superuser
#
#     def get(self, *args, **kwargs):
#         return FileResponse(open(settings.LOG_FILE, "rb"))

class LogDownloadView(UserPassesTestMixin, View):

    def test_func(self):
        return self.request.user.is_superuser

    def get(self, *args, **kwargs):
        return FileResponse(open(settings.LOG_FILE, "rb"))



