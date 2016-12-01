from django.shortcuts import render
from django.http import Http404
from django.conf import settings


def colors(request):
    try:
        theme = settings.THEME
    except:
        theme = False
    # end try
    if theme:
        return render(request, 'exileui/colors.css', {
            'accent': theme.get('accent'),
            'accent_light': theme.get('accent_light'),
            'primary': theme.get('primary'),
            'secondary': theme.get('secondary')
        }, content_type='text/css')
    else:
        raise Http404
    # end if
# end def
