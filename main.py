# Python Docs: https://docs.python.org
# Selenuim Docs: https://www.selenium.dev/documentation/
# Start here: https://www.selenium.dev/documentation/webdriver/getting_started/first_script/
from selenium import webdriver
from selenium.webdriver.common.by import By

def try_automate():
    # Starting session on a browser(you can select multiple)
    # Choices: Chrome, Edge, IE, Safari, Firefox
    driver = webdriver.Chrome()

    # navigating to a web page
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    # requesting driver information
    title = driver.title
    print(f"Title: {title}")

    # establish wating strategy
    driver.implicitly_wait(0.5)

    # find an element
    text_box = driver.find_element(by=By.NAME, value="my-text")
    text_area = driver.find_element(by=By.NAME, value="my-textarea")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

    # clear inputs
    text_box.clear()
    text_area.clear()

    # adding info in input areas
    some_text = "This is a test"
    some_paragraph = "Lorem Ipsum something something"

    text_box.send_keys(some_text)
    text_area.send_keys(some_paragraph)

    # take action on the element
    submit_button.click()

    # requesting element information
    message = driver.find_element(by=By.ID, value="message")
    text = message.text

    print(f"Text: {text}")

    driver.quit()

def main():
    try_automate()

if __name__ == "__main__":
    main()