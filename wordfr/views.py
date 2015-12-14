from django.shortcuts import render
from django.template.loader import get_template
from django.template import TemplateDoesNotExist


def index(request, filename):
    source = str()
    try:
        source = get_template(filename).template.source
    except TemplateDoesNotExist:
        return render(request, 'error.html')
    fr = dict()
    for i in source.split():
        fr[i] = fr.get(i, 0) + 1
    return render(request, 'index.html', {'fr': fr})
