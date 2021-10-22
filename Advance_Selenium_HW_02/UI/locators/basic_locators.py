from selenium.webdriver.common.by import By


class LoginPageLocators:
    ENTER_BUTTON = (By.CSS_SELECTOR, "[class*='responseHead-module-button']")
    EMAIL_FIELD = (By.NAME, "email")
    PASSWORD_FIELD = (By.NAME, "password")
    LOG_IN_BUTTON = (By.CSS_SELECTOR, "[class*='authForm-module-button']")


class DashboardPageLocators:
    TITLE = (By.CSS_SELECTOR, "[class*='instruction-module-title']")
    ACCOUNT = (By.CSS_SELECTOR, "[class*='right-module-rightWrap']")
    EXIT = (By.CSS_SELECTOR, "[href='/logout']")
    AUDIENCE = (By.CSS_SELECTOR, "[class*='center-module-segments']")
    BILLING = (By.CSS_SELECTOR, "[class*='center-module-billing']")
    PROFILE = (By.CSS_SELECTOR, "[href='/profile']")
    USER_NAME = (By.CSS_SELECTOR, "[class*='right-module-userNameWrap']")
    CREATE_COMPANY = (By.CSS_SELECTOR, "[class*=dashboard-module-createButtonWrap] > div > div")


class ProfileInfoLocators:
    FIO = (By.CSS_SELECTOR, "[data-name='fio'] > div > input")
    MOBILE = (By.CSS_SELECTOR, "[data-name='phone'] > div > input")
    SAVE = (By.CSS_SELECTOR, "button.button_submit > div")

class CreateCompanyPageLocators:
    REACH = (By.CSS_SELECTOR, "column-list-item._reach")
