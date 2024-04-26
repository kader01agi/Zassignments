from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register("", views.CountryViewSet)  # Use a meaningful endpoint name
urlpatterns = router.urls
