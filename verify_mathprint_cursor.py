import asyncio
from playwright.async_api import async_playwright
import os

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        path = os.path.abspath("index.html")
        await page.goto(f"file://{path}")

        # Type sin(30)
        await page.click("button[data-val='sin']")
        await page.click("button[data-val='3']")
        await page.click("button[data-val='0']")
        await page.click("button[data-val=')']")

        # Move left twice
        await page.click("button[data-val='left']")
        await page.click("button[data-val='left']")

        await page.screenshot(path="verify_mathprint_cursor.png")
        await browser.close()

asyncio.run(run())
