import asyncio
from playwright.async_api import async_playwright
import os

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        path = os.path.abspath("index.html")
        await page.goto(f"file://{path}")

        # Store 5 to x
        await page.evaluate("ans = 5; showStoMenu();")
        await page.click("text=1: x")

        # Use x in expression: x * 2
        await page.evaluate("inputBuffer = 'x * 2'; evaluate();")
        res = await page.evaluate("inputBuffer")
        print(f"Result of x * 2 (x=5): {res}")

        # Store 10 to y
        await page.evaluate("ans = 10; showStoMenu();")
        await page.click("text=2: y")

        # Use y: y + 3
        await page.evaluate("inputBuffer = 'y + 3'; evaluate();")
        res_y = await page.evaluate("inputBuffer")
        print(f"Result of y + 3 (y=10): {res_y}")

        await browser.close()

asyncio.run(run())
