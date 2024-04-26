from rest_framework.routers import SimpleRouter
from . import views



router = SimpleRouter()

router.register("", views.ContinentViewsets)
urlpatterns = router.urls