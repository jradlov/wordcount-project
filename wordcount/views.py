from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html', {'mykey':'this is the value for mykey'}) # pass a dictionary to home.html

def about(request):
    return render(request, 'about.html') 

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    print(fulltext)

    for word2 in wordlist:           # don't count '--' as a word
        if word2 == '--':
            wordlist.remove(word2)
        if word2 == '-':
            wordlist.remove(word2)

    dictionary1 = {}        # declare empty dictionary

    for fullword in wordlist:
        word = fullword.strip(',')      # strip commas from words like 'nation,'
        word = fullword.strip('.')      # strip periods from words like 'equal.'
        word = fullword.strip(':')
        word = fullword.strip(';')
        word = fullword.strip('?')
        word = fullword.strip('!')
        #word = fullword.strip('%3F')

        if word in dictionary1:
            dictionary1[word] += 1
        else:
            #if word != '--':            # don't count '--' as a word
            dictionary1[word] = 1

    sortedwords = sorted(dictionary1.items(), key=operator.itemgetter(1),reverse=True)

    return render(request, 'count.html', { 'fulltext':fulltext, 'wordcount':len(wordlist),
        'dictionary1':dictionary1, 'sortedwords':sortedwords })

        # 'dictionarylist':dictionary1.items()
