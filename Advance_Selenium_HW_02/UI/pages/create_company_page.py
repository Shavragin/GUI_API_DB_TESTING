import datetime
import os
import random
import allure

import numpy
from PIL import Image

from UI.locators.basic_locators import CreateCompanyPageLocators
from UI.pages.base_page import BasePage


def date():
    today = datetime.date.today()
    return f"{today.day}.{today.month}.{today.year}"


def random_url():
    return f"http://company{random.randint(0, 1000)}.ru"


def random_company():
    return f"Company{random.randint(0, 100000)}"


def create_image(temp_dir):
    imarray = numpy.random.rand(400, 600, 3) * 600
    im = Image.fromarray(imarray.astype('uint8')).convert('RGBA')
    dir = os.path.join(temp_dir, 'result_image.png')
    im.save(dir)
    return dir


class CreateCompanyPage(BasePage):
    url = "https://target.my.com/campaign/new"
    locator = CreateCompanyPageLocators()

    @allure.step("Creating company")
    def create_company(self, ):
        self.logger.info("Save company")
        self.clicking(self.locator.SAVE_COMPANY)

    def fill_random_url(self):
        self.logger.info("Adding URL")
        self.clicking(self.locator.COVERAGE)
        URL = self.find(self.locator.URL_ADVERTISE)
        URL.send_keys(random_url())

    def pick_banner(self):
        self.logger.info("Picking banner")
        banner = self.find(self.locator.BANNER)
        self.scroll_to(banner)
        banner.click()

    def upload_picture(self, temp_dir):
        self.logger.info("Uploading picture")
        upload_picture = self.find(self.locator.UPLOAD_PICTURE)
        self.scroll_to(upload_picture)
        image = create_image(temp_dir)
        upload_picture.send_keys(image)
        self.clicking(self.locator.SAVE_PICTURE)

    def fill_date(self):
        self.logger.info("Adding dates")
        self.find(self.locator.DATE_FROM).send_keys(date())
        self.find(self.locator.DATE_TO).send_keys(date())

    def fill_budget(self):
        self.logger.info("Adding budget")
        self.find(self.locator.BUDGET_PER_DAY).send_keys("100")
        self.find(self.locator.BUDGET_TOTAL).send_keys("100")

    def fill_random_company(self):
        self.logger.info("Adding company name")
        self.find(self.locator.COMPANY_NAME).clear()
        self.company = random_company()
        self.find(self.locator.COMPANY_NAME).send_keys(self.company)

    @allure.step("Filling information")
    def fill_information(self, temp_dir):
        self.fill_random_url()
        self.pick_banner()
        self.upload_picture(temp_dir)
        self.fill_date()
        self.fill_budget()
        self.fill_random_company()
