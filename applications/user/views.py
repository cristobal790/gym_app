from django.shortcuts import redirect


def redirect_view(request):
    response = redirect('account_login')
    return response
