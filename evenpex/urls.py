"""evenpex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
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
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
