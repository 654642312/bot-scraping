import asyncio
from playwright.async_api import async_playwright


def checkStock(ContentButton):
    if ContentButton == "Finalizar la compra":
        return True
    else:
        return False


shops = [
    {
        'shop': 'Microsoft',
        'url': 'https://www.xbox.com/es-es/configure/8WJ714N3RBTL',
    },
]


async def init():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://www.xbox.com/es-es/configure/8WJ714N3RBTL")
        content = await page.text_content('[aria-label="Finalizar la compra del pack"]')
        has_stock = checkStock(content)
        print({'shop': 'Microsoft', 'content': content, 'has_stock': has_stock})
        await browser.close()


if __name__ == '__main__':
    asyncio.run(init())
