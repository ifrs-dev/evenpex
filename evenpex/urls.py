from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from events import views

urlpatterns = [
    path('', views.EventListView.as_view(), name="home"),
    path('eventos/pesquisa/', views.EventSearchListView.as_view(), name="event-search"),
    path('eventos/extensao/', views.EventExtensionListView.as_view(), name="event-extension"),
    path('eventos/ensino/', views.EventTeachingListView.as_view(), name="event-teaching"),
    path('eventos/abertos/', views.PageEventsListView.as_view(), name="event-open"),
    path('eventos/meus/', login_required(views.MyRegistrationsListView.as_view()), name="my-events"),
    path('evento/<int:pk>/', views.EventDetailView.as_view(), name='event-detail'),
    path('evento/<int:pk>/participantes/', login_required(views.RegistrationsListView.as_view()), name="registrations-list"),
    path('evento/<int:pk>/participantes/imprimir/', login_required(views.RegistrationsPDFView.as_view()), name="registrations-list-pdf"),
    path('evento/<int:pk>/inscricao/', login_required(views.EventRegistrationView.as_view()), name="event-registration"),
    path('evento/presenca/<int:pk>/', login_required(views.RegistrationPresentView.as_view()), name="registration-present"),
    path('evento/ausencia/<int:pk>/', login_required(views.RegistrationAbsentView.as_view()), name="registration-absent"),
    path('evento/certificado/<int:pk>/', login_required(views.RegistrationDetailView.as_view()), name="registration-detail"),
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.logout, {'next_page': '/login/'}, name="logout"),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'evenPEX'
admin.site.index_title = 'Sistema de administração de eventos acadêmicos'
admin.site.site_title = 'evenPEX'
