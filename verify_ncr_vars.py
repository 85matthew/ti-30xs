import asyncio
from playwright.async_api import async_playwright
import os

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        path = os.path.abspath("index.html")
        await page.goto(f"file://{path}")

        # Set y = 5
        await page.evaluate("vars.y = 5;")

        # Test y nCr 2
        await page.evaluate("inputBuffer = 'y nCr 2'; evaluate();")
        res = await page.evaluate("inputBuffer")
        print(f"y nCr 2 (y=5): {res}")

        await browser.close()

asyncio.run(run())
