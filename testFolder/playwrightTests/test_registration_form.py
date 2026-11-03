from playwright.sync_api import Page, expect
from datetime import datetime
from consts import REGISTRATION_FORM

GITHUB_FORM_URL = "https://github.com/yashago/hadasim-qa-pytest/blob/9bcef875b222092b4f32c3599b7773e5d1aca48b/tests/playwright/src/playwright_registration_form.html"
FILE_PATH = f"https://htmlpreview.github.io/?{GITHUB_FORM_URL}"

def test_registration_form(page: Page , request):
    # Navigate to the local registration form
    page.goto(FILE_PATH)
    page.pause()
    getFormFields(page).get("registrationLink").highlight()
    page.pause()
    getFormFields(page).get("registrationLink").click()
    target_section = page.locator(REGISTRATION_FORM.get('registrationTargetSection'))
    expect(target_section).to_be_in_viewport()

    page.pause()

    fillInFullForm(page, request)
    validateResetForm(page)
    fillInFullForm(page, request)
    validateSubmitForm(page)
    #take screenshot
    test_name = request.node.name
    date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    page.screenshot(path = f"screenshots/{test_name}_{date}.png")

def test_header(page: Page):
    page.goto(FILE_PATH)
    registrationLink(page)
    PreferencesLink(page)
    helpLink(page)
    PlaywrightDocsLink(page)

def fillInFullForm(page, request):
    #TODO: Fill in the first name
    fillInFirstName(page, REGISTRATION_FORM.get('textForFirstName'))

    #TODO: Fill in the last name
    fillInLastName(page, REGISTRATION_FORM.get('textForLastName'))

    #TODO: Fill in the email
    fillInEmail(page, REGISTRATION_FORM.get('textForEmailAdress'))

    #TODO: Fill in the email confirmation
    fillInEmailConfirmation(page, REGISTRATION_FORM.get('textForEmailConfirmationAdress'))

    #TODO: Fill in the password
    fillInPassword(page, REGISTRATION_FORM.get('textForPassword'))

    #TODO: Fill in the phone number
    fillInPhoneNumber(page, REGISTRATION_FORM.get('textForPhoneNumber'))

    #TODO: Fill in the date of birth
    fillInDateOfBirth(page, REGISTRATION_FORM.get('textForDateOfBirth'))

    #TODO: Select the country
    selectCountry(page, REGISTRATION_FORM.get('country'))

    #TODO: Fill in the city
    fillInCity(page, REGISTRATION_FORM.get('city'))

    #TODO: Fill Personal website
    fillPersonalWebsite(page, REGISTRATION_FORM.get('personalWebsite'))

    #TODO: Select the gender
    selectGender(page, REGISTRATION_FORM.get('gender'))

    #TODO: Select the Occupation
    selectOccupation(page, REGISTRATION_FORM.get('occupation'))

    #TODO: Fill Short introduction
    fillShortIntroduction(page, REGISTRATION_FORM.get('shortIntroduction'))

    #TODO: Select years of experience
    selectNumOfExperienceYears(page, REGISTRATION_FORM.get('experienceYears') )

    #TODO: Select favorite browser
    selectFavoriteBrowser(page, REGISTRATION_FORM.get('favoriteBrowser') )

    #TODO: Select which topics interest you
    selectYourTopicsInterest(page, REGISTRATION_FORM.get('topicsInterestList') )

    #TODO: Select preferred contact method
    selectPreferredContactMethod(page, REGISTRATION_FORM.get('preferredContactMethod'))

    #TODO: Select 2 checkBox
    selectSubscribeCheckBox(page)
    selecttermsAndConditionsCheckBox(page)


def printAccessibilityTree(page):
    pageAccesibility = page.locator("body").aria_snapshot()
    print(f"pageAccesibility: {pageAccesibility}")

def fillField(field, value):
    field.scroll_into_view_if_needed()
    field.fill(value)

def selectField(field, label):
    field.scroll_into_view_if_needed()
    field.select_option(label=label)

def fillInFirstName(page, firstName):
    #By role, preferred method
    print(f"Filling in {firstName}")
    fillField(getFormFields(page)["firstName"], firstName)
    

