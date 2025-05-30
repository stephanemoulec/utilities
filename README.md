# My Utilities

Repository of tools scripts that I use to make my life easier. When I make one that could help others, I will post them here. 
I don't guarantee any kind of support or feature enhancements. I hope it'll help a few people.

## Magento 2.x

### Bulk Delete Product Images by SKU for Magento / Adobe Commerce

Magento (Adobe Commerce) lacks native functionality to bulk delete product images across multiple SKUs. This Python script fills that gap by automating the process.

#### 🔧 What It Does

This script reads a list of SKUs from a `delete_skus_images.csv` file and performs the following actions for each product:

1. **Fetches the product by SKU via the Magento REST API**
2. **Unlinks all associated media gallery images**
3. **Sends a request to delete those images from the catalog**

This is useful in scenarios like:

* Replacing old brand logos or outdated product shots across multiple items
* Cleaning up media entries after a bulk import error
* Preparing a batch of SKUs for new image uploads

#### 📦 Requirements

* Python 3.7+
* Magento 2.4.x with REST API access enabled
* Admin token or integration credentials with appropriate media permissions

#### 📁 Input Format

The script expects a CSV file named `delete_skus_images.csv` with a simple list of SKUs (no header required).
Example:

```
SKU001
SKU002
SKU003
```
