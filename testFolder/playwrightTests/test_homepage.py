from playwright.sync_api import Page, expect
import re

PLAYWRIGHT_URL = "https://playwright.dev/"

# def test_homepage_heading(page: Page):
#     page.goto(PLAYWRIGHT_URL)
#     pageAccesibility = page.locator("body").aria_snapshot()
#     print(f"PageAccessibility: {pageAccesibility}")
#     heading = page.get_by_role("heading", name="playwright", level=1)
#     print(f"Heading: {heading}")
#     page.pause()
#     heading.highlight()
#     expect(heading).to_be_visible()

    
def test_get_started_navigation(page: Page):
    page.goto(PLAYWRIGHT_URL)
    link = page.get_by_role("link", name="Get started")
    page.pause()
    link.highlight()
    link.click()
    expect(
        page.get_by_role("heading", name="Installation")
    ).to_be_visible()


