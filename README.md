# Product API

A Django REST API that scrapes product data from Basalam and exposes it via a RESTful API-

## Features

- Scrapes product name and price from a Basalam category page
- Stores products in SQLite using Django ORM
- REST API with list, detail, search, filter and ordering
- Admin panel for managing products
- Idempotent scraping (no duplicate products on re run)

## Tech Stack

- Python 3
- Django
- Django REST Framework
- django-filter
- BeautifulSoup4
- requests

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/Roozbeh_web/product-price-api.git
    cd product-price-api
    ```

2. Create and activate a virtual enviroment:
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run migrations:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser (for admin panel);
    ```bash
    python manage.py createsuperuser
    ```

6. Scrape products:
    ```bash
    python manage.py scrape_basalam
    ```

7. Run the server:
    ```bash
    python manage.py runserver
    ```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/products/` | List All products |
| GET | `/api/products/<id>/` | Retrive a single product |

### Query paramentrs

. `?search=<term>` - Search products by name
. `?price=<amount>` - Filter by exact price
. `?ordering=price` - Order by price (ascending)
- `?ordering=-price` - Order by price (descending)

### Example

GET /api/products/?search=آی سی&ordering=-price

## Admin panel

Access the admin panel at `/admin/` to view and manage scraped products-

## Notes

- The scraper targets a single category page on basalm. CSS class names may change if site updates its frontend.
- Scraping respects the site's `robots.txt`.

## Author

[Roozbeh](https://github.com/Roozbeh_web)
