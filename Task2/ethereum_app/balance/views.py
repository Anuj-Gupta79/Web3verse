from django.shortcuts import render
from .utils import fetch_ethereum_data

def fetch_balance(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        data = fetch_ethereum_data(address)
        return render(request, 'balance/result.html', {'data': data})
    return render(request, 'balance/index.html')
