import asyncio
from playwright.async_api import async_playwright
import os

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        path = os.path.abspath("index.html")
        await page.goto(f"file://{path}")

        # Input 1 / 2
        await page.evaluate("""
            inputBuffer = '1 / 2';
            updateDisplay();
        """)
        await page.screenshot(path="verify_mathprint_frac.png")

        # Input sin(30)
        await page.evaluate("""
            inputBuffer = 'sin(30)';
            updateDisplay();
        """)
        await page.screenshot(path="verify_mathprint_sin.png")

        await browser.close()

asyncio.run(run())
