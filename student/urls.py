from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import StudentsListView, StudentAddView, StudentDeleteView, StudentUpdateView, MainPageView, StudentDetailView

app_name = 'student'

urlpatterns = [
    path('students/', StudentsListView.as_view(), name='students'),
    path('students/new_student/', StudentAddView.as_view(), name='student_add'),
    path('students/about/<int:pk>/', StudentDeleteView.as_view(), name='student_delete'),
    path('students/update/<int:pk>/', StudentUpdateView.as_view(), name='student_update'),
    path('students/delete/<int:pk>/', StudentDetailView.as_view(), name='student_about'),
    path('', MainPageView.as_view(), name='main'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)