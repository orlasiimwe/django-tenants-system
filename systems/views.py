from django.shortcuts import render,redirect, get_object_or_404
import datetime
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Tenant
from .forms import TenantForm ,UpdateTenantForm,SearchForm
from django.contrib import messages

def get_home(request):
    return(render( request, 'home.html'))

@login_required
def get_visitors(request):
    tenants=Tenant.objects.all()
    form = SearchForm()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search_word=form.cleaned_data['search']
            result=Tenant.objects.filter(first_name=search_word)
            
            # if result is None:
            #     result=Tenant.objects.filter(last_name=search_word).exists()

            #     if result is None:
            #         result=Tenant.objects.filter(company=search_word).exists()

            #     else:
            #         result='Does not exist'
            context={
                'result':result,
                'form':form
                
            }
            return(render( request, 'get_visitors.html',context))
        else:
            form= SearchForm()
    else:
        context={            
            'tenants':tenants,
            'form':form,
        }
        return(render( request, 'get_visitors.html',context))

@login_required
def add_visitors(request):
    form = TenantForm()
    if request.method == 'POST':
        form = TenantForm(request.POST)
        if form.is_valid():
            tenant= Tenant(
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                company=form.cleaned_data["company"],
                temperature=form.cleaned_data["temperature"],
                id_no=form.cleaned_data["id_no"],
                
            )
            tenant.save()
            return HttpResponseRedirect('/visitors')
        else:
            form = TenantForm()

    context = {
        "form": form,
    }
    return render(request, "add_visitors.html", context)

@login_required
def visitor_details(request,pk):
   tenant=Tenant.objects.get(pk=pk)

   context={
       'tenant':tenant
   }
   return(render( request, 'visitor_details.html',context))

@login_required
def update_visitor(request ,pk):
    tenant=Tenant.objects.get(pk=pk)

    form = UpdateTenantForm()
    if request.method == 'POST':
        form = UpdateTenantForm(request.POST or None)
        if form.is_valid():
            tenant.temperature=form.cleaned_data['temperature']
            tenant.date = datetime.date.today()
            tenant.save()
           
            
            return HttpResponseRedirect('/visitors')
        else:
            form = UpdateTenantForm()

    context = {
        "form": form,
    }
    return render(request, "update_visitor.html", context)


@login_required
def search(request):
    return render(request,"search_visitors.html")
