from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, FileResponse
from dataclasses import dataclass

from main.models import Dictionary
from main.forms import DictionaryForm


def index(request):
    return render(
        request,
        'index.html'
    )


def words_list(request):
    data = Dictionary.objects.all()
    return render(
        request,
        'words_list.html',
        {
            'dict': data
        }
    )


def add_word(request):
    form = DictionaryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('main:index')

    return render(
        request,
        'add_word.html',
        {
            'form': form
        }
    )

def download_txt(requests):
    data = ''
    data_pair = Dictionary.objects.all()
    for el in data_pair:
        data += f'{el.word} - {el.translation}\n'

    filename = 'переводы.txt'
    response = HttpResponse(data)
    response['Content-Type'] = 'text/plain; charset=utf-8'
    response['Content-Disposition'] = f'attachment; filename={filename}'
    return response
