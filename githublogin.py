from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

# TODO Find a way to grab the elements of the profile of the user 
def git_login():
    # Loading environment variables
    load_dotenv()

    # ofcourse 
    driver = webdriver.Chrome()
    cred_user = os.getenv("MY_LOGIN")
    cred_pass = os.getenv("MY_PASS")

    driver.get("https://github.com/login")

    page_title = driver.title
    print(f"Page Title: {page_title}")

    driver.implicitly_wait(1)

    # Finding login fields
    github_login_user = driver.find_element(by=By.ID, value="login_field")

    github_login_pass = driver.find_element(by=By.ID, value="password")

    github_login_button = driver.find_element(by=By.NAME, value="commit")

    # clear inputs first
    github_login_user.clear()
    github_login_pass.clear()

    # login process
    github_login_user.send_keys(cred_user)
    github_login_pass.send_keys(cred_pass)
    github_login_button.click()

    # Inside github
    # github_right_menu = driver.find_element(by=By.CLASS_NAME, value="Button--invisible Button--medium Button Button--invisible-noVisuals color-bg-transparent p-0")

    # print(f"{github_right_menu}")

    # github_user_repo = driver.find_element(by=By.CLASS_NAME, value="Item__LiBox-sc-yeql7o-0 gajtZp")

    # print(f"{github_user_repo}")

    # github_user_logout = driver.find_element(by=By.LINK_TEXT, value="/logout")

    # print(f"{github_user_logout}")

    driver.get("https://github.com/logout")

    github_final_logout = driver.find_element(by=By.NAME, value="commit")

    print(f"{github_final_logout}")

    # Navigation sequence
    # github_right_menu.click()
    # github_user_repo.click()
    # github_right_menu.click()

    # final 2 logouts
    # github_user_logout.click()
    # github_final_logout.click()
    github_final_logout.click()

    print("User logged out!")

    driver.quit()

def main():
    # Start script
    git_login()

if __name__ == "__main__":
    main()


# Will look for other websites to log into for testing