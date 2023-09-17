from django.urls import path
from app.views import TodoViewsets
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', TodoViewsets)
urlpatterns = router.urls