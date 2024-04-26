from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()

router.register("", views.CityorstateViewSet, basename="city_or_state")
urlpatterns = router.urls

