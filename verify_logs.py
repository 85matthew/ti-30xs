import asyncio
from playwright.async_api import async_playwright
import os

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        path = os.path.abspath("index.html")
        await page.goto(f"file://{path}")

        # Test log(10)
        await page.evaluate("inputBuffer = 'log(10)'; evaluate();")
        res1 = await page.evaluate("inputBuffer")
        print(f"log(10): {res1}")

        # Test ln(10) - should be ~2.3025
        await page.evaluate("inputBuffer = 'ln(10)'; evaluate();")
        res2 = await page.evaluate("inputBuffer")
        print(f"ln(10): {res2}")

        await browser.close()

asyncio.run(run())
