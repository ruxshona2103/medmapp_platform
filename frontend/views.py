from django.shortcuts import render

def home(request, lang="uz"):
    if lang not in ["uz", "ru", "en"]:
        lang = "uz"
    return render(request, f"frontend/{lang}/index.html")

def clinics(request, lang="uz"):
    if lang not in ["uz", "ru", "en"]:
        lang = "uz"
    return render(request, f"frontend/{lang}/clinics.html")

def blog(request, lang="uz"):
    if lang not in ["uz", "ru", "en"]:
        lang = "uz"
    return render(request, f"frontend/{lang}/blog.html")

def doctors(request, lang="uz"):
    if lang not in ["uz", "ru", "en"]:
        lang = "uz"
    return render(request, f"frontend/{lang}/doctors.html")

def services(request, lang="uz"):
    if lang not in ["uz", "ru", "en"]:
        lang = "uz"
    return render(request, f"frontend/{lang}/services.html")
