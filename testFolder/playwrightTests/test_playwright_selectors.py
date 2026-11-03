from playwright.sync_api import Page, expect
import re

PLAYWRIGHT_URL = "file:///C:/Users/User/PROJECT/myPythonTests/testFolder/playwrightTests/playwright-selectors.html"

# TODO: Find the button using its role and name.
def test_for_all_mission(page: Page):
    page.goto(PLAYWRIGHT_URL)
    button = page.get_by_role("button", name="Open Details")
    page.pause()
    button.highlight()
    # TODO: Click it and verify the confirmation text.
    button.click()
    expect(page.locator("#button-result")).to_have_text("Button clicked! This text appeared after the click.")
    # TODO: Find the email input using its placeholder.
    email_input = page.get_by_placeholder("name@example.com")
    assert email_input.is_visible()
    # TODO: Fill in the password field.
    password_input = page.get_by_placeholder("Enter your password")
    password_input.scroll_into_view_if_needed()
    password_input.highlight()
    password_input.fill("naama2580")
    # TODO: Select United Kingdom from the dropdown.
    page.get_by_label("Choose a country").select_option("United Kingdom")
    # TODO: Select Premium.
    premium = page.get_by_label("Premium")
    premium.check()
    expect(premium).to_be_checked()
    # TODO: Check the terms checkbox.
    terms_checkbox = page.get_by_label(" I agree to the terms")
    terms_checkbox.check()
    expect(terms_checkbox).to_be_checked()
    # TODO: Submit the form and verify the confirmation.
    submit_button = page.get_by_role("button", name="Submit Form")
    submit_button.click()
    expect(page.locator("#form-result")).to_have_text("Form submitted successfully!")
    # TODO: Click the Details link and verify that a new tab opens.
    with page.context.expect_page() as new_page_info:
        details_link = page.get_by_role("link", name="Go to Details Page")
        details_link.click()
    new_page = new_page_info.value
    new_page.wait_for_load_state()
    expect(new_page).to_have_url("https://playwright.dev/")
    # TODO: Verify the headline and paragraph on the new page
    expect(new_page.get_by_role("heading", name="Playwright enables reliable web automation for testing, scripting, and AI agents.")).to_be_visible()