from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, render_to_response
from django.views.generic import DetailView, ListView

from .models import Site, ColoProvider, Region, Specs
from .forms import ExcelForm

@login_required
def sites_summary(request):
    sites = Site.objects.all() 
    return render(request, 'reporting/sites_summary.html', {'sites': sites})


@login_required
def sites(request):
    sites = Site.objects.all() 
    return render(request, 'reporting/list/sites.html', {'sites': sites})

@login_required
def site_detail(request, site_id):
    try: 
        site = Site.objects.get(pk=site_id)
        specs = site.get_latest_specs()
    except Site.DoesNotExist: 
        raise Http404("Site does not exist")
    return render(request, 'reporting/detail/site.html', {'site': site, 'specs' : specs})

@login_required
def specs_by_site_code_and_pk(request, site_code, specs_id):
    specs = get_object_or_404(Specs, pk=specs_id)
    site = get_object_or_404(Site, code=site_code)
    return render(request, 'reporting/detail/site.html', {'site': site, 'specs' : specs})

@login_required 
def site_by_code(request, site_code):
    site = get_object_or_404(Site, code=site_code)
    return site_detail(request, site.pk)

@login_required
def topology_summary(request):
    return render(request, 'reporting/topology_summary.html', {})

@login_required 
def upload_excel(request):
    if request.method == 'POST':
        form = ExcelForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else: 
        form = ExcelForm()
    return render_to_response('reporting/upload.html', {'form': form})
        

def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)

class RegionList(LoginRequiredMixin, ListView):
    model = Region

class ColoProviderList(LoginRequiredMixin, ListView):
    model = ColoProvider

class SiteList(LoginRequiredMixin,ListView):
    model = Site

class SiteDetail(LoginRequiredMixin, DetailView):
    model = Site

# class SpecsWeightsList(LoginRequiredMixin, ListView):
#     model = SpecsWeights
