from django.shortcuts import render
from django.http import Http404
from django.conf import settings


def colors(request):
    try:
        theme = settings.THEME
    except e:
        theme = False
    # end try
    if theme:
        return render(request, 'exileui/colors.css', {
            'accent': theme.get('accent'),
            'accent_ligth': theme.get('accent_ligth'),
            'primary': theme.get('primary'),
            'secundary': theme.get('secundary')
        }, content_type='text/css')
    else:
        raise Http404
    # end if
# end def
