from django.urls import path 

from .views import home, polling_unit_result, lga_result

app_name="pollapp"
urlpatterns = [
    path("", home, name="home"),
    path("polling-unit-results/", polling_unit_result, name="polling_unit_result"),
    path("lga-result/", lga_result, name="lga_result"),
]