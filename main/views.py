from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .forms import URLForm
from .models import URL

# Create your views here.


def home(request):
    if request.method == "POST":
        form = URLForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            try:
                name = URL.objects.get(name=name)
                form.errors["__all__"] = "Name is exist try with differnt name."
                return render(request, "main/home.html", {"form": form})
            except URL.DoesNotExist:
                form.save()
                return render(request, "main/success.html", {"name": name})
    form = URLForm()
    return render(request, "main/home.html", {"form": form})


def url_redirect(request, postfix):
    try:
        url = URL.objects.get(name=postfix).url
        return redirect(url)
    except URL.DoesNotExist:
        return render(request, "main/error.html")
