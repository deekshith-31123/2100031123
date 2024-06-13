from django.http import JsonResponse
import requests

BEARER_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiZXhwIjoxNzE4MjY0NDU2LCJpYXQiOjE3MTgyNjQxNTYsImlzcyI6IkFmZm9yZG1lZCIsImp0aSI6ImFlZTU2OGMxLWZiMGItNDA5YS04YjlmLTRkODZhNTBkYjcxNCIsInN1YiI6InBhdG5hbmFzYWlkZWVrc2hpdGhAZ21haWwuY29tIn0sImNvbXBhbnlOYW1lIjoiS0wgVU5JVkVSU0lUWSIsImNsaWVudElEIjoiYWVlNTY4YzEtZmIwYi00MDlhLThiOWYtNGQ4NmE1MGRiNzE0IiwiY2xpZW50U2VjcmV0IjoiYU5HS1B6QlhieWFEZkh6biIsIm93bmVyTmFtZSI6IlAuU0FJIERFRUtTSElUSCIsIm93bmVyRW1haWwiOiJwYXRuYW5hc2FpZGVla3NoaXRoQGdtYWlsLmNvbSIsInJvbGxObyI6IjIxMDAwMzExMjMifQ.X_ajJHu8mVPrJ9jQ0vS0-TZki17rx9ug6CqS6BlH728'  # Replace with your actual bearer token


def get_top_products(request, companyname, categoryname):
    n = int(request.GET.get('n', 10))
    page = int(request.GET.get('page', 1))
    min_price = request.GET.get('minPrice', 0)
    max_price = request.GET.get('maxPrice', 1000000)
    sort_by = request.GET.get('sortBy', 'price')
    order = request.GET.get('order', 'asc')

    url = f'http://20.244.56.144/test/companies/{companyname}/categories/{categoryname}/products'
    params = {
        'top': n,
        'minPrice': min_price,
        'maxPrice': max_price
    }

    headers = {
        'Authorization': f'Bearer {BEARER_TOKEN}',
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        products = response.json()

        for product in products:
            product['company'] = companyname
            product['category'] = categoryname

        reverse_order = order == 'desc'
        products = sorted(products, key=lambda x: x.get(sort_by, 0), reverse=reverse_order)

        start_index = (page - 1) * n
        end_index = start_index + n
        paginated_products = products[start_index:end_index]

        response_data = {
            'total_products': len(products),
            'total_pages': (len(products) + n - 1) // n,
            'current_page': page,
            'products': paginated_products
        }

        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Failed to fetch products'}, status=response.status_code)


def get_product_details(request, categoryname, productid):
    company, product_name = productid.split('_')

    url = f'http://20.244.56.144/test/companies/{company}/categories/{categoryname}/products'

    headers = {
        'Authorization': f'Bearer {BEARER_TOKEN}',
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        products = response.json()

        for product in products:
            if product['productName'] == product_name:
                product['company'] = company
                product['category'] = categoryname
                return JsonResponse(product)

        return JsonResponse({'error': 'Product not found'}, status=404)
    else:
        return JsonResponse({'error': 'Failed to fetch products'}, status=response.status_code)
