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
    CREATED_COMPANY = (By.CSS_SELECTOR, "[class*='nameCell-module-campaignNameLink']")
    SEGMENTS = (By.CSS_SELECTOR, "[class*='center-module-segments']")


class ProfileInfoLocators:
    FIO = (By.CSS_SELECTOR, "[data-name='fio'] > div > input")
    MOBILE = (By.CSS_SELECTOR, "[data-name='phone'] > div > input")
    SAVE = (By.CSS_SELECTOR, ".button_submit > div")

class CreateCompanyPageLocators:
    REACH = (By.CSS_SELECTOR, "column-list-item._reach")
    COVERAGE = (By.CSS_SELECTOR, "[class*='right-wrap'] > [class*='column-list']  > [class*='_reach']")
    URL_ADVERTISE = (By.XPATH, "//input[@placeholder='Введите ссылку']")
    BANNER = (By.ID, "patterns_banner_4")
    # UPLOAD_PICTURE = (By.XPATH, "//input[@data-test='overlay_240x400']")
    # UPLOAD_PICTURE = (By.CSS_SELECTOR, "[data-test*='overlay']")
    # UPLOAD_PICTURE = (By.CSS_SELECTOR, "overlay_240x400")
    UPLOAD_PICTURE = (By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[6]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div/div/div[2]/input")
    SAVE_PICTURE = (By.CSS_SELECTOR, "[class*='image-cropper__save']")
    SAVE_COMPANY = (By.CSS_SELECTOR, "[class*='footer__button js-save-button-wrap'] > button > div")
    COMPANY_NAME = (By.XPATH, "//div[@class='input input_campaign-name input_with-close']/div[2]/input")
    DATE_FROM = (By.CSS_SELECTOR, "[class*='date-setting__date-from'] > input")
    DATE_TO = (By.CSS_SELECTOR, "[class*='date-setting__date-to'] > input")
    BUDGET_PER_DAY = (By.CSS_SELECTOR, "[data-test= 'budget-per_day']")
    BUDGET_TOTAL = (By.CSS_SELECTOR, "[data-test= 'budget-total']")

class SegmentPageLocators:
    CREATE_SEGMENT_MAIN = (By.XPATH, "//div[@class='page_segments__instruction-wrap js-instruction-wrap']//a")
    CHECKBOX = (By.CSS_SELECTOR, "[class*='__checkbox']")
    ADD_SEGMENT = (By.CSS_SELECTOR, "[class*='__btn-wrap js-add'] > button > div")
    CREATE_SEGMENT_FINAL = (By.CSS_SELECTOR, "[class*='__btn-wrap js-create'] > button > div")