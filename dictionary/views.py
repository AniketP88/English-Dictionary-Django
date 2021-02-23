from django.shortcuts import render
from PyDictionary import PyDictionary

# Create your views here.


def index(request):
    return render(request, 'index.html')


def word(request):

    search = request.GET.get('search')
    dictionary = PyDictionary()
    try:
        if search:

            meaning = dictionary.meaning(search)
            synonyms = dictionary.synonym(search)
            antonyms = dictionary.antonym(search)
            context = {
                'meaning': meaning['Noun'][0],
                'synonyms': synonyms,
                'antonyms': antonyms,
                'search': search

            }
            return render(request, 'word.html', context)
    except TypeError:
        return render(request, 'index.html', {"search": search})
