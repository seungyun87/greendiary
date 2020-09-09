from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.http import HttpResponse, HttpResponseRedirect 

from .models import Diary
from account.models import Profile

from django.views.generic.base import View
from django.http import HttpResponseForbidden
from urllib.parse import urlparse

from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView
from django.utils import timezone

from datetime import datetime, timedelta, date
from django.utils.safestring import mark_safe
from .calendar import Calendar
import calendar

# Create your views here.
def home(request):
    return render(request, 'home.html')

class CalendarView(ListView):
    model = Diary
    template_name_suffix = '_calendar'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(day):
    first = day.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(day):
    days_in_month = calendar.monthrange(day.year, day.month)[1]
    last = day.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

class DiaryList(ListView):
    model = Diary
    template_name_suffix = '_list'

class DiaryCreate(CreateView):
    model = Diary
    template_name_suffix = '_create'
    fields = '__all__'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            self.request.user.profile.get_points(1)
            return redirect('/')
        else:
            return self.render_to_response({'form':form})


class DiaryDelete(DeleteView):
    model = Diary
    template_name_suffix = '_delete'
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()
        if object.author != request.user:
            messages.warning(request, '삭제할 권한 없음')
            return HttpResponseRedirect('/')
        else:
            return super(DiaryDelete, self).dispatch(request, *args, **kwargs)


class DiaryDetail(DetailView):
    model = Diary
    template_name_suffix = '_detail'

class DiaryEdit(UpdateView):
    model = Diary
    template_name_suffix = '_edit'
    fields = ['text', 'image']
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()
        if object.author != request.user:
            messages.warning(request, '수정할권한없음')
            return HttpResponseRedirect('/')
        else:
            return super(DiaryEdit, self).dispatch(request, *args, **kwargs)