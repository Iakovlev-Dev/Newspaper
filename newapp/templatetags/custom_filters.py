from django import template
import re
 
CENZOR_VOCABULARY = ['спорт', 'спортивно', 'спортом']

register = template.Library()

@register.filter(name='cenzor')
def cenzor(text):
    cenzor_text = text
    for word in cenzor_text.split()[:]:
        if word in CENZOR_VOCABULARY:
            word = f'{word[0]}{re.sub("[a-zA-zа-яА-ЯёЁ]","*", word[1:-1])}{word[-2:]}'
        cenzor_text += f' {word}'
    return cenzor_text