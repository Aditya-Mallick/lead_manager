from rest_framework import routers
from .views import LeadApi

router = routers.DefaultRouter()
router.register('api/leads', LeadApi, 'leads')

urlpatterns = router.urls

