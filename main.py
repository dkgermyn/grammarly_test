from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

if __name__ == '__main__':
    # create a new chrome webdriver with the Grammarly extension added
    chrome_options = webdriver.ChromeOptions()
    chrome_extension_path = "kbfnbcaeplbcioakkpcpgfkobkghlhen-14.1006.0-Crx4Chrome.com.crx"
    chrome_options.add_extension(chrome_extension_path)
    driver = webdriver.Chrome(options=chrome_options)

    # open the grammarly extension
    driver.get("chrome-extension://kbfnbcaeplbcioakkpcpgfkobkghlhen/src/popup.html")

    # the extension opens a new javascript page to sign up or sign in
    # we need to switch to it first
    WebDriverWait(driver, 20).until(ec.number_of_windows_to_be(2))
    windows = driver.window_handles
    pop_up_window = windows[1]
    driver.switch_to.window(pop_up_window)

    # now, sign in with an existing grammarly account
    sign_in_link = driver.find_element_by_class_name("_1CcgG-link")
    sign_in_link.click()

    # sign in window flow below
    # we'll use my e-mail address and a dummy password
    # here, i would prefer to use a page object model, but this is a tech interview
    # and i don't want to create more than one script, as mentioned in the requirements
    email_address_text_field = driver.find_element_by_css_selector("input[data-qa='txtEmail']")
    email_address_text_field.send_keys("kgermyn@gmail.com")
    continue_button = driver.find_element_by_css_selector("button[data-qa='btnLogin']")
    continue_button.click()
    password_input_field = driver.find_element_by_css_selector("input[data-qa='txtPassword']")
    WebDriverWait(driver, 20).until((ec.element_to_be_clickable((By.CSS_SELECTOR, "input[data-qa='txtPassword']"))))
    password_input_field.click()
    password_input_field.send_keys("!Q@W3e4r")
    login_button = driver.find_element_by_css_selector("button[data-qa='btnLogin']")
    login_button.click()

    # i used this code to automate the process of signing up for a new account before realizing that i could just use
    # an existing account to login to grammarly
    # left the code here for posterity

    # sign up for a grammarly account
    # email_input_field = driver.find_element_by_css_selector("input[data-qa='txtSignupEmail']")
    # email_input_field.click()
    # email_input_field.send_keys("kgermyn@gmail.com")
    # password_input_field = driver.find_element_by_css_selector("input[data-qa='txtSignupPassword']")
    # password_input_field.click()
    # password_input_field.send_keys("!Q@W3e4r")
    # username_input_field = driver.find_element_by_css_selector("input[data-qa='txtSignupName']")
    # WebDriverWait(driver, 20).until((EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-qa='txtSignupName']"))))
    # username_input_field.click()
    # username_input_field.send_keys("GrammarlyAutomationTest")
    # agree_and_sign_up_button = driver.find_element_by_css_selector("button[data-qa='btnSignupSubmit']")
    # # WebDriverWait(driver, 20).until((EC.element_to_be_clickable
    # ((By.CSS_SELECTOR, "input[data-qa='btnSignupSubmit']"))))
    # agree_and_sign_up_button.click()

    # the fact that we just logged in verifies that grammarly is working
    expected_grammarly_url = "https://app.grammarly.com/"
    WebDriverWait(driver, 20).until(ec.url_matches(expected_grammarly_url))
    # again, if not a single script, we could add hooks here for Robot Framework, Cucumber, etc.
    # for now a simple assertion will work
    assert ec.url_matches(expected_grammarly_url), "FAIL : Grammarly Extension not working as intended"

    # how do we verify that the plugin ISN'T working?
    """
    I'm a bit unclear on the instructions here.  The request is two test cases :
    1) Verify that the extension is working as intended -- this is straightforward
    2) Verify that the extension is not working as intended -- language unclear here
    
    Do we mean that "verify the extension is not working, because we disabled it, therefore it's not working
    as we intended"?
    
    Or do we mean that "verify the extension isn't working, even though it's enabled, 
    so it's not working "as intended"?
    
    To test the former, you could spin up a chrome WebDriver WITHOUT passing in chrome_options,
    some check or assert when we attempted to open the chrome extension popup.html URL would
    validate that we were unable to open the extension, therefore it's not enabled
    
    To test the latter seems redundant : if the "verify extension works as intended" script passes,
    then it follows, the "verify extension isn't working" script will fail, and vice versa
    """
    driver.quit()
