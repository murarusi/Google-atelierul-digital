from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from aplicatie2.models import Companies


class CompaniesView(LoginRequiredMixin, ListView):
    model = Companies
    template_name = "aplicatie2/companies_index.html"


class CreateCompanyView(LoginRequiredMixin, CreateView):
    model = Companies
    fields = ["name", "website", "company_type"]
    template_name = "aplicatie2/company_form.html"

    def get_success_url(self):
        return reverse('companies:companies_list')


class UpdateCompaniesView(LoginRequiredMixin, UpdateView):
    model = Companies
    fields = ["name", "website", "company_type"]
    template_name = "aplicatie2/company_form.html"

    def get_success_url(self):
        return reverse('companies:companies_list')


@login_required
def delete_company(request, pk):
    Companies.objects.filter(id=pk).update(active=0)
    return redirect("companies:companies_list")

@login_required
def activate_company(request, pk):
    Companies.objects.filter(id=pk).update(active=1)
    return redirect("companies:companies_list")
