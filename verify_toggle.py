import asyncio
from playwright.async_api import async_playwright
import os

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        path = os.path.abspath("index.html")
        await page.goto(f"file://{path}")

        # Start with 1.5
        await page.evaluate("inputBuffer = '1.5'; updateDisplay();")

        # Toggle 1: should be 3 / 2
        await page.evaluate("toggleDecFrac();")
        res1 = await page.evaluate("inputBuffer")
        print(f"Toggle 1 (1.5): {res1}")

        # Toggle 2: should be 1 _ 1 / 2
        await page.evaluate("toggleDecFrac();")
        res2 = await page.evaluate("inputBuffer")
        print(f"Toggle 2: {res2}")

        # Toggle 3: should be 1.5
        await page.evaluate("toggleDecFrac();")
        res3 = await page.evaluate("inputBuffer")
        print(f"Toggle 3: {res3}")

        await browser.close()

asyncio.run(run())
