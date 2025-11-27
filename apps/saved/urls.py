from rest_framework.routers import DefaultRouter
from .views import SavedJobViewSet

router = DefaultRouter()
router.register(r'saved-jobs', SavedJobViewSet, basename='savejob')

urlpatterns = router.urls