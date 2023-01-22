from django.template.defaulttags import register


@register.filter(is_safe=True)
def mediapath(text):
    return f'/media/{text}'


@register.simple_tag
def mediapath(text):
    return f'/media/{text}'