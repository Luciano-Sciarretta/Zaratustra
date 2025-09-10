from rest_framework import routers
from .viewset import ZaratustraRestApiViewSet




router = routers.SimpleRouter()
router.register("zaratustrarestapi", ZaratustraRestApiViewSet, basename="zaratustrarestapi")
urlpatterns = router.urls


    

