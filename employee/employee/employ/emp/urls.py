from django.conf.urls import url
from rest_framework import routers
from views import EmployeenameViewSet, EmployeeteamViewSet

router = routers.DefaultRouter()
router.register(r'employee_name', EmployeenameViewSet)
router.register(r'employee_team', EmployeeteamViewSet)


urlpatterns = router.urls
