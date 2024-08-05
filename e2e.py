import sys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def test_scores_service():
    chrome_options = Options()

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get("http://127.0.0.1:5245/")
    score_element = driver.find_element(By.ID, "score")
    score_value = int(score_element.text)

    if 0 <= score_value <= 1000:
        driver.quit()
        return True
    else:
        driver.quit()
        return False


def main_function():
    if test_scores_service():
        sys.exit(0)
    else:
        sys.exit(-1)


if __name__ == "__main__":
    main_function()
