import re
import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from products.models import Product


class Command(BaseCommand):
    help = "Scrape products from Basalam category page"

    def handle(self, *args, **options):
        url = "https://basalam.com/cat/tools/%D8%A2%DB%8C-%D8%B3%DB%8C"

        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        if response.status_code != 200:
            self.stdout.write(self.style.ERROR(f"Failed to fetch page: {response.status_code}"))
            return

        soup = BeautifulSoup(response.text, "html.parser")
        product_links = soup.select("a[href*='/product/']")

        self.stdout.write(f"Found {len(product_links)} product links")

        created_count = 0
        skipped_count = 0

        for link in product_links:
            href = link.get("href")
            full_url = "https://basalam.com" + href

            name_tag = link.select_one("h2")
            if not name_tag:
                continue
            name = name_tag.text.strip()

            price_tag = link.select_one("span.TQCqjN")
            if not price_tag:
                continue
            price_text = price_tag.text.strip()
            price_digits = re.sub(r"[^\d]", "", price_text)
            if not price_digits:
                continue
            price = int(price_digits)

            product, created = Product.objects.get_or_create(
                url=full_url,
                defaults={"name": name, "price": price},
            )

            if created:
                created_count += 1
                self.stdout.write(self.style.SUCCESS(f"Created: {name} — {price:,} تومان"))
            else:
                skipped_count += 1

        self.stdout.write(self.style.SUCCESS(
            f"\nDone. {created_count} new products added, {skipped_count} skipped."
        ))