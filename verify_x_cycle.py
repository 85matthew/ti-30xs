import asyncio
from playwright.async_api import async_playwright
import os

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        path = os.path.abspath("index.html")
        await page.goto(f"file://{path}")

        # Click x once
        await page.click("button[data-val='x']")
        res1 = await page.evaluate("inputBuffer")
        print(f"Press 1: {res1}")

        # Click x again
        await page.click("button[data-val='x']")
        res2 = await page.evaluate("inputBuffer")
        print(f"Press 2: {res2}")

        # Click x again
        await page.click("button[data-val='x']")
        res3 = await page.evaluate("inputBuffer")
        print(f"Press 3: {res3}")

        # Click + then x
        await page.click("button[data-val='+']")
        await page.click("button[data-val='x']")
        res4 = await page.evaluate("inputBuffer")
        print(f"Press + then x: {res4}")

        await browser.close()

asyncio.run(run())
