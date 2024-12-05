from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
import time

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
    github_right_menu = driver.find_element(By.CSS_SELECTOR, ".AppHeader-user button")
    github_wait_menu = WebDriverWait(driver, 10.0).until(EC.visibility_of(github_right_menu))

    print(f"GITHUB RIGHT MENU IS CLICKED!: {github_right_menu}")

   


    # driver.get("https://github.com/logout")

    # github_final_logout = driver.find_element(By.NAME, "commit")

    # print(f"{github_final_logout}")

    # Navigation sequence
    github_right_menu.click()

    # github_user_repo = driver.find_element(By.CSS_SELECTOR, ".List__ListBox-sc-1x7olzq-0 .gajtZp a")
    github_user_repo = driver.find_element(By.CSS_SELECTOR, ".gajtZp a")
    # github_user_repo = driver.find_element(By.CSS_SELECTOR, "il:nth-child(3n) a")

    github_wait_repo = WebDriverWait(driver, 10.0).until(EC.visibility_of(github_user_repo))

    # github_user_repo = locate_with(By.TAG_NAME, "a").near({By.CSS_SELECTOR: ".List__ListBox-sc-1x7olzq-0 .gajtZp"})

    print(f"GITHUB USER REPO IS CLICKED!: {github_user_repo}")


    github_user_repo.click()
    # TODO: right menu not executing again
    # github_right_menu.click()

    time.sleep(15)

    driver.get("https://github.com/logout")

    # TODO: find a way to select the logout button on the right menu
    # github_user_logout = driver.find_element(By.CSS_SELECTOR, ".List__ListBox-sc-1x7olzq-0 li:last-child a")
    # github_user_logout = driver.find_element(By.CSS_SELECTOR, "ul:last-child a")

    # github_wait_logout = WebDriverWait(driver, 10.0).until(EC.visibility_of(github_user_logout))

    # print(f"{github_user_logout}")

    github_final_logout = driver.find_element(By.NAME, "commit")

    github_wait_final_logout = WebDriverWait(driver, 10.0).until(EC.visibility_of(github_final_logout))

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
