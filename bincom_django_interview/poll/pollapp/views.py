from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .forms import LgaResultForm

from .models import (
    announced_pu_results, polling_unit,
    party, lga, announced_lga_results
)


def home(request):
    return render(request, "index.html")


def polling_unit_result(request):
    
    p_unit_results = announced_pu_results.objects.all()
    
    return render(request, "p_unit_results.html", {"p_unit_results": p_unit_results})


def lga_result(request):
    if request.method == "POST":
        form = LgaResultForm(request.POST)
        local_ga = request.POST.get("lga")
        lga_name = get_object_or_404(lga, uniqueid=local_ga)
        lga_name_total_result = sum(announced_lga_results.objects.filter(lga_name=local_ga).values_list("party_score", flat=True))
        return render(request, "lga_results.html", {"get_lga": lga_name, "lga_name_total_result": lga_name_total_result})
    form = LgaResultForm(request.GET)
    return render(request, "select_lga.html", {"form": form})
    
