# products/views.py
from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
import pandas as pd

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def product_add(request):
    if request.method == 'POST':
        if 'file' in request.FILES:
            # Обработка загруженного файла
            file = request.FILES['file']
            df = pd.read_excel(file)
            for index, row in df.iterrows():
                Product.objects.create(
                    article=row['Артикул'],  # Замените на ваши названия столбцов
                    status=row['Статус'],
                    sku=row['SKU'],
                    confirmation_date=row['Дата подтверждения'],
                    comment=row['Комментарий'],
 )
            return redirect('product_list')
        else:
            form = ProductForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'products/product_add.html', {'form': form})
