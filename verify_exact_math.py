import asyncio
from playwright.async_api import async_playwright
import os

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        path = os.path.abspath("index.html")
        await page.goto(f"file://{path}")

        tests = [
            ('1 / 2 + 1 / 4', '3 / 4'),
            ('5 nCr 2', '10'),
            ('0.5 + 1 / 4', '0.75'),
            ('√( 4', '2'),
            ('(1 + 4) nCr 2', '10'),
            ('6 nPr 2', '30')
        ]

        for expr, expected in tests:
            await page.evaluate(f"inputBuffer = '{expr}'; evaluate();")
            result = await page.evaluate("inputBuffer")
            print(f"Expr: {expr} | Expected: {expected} | Actual: {result}")

        await browser.close()

asyncio.run(run())
