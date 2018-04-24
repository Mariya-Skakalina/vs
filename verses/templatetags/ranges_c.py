from django import template


register = template.Library()
# @ - вызов декоратора

@register.filter(name='ranges_s')
def ranges_s(arg):
    print('------sdsadad-----------')
    print(arg)
    result = []

    for i in range(0,arg):
        result.append(i+1)

    return result