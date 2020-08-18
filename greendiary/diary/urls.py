from django.urls import path
from .views import DiaryCreate, DiaryList, CalendarView
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'diary'

urlpatterns = [
    path('',views.home, name="home"),
    path("create/", DiaryCreate.as_view(), name="create"),
    path("calendar/", CalendarView.as_view(), name="calendar"),
    path("list/", DiaryList.as_view(), name="list"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)