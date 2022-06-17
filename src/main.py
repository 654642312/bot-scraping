import asyncio
from playwright.async_api import async_playwright


async def init():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://www.google.com/")
        print(await page.title())
        await browser.close()


if __name__ == '__main__':
    asyncio.run(init())
