from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from events import views

urlpatterns = [
    path('', views.EventListView.as_view(), name="home"),
    path('evento/<int:pk>/', views.EventDetailView.as_view(), name='event-detail'),
    path('eventos-pesquisa/', views.EventSearchListView.as_view(), name="event-search"),
    path('eventos-extensao/', views.EventExtensionListView.as_view(), name="event-extension"),
    path('eventos-ensino/', views.EventTeachingListView.as_view(), name="event-teaching"),
    path('meus-eventos/', login_required(views.MyRegistrationsListView.as_view()), name="my-events"),
    path('inscricao/<int:pk>/', login_required(views.EventRegistrationView.as_view()), name="event-registration"),
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.logout, {'next_page': '/login/'}, name="logout"),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'evenPEX'
admin.site.index_title = 'Sistema de administração de eventos acadêmicos'
admin.site.site_title = 'evenPEX'
