from rest_framework import routers
from .views import BBCNewsViewSet, NikkeiNewsViewSet

router = routers.DefaultRouter()
router.register(r'v1/BBCNews', BBCNewsViewSet)
#router.register(r'v1/BBCNews/<int:year>&month=<int:month>&day=<int:day>')

router.register(r'v1/NikkeiNews', NikkeiNewsViewSet)
#router.register(r'v1/NikkeiNews/<int:year>&month=<int:month>&day=<int:day>')