def fillInLastName(page, lastName):
    #By role, preferred method
    print(f"Filling in {lastName}")
    fillField(getFormFields(page)["lastName"], lastName)

def fillInEmail(page, emailAdress):
    print(f"Filling in {emailAdress}")
    fillField(getFormFields(page)["email"], emailAdress)

def fillInEmailConfirmation(page, emailConfirmationAdress):
    print(f"Filling in {emailConfirmationAdress}")
    fillField(getFormFields(page)["emailConfirm"], emailConfirmationAdress)
    # Verify that two emails adress are match
    verifyEmailsMatch(page)

def verifyEmailsMatch(page):
    email_field = getFormFields(page)["email"]
    confirm_field = getFormFields(page)["emailConfirm"]
    expect(confirm_field).to_have_value(email_field.input_value())
    print(f"Email confirmation value: {confirm_field.input_value()} matches email value: {email_field.input_value()}")

def fillInPassword(page, Password):
    print(f"Filling in {Password}")
    fillField(getFormFields(page)["password"], Password)

def fillInPhoneNumber(page, phoneNumber):
    print(f"Filling in {phoneNumber}")
    fillField(getFormFields(page)["phone"], phoneNumber)

def fillInDateOfBirth(page, dateOfBirth):
    print(f"Filling in {dateOfBirth}")
    #By label, preferred method
    datePicker = getFormFields(page)["dateOfBirth"]
    fillField(datePicker, dateOfBirth)
    datePicker.highlight()  

def selectCountry(page, country):
    selectField(getFormFields(page)["country"], country)

def fillInCity(page, city):
    fillField(getFormFields(page)["city"], city)

def fillPersonalWebsite(page, personalWebsite):
    fillField(getFormFields(page)["website"], personalWebsite)

def selectGender(page, gender):
    page.get_by_role("radio", name=gender, exact=True).check()

def selectOccupation(page, occupation ):
    selectField(getFormFields(page)["occupation"], occupation)

def fillShortIntroduction(page, shortIntroduction):
    selfIntroduction = getFormFields(page)["intro"]
    fillField(selfIntroduction, shortIntroduction)


def selectNumOfExperienceYears(page, experienceYears):
    selectField(getFormFields(page)["experienceYears"], experienceYears)

def selectFavoriteBrowser(page, favoriteBrowser):
    selectField(getFormFields(page)["favoriteBrowser"], favoriteBrowser)

def selectYourTopicsInterest(page, topicsInterestList):
    for topic in topicsInterestList:
        page.get_by_role("checkbox", name=topic).check()

def selectPreferredContactMethod(page,preferredContactMethod ):
    page.get_by_role("radio", name=preferredContactMethod, exact=True).check()

def selectSubscribeCheckBox(page):
    getFormFields(page)["subscribe"].check()

def selecttermsAndConditionsCheckBox(page):
    getFormFields(page)["termsAndConditions"].check()

def validateResetForm(page):
    getFormFields(page).get("resetFormButton").click()
    expect(page.get_by_role("status")).to_have_text(REGISTRATION_FORM.get('resetFormButtonStatus'))
    expect(getFormFields(page).get("firstName")).to_be_empty()
    expect(getFormFields(page).get("lastName")).to_be_empty()
    expect(getFormFields(page).get("email")).to_be_empty()
    expect(getFormFields(page).get("emailConfirm")).to_be_empty()
    expect(getFormFields(page).get("password")).to_be_empty()
    expect(getFormFields(page).get("phone")).to_be_empty()
    expect(getFormFields(page).get("dateOfBirth")).to_be_empty()
    expect(getFormFields(page).get("city")).to_be_empty()
    expect(getFormFields(page).get("website")).to_be_empty()
    expect(getFormFields(page).get("intro")).to_be_empty()
    expect(getFormFields(page).get("occupation")).to_have_value("")
    expect(getFormFields(page).get("experienceYears")).to_have_value("")
    expect(getFormFields(page).get("favoriteBrowser")).to_have_value("")    


    printAccessibilityTree(page)

