from django.urls import path
from .views import DiaryCreate, DiaryList, CalendarView, DiaryDetail, DiaryDelete, DiaryEdit
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'diary'

urlpatterns = [
    path("", views.home, name="home"),
    path("create/", DiaryCreate.as_view(), name="create"),
    path("calendar/", CalendarView.as_view(), name="calendar"),
    path("list/", DiaryList.as_view(), name="list"),
    path("detail/<int:pk>", DiaryDetail.as_view(), name="detail"),
    path("delete/<int:pk>", DiaryDelete.as_view(), name="delete"),
    path("edit/<int:pk>", DiaryEdit.as_view(), name="edit"),
    path("news/", views.news, name="news"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)