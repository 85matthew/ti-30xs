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

        # Press Table
        await page.click("button[data-val='table']")
        # Should be in TABLE_Y state
        content1 = await page.inner_html("#lcd-input-line")
        print(f"Table Y Screen: {content1}")

        # Enter x^2
        await page.click("button[data-val='x']")
        await page.click("button[data-val='sq']")

        # Press Enter
        await page.click("button[data-val='enter']")
        # Should be in TABLE_SETUP state
        content2 = await page.inner_html("#lcd-input-line")
        print(f"Table Setup Screen: {content2}")

        # Set Start = 5
        await page.click("button[data-val='5']")
        # Set Step = 2
        await page.click("button[data-val='down']")
        await page.click("button[data-val='2']")

        await page.screenshot(path="verify_table_setup.png")

        # Press Enter to view table
        await page.click("button[data-val='enter']")

        # Check table first row
        table_rows = await page.inner_text("#table-body")
        print(f"Table rows:\n{table_rows}")

        await page.screenshot(path="verify_table_view.png")
        await browser.close()

asyncio.run(run())