def validateSubmitForm(page):
    submitButton = page.get_by_role("button", name="Submit registration")
    submitButton.scroll_into_view_if_needed()
    submitButton.highlight()
    submitButton.click()
    expect(getFormFields(page).get("my_dialog")).to_be_visible()
    expect(getFormFields(page).get("h2_heading")).to_have_text(REGISTRATION_FORM.get('submitDialogHeading'))
    getFormFields(page).get("closeDialogButton").click()
    expect(getFormFields(page).get("my_dialog")).to_be_hidden()






def registrationLink(page):
    registrationLink = page.get_by_role("link", name="Registration")
    registrationLink.scroll_into_view_if_needed()
    registrationLink.highlight()
    registrationLink.click()
    targetSection = page.locator(REGISTRATION_FORM.get('registrationTargetSection'))
    expect(targetSection).to_be_in_viewport()


def PreferencesLink(page):
    getFormFields(page).get("PreferencesLink").scroll_into_view_if_needed()
    getFormFields(page).get("PreferencesLink").highlight()
    getFormFields(page).get("PreferencesLink").click()
    targetSection = page.locator(REGISTRATION_FORM.get('preferencesTargetSection'))
    expect(targetSection).to_be_in_viewport()


def helpLink(page):
    helpLink = page.get_by_role("link", name="Help")
    helpLink.scroll_into_view_if_needed()
    helpLink.highlight()
    helpLink.click()

    #printAccessibilityTree(page)
    dialog = page.get_by_role("dialog", name=REGISTRATION_FORM["modalHeaderText"])
    expect(dialog).to_be_visible()
    expect(dialog.get_by_role("heading", level=2, name=REGISTRATION_FORM.get("modalHeaderText"))).to_be_visible()

    dialogOkButton = dialog.get_by_role("button", name=REGISTRATION_FORM.get("modalButtonText"))
    expect(dialogOkButton).to_be_visible()
    expect(dialogOkButton).to_be_enabled()
    dialogOkButton.click()

def PlaywrightDocsLink(page):
    PlaywrightDocsLink = getFormFields(page).get("PlaywrightDocsLink")
    PlaywrightDocsLink.scroll_into_view_if_needed()
    PlaywrightDocsLink.highlight()
    with page.context.expect_page() as new_page_info:
        PlaywrightDocsLink.click()
    new_page = new_page_info.value
    new_page.wait_for_load_state()
    expect(new_page).to_have_url(REGISTRATION_FORM.get("playwrightDocsLink"))
    expect(new_page.get_by_role("heading", name=REGISTRATION_FORM.get("playwrightDocsHeading"))).to_be_visible()



def getFormFields(page):
    return {
        "registrationLink": page.get_by_role("link", name = "Registration" ),
        "firstName":    page.get_by_role("textbox", name="First name"),
        "lastName":     page.get_by_role("textbox", name="Last name"),
        "email":        page.get_by_role("textbox", name="Email address *", exact=True),
        "emailConfirm": page.get_by_role("textbox", name="Confirm email address"),
        "password":     page.get_by_label("Password"),
        "phone":        page.get_by_role("textbox", name="Phone number"),
        "dateOfBirth":  page.get_by_label("Date of birth"),
        "city":         page.get_by_role("textbox", name="City"),
        "website":      page.get_by_role("textbox", name="Personal website"),
        "intro":        page.get_by_role("textbox", name="Short introduction"),
        "country":      page.get_by_role("combobox", name="Country"),
        "occupation":   page.get_by_role("combobox", name="Occupation"),
        "experienceYears": page.get_by_role("combobox", name="Years of experience"),
        "favoriteBrowser": page.get_by_role("combobox", name="Favorite browser"),
        "subscribe":    page.get_by_role("checkbox", name=REGISTRATION_FORM.get("Subscribe"), exact=True),
        "termsAndConditions": page.get_by_role("checkbox", name=REGISTRATION_FORM.get("termsAndConditions"), exact=True),
        "resetFormButton": page.get_by_role("button", name=REGISTRATION_FORM.get("resetFormButtonName"), exact=True),
        "my_dialog": page.get_by_role("dialog"),
        "h2_heading": page.get_by_role("dialog").get_by_role("heading", level=2),
        "closeDialogButton": page.get_by_role("button", name= "Close", exact=True),
        "PreferencesLink": page.get_by_role("link", name="Preferences"),
        "PlaywrightDocsLink": page.get_by_role("link", name="Playwright documentation")

    }
