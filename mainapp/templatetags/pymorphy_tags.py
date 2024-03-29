from django import template
from pymorphy2 import MorphAnalyzer

register = template.Library()


@register.filter
def inflect_to_dative(word):
    morph = MorphAnalyzer()
    parsed_word = morph.parse(word)[0]
    inflected_word = parsed_word.inflect({'datv'}).word
    return inflected_word.capitalize()
