from django import template

register = template.Library()

@register.filter(name='count_replies')
def count_replies(replies,com):
    counter=0
    for r in replies:
        if r.parent.sno == com:
            counter+=1
    return counter
    
