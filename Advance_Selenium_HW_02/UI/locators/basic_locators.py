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
    USER_NAME = (By.CSS_SELECTOR, "[class*='userNameWrap']")
    CREATE_CAMPAIGN = (By.XPATH, "//div[contains(@class, 'createButtonWrap')]/div/div")
    CREATED_CAMPAIGN = (By.CSS_SELECTOR, "[class*='campaignNameLink']")
    SEGMENTS = (By.CSS_SELECTOR, "[class*='segments']")


class ProfileInfoLocators:
    FIO = (By.CSS_SELECTOR, "[data-name='fio'] > div > input")
    MOBILE = (By.CSS_SELECTOR, "[data-name='phone'] > div > input")
    SAVE = (By.CSS_SELECTOR, ".button_submit > div")


class CreateCampaignPageLocators:
    REACH = (By.CSS_SELECTOR, "column-list-item._reach")
    COVERAGE = (By.CSS_SELECTOR, "[class*='right-wrap'] > [class*='column-list']  > [class*='_reach']")
    URL_ADVERTISE = (By.XPATH, "//input[@data-gtm-id='ad_url_text']")
    BANNER = (By.ID, "patterns_banner_4")
    UPLOAD_PICTURE = (By.CSS_SELECTOR, "[data-test*='image']")
    SAVE_PICTURE = (By.CSS_SELECTOR, "[class*='image-cropper__save']")
    SAVE_CAMPAIGN = (By.XPATH, "//div[contains(@class, 'js-save-button-wrap')]/button/div")
    CAMPAIGN_NAME = (By.XPATH, "//div[contains(@class,'input_with-close')]/div[2]/input")
    DATE_FROM = (By.CSS_SELECTOR, "[class*='date-from'] > input")
    DATE_TO = (By.CSS_SELECTOR, "[class*='date-to'] > input")
    BUDGET_PER_DAY = (By.CSS_SELECTOR, "[data-test= 'budget-per_day']")
    BUDGET_TOTAL = (By.CSS_SELECTOR, "[data-test= 'budget-total']")


class SegmentPageLocators:
    CREATE_SEGMENT_MAIN = (By.XPATH, "//div[contains(@class,'js-instruction-wrap')]//a")
    CREATE_SEGMENT_IF_EXIST = (By.CSS_SELECTOR, "[class*='__btn']>button")
    CHECKBOX = (By.CSS_SELECTOR, "[class*='__checkbox']")
    ADD_SEGMENT = (By.CSS_SELECTOR, "[class*='__btn-wrap js-add'] > button > div")
    CREATE_SEGMENT_FINAL = (By.CSS_SELECTOR, "[class*='js-create'] > button > div")
    SEGMENT_NAME = (By.XPATH, "//div[@class='js-segment-name']//input")
    SEGMENT_IN_TABLE = (By.CSS_SELECTOR, "[class*='cells-module-nameCell'] > a")
    REMOVE_CELL = (By.CSS_SELECTOR, "[class*='remove']")
    CONFIRM_DELETE = (By.CSS_SELECTOR, "[class*='button_confirm']")
    CHECKBOX_SEGMENTS = (By.CSS_SELECTOR, "[class*='idCellCheckbox']")
    ACTION_BUTTON = (By.CSS_SELECTOR, "[class*='selectItem']")
    DELETE_ACTION = (By.CSS_SELECTOR, "[data-test='remove']")
