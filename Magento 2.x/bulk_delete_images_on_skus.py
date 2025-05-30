import requests

MAGENTO_BASE_URL = 'https://server.base.url'  # <-- CHANGE THIS
ADMIN_TOKEN = 'API_auth_token'  # <-- generate with /rest/all/V1/integration/admin/token or make a permanent one with Magento integration


HEADERS = {
    'Authorization': f'Bearer {ADMIN_TOKEN}',
    'Content-Type': 'application/json'
}

def remove_images_from_product(sku):
    url = f'{MAGENTO_BASE_URL}/rest/all/V1/products/{sku}'
    resp = requests.get(url, headers=HEADERS)
    if resp.status_code != 200:
        print(f"Failed to fetch SKU {sku}: {resp.text}")
        return

    product = resp.json()
    # Unset image roles by setting them to 'no_selection'
    product['custom_attributes'] = [
        attr for attr in product.get('custom_attributes', [])
        if attr['attribute_code'] not in ['image', 'small_image', 'thumbnail', 'swatch_image']
    ]
    product['custom_attributes'] += [
        {'attribute_code': 'image', 'value': 'no_selection'},
        {'attribute_code': 'small_image', 'value': 'no_selection'},
        {'attribute_code': 'thumbnail', 'value': 'no_selection'},
        {'attribute_code': 'swatch_image', 'value': 'no_selection'},
    ]

    product['media_gallery_entries'] = []

    # Update product
    update_url = f'{MAGENTO_BASE_URL}/rest/all/V1/products/{sku}'
    resp = requests.put(update_url, headers=HEADERS, json={'product': product})
    if resp.status_code == 200:
        print(f"All images deleted for SKU: {sku}")
    else:
        print(f"Failed to update SKU {sku}: {resp.text}")

def main():
    with open('delete_skus.txt', 'r') as f:
        skus = [line.strip() for line in f if line.strip()]
    for sku in skus:
        remove_images_from_product(sku)

if __name__ == "__main__":
    main()
