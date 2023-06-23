from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'notes', views.NotesViewSet)


urlpatterns = [
  path("", include(router.urls)),
  path("healthcheck/", views.healthcheck, name="healthcheck"),
  # Documentation api
  path("schema/", SpectacularAPIView.as_view(), name="schema"),
  path("schema/docs/", SpectacularSwaggerView.as_view(url_name="schema")),
]