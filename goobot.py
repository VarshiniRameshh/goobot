from time import sleep
import undetected_chromedriver.v2 as uc
from selenium.webdriver.chrome.options import Options
from undetected_chromedriver.options import ChromeOptions
from selenium.common.exceptions import NoSuchElementException
import datetime
import time
from pyfiglet import Figlet
from termcolor import colored, cprint

f = Figlet(font='isometric2')
print(colored(f.renderText('GOO BOT'), 'green'))

f = Figlet(font='standard')
print(colored(f.renderText('BY:VARSHINI RAMESH & SURYA.V'), 'yellow'))

now = datetime.datetime.now()
current_time = now.strftime("%H:%M / %A")

justtime = now.strftime("%H:%M")
print (current_time)

if __name__ == '__main__':
    username = "varsur1420"
    password = "varshinisurya"

    driver = uc.Chrome()
    driver.delete_all_cookies()
    driver.get(
        'https://accounts.google.com/signin/v2/identifier?hl=en-GB&continue=https%3A%2F%2Fwww.google.com%3Fhl%3Den-GB&ec=GAlA8wE&flowName=GlifWebSignIn&flowEntry=AddSession')
    sleep(2)

    driver.find_element_by_xpath('//input[@type="email"]').send_keys(username)

    driver.find_element_by_xpath('//*[@id="identifierNext"]').click()

    sleep(2)

    driver.find_element_by_xpath('//input[@type="password"]').send_keys(password)
    driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
    sleep(2)
    driver.get('https://meet.google.com/sda-ftmj-xki')
    sleep(20)

    def meet_redirect():
        try:
            driver.find_element_by_xpath(
                "//span[contains(text(),'Ask to join')]").click()
            sleep(300)
        except NoSuchElementException:
            if driver.find_element_by_xpath("//span[contains(text(),'Join now')]"):
                driver.find_element_by_xpath(
                    "//span[contains(text(),'Join now')]").click()
                sleep(30)

        except NoSuchElementException:
            pass

    meet_redirect()

    def browser():

        chromeOptions = ChromeOptions()
        chromeOptions.add_argument("--no-sandbox")
        chromeOptions.add_argument("--headless")
        chromeOptions.add_argument("--disable-infobars")
        chromeOptions.add_argument("--disable-gpu")
        chromeOptions.add_argument("--disable-extensions")
        chromeOptions.add_argument("--mute-audio")
        chromeOptions.add_experimental_option(
            'excludeSwitches', ['enable-logging'])
        chromeOptions.add_experimental_option("prefs",
                    {"profile.default_content_setting_values.media_stream_mic": 2,
                    "profile.default_content_setting_values.media_stream_camera": 2,
                    "profile.default_content_setting_values.geolocation": 2,
                    "profile.default_content_setting_values.notifications": 2
                    })
    browser()

    driver = uc.Chrome(ChromeOptions=ChromeOptions)

    def endMeet():

        endButton = driver.find_element_by_css_selector(endButtonPath)
        endButton.click()
    print(colored(f"\nSuccessfully ended Google Meet #{meetIndex} @{timeStamp()}\n", "red"), end="")