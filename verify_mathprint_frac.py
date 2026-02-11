import asyncio
from playwright.async_api import async_playwright
import os

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        path = os.path.abspath("index.html")
        await page.goto(f"file://{path}")
        await page.wait_for_selector("#calculator")

        await page.evaluate("inputBuffer = '1 / 2 + 3 / 4'; cursorPos = 13; updateDisplay();")
        await page.screenshot(path="verify_mathprint_frac_final.png")
        await browser.close()

asyncio.run(run())
