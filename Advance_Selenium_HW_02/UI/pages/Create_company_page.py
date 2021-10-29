from UI.pages.base_page import BasePage
from UI.locators.basic_locators import CreateCompanyPageLocators
# from UI.pages.dashboard_page import DashboardPage
import random
import numpy
import os
import datetime
import time
from PIL import Image


def date():
    today = datetime.date.today()
    return f"{today.day}.{today.month}.{today.year}"

def random_url():
    return f"http://company{random.randint(0,1000)}.ru"

def random_company():
    return f"Company{random.randint(0,100000)}"


def create_image(temp_dir):
    imarray = numpy.random.rand(400, 600, 3) * 600
    im = Image.fromarray(imarray.astype('uint8')).convert('RGBA')
    dir = os.path.join(temp_dir, 'result_image.png')
    im.save(dir)
    return dir


class CreateCompanyPage(BasePage):

    url = "https://target.my.com/campaign/new"
    locator = CreateCompanyPageLocators()


    def create_company(self,):
        self.clicking(self.locator.SAVE_COMPANY)


    def fill_information(self, temp_dir):
        self.clicking(self.locator.COVERAGE)
        URL = self.find(self.locator.URL_ADVERTISE)
        URL.send_keys(random_url())
        banner = self.find(self.locator.BANNER)
        self.scroll_to(banner)
        banner.click()
        upload_picture = self.find(self.locator.UPLOAD_PICTURE)
        self.scroll_to(upload_picture)
        image = create_image(temp_dir)
        upload_picture.send_keys(image)
        self.clicking(self.locator.SAVE_PICTURE)
        self.find(self.locator.DATE_FROM).send_keys(date())
        self.find(self.locator.DATE_TO).send_keys(date())
        self.find(self.locator.BUDGET_PER_DAY).send_keys("100")
        self.find(self.locator.BUDGET_TOTAL).send_keys("100")
        self.find(self.locator.COMPANY_NAME).clear()
        company = random_company()
        self.find(self.locator.COMPANY_NAME).send_keys(company)
        return company

