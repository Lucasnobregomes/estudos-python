from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    """ Main function of source code"""
    
    driver = webdriver.Chrome()
    driver.get("http://www.youtube.com")
    campoTexto = driver.find_element(By.ID, "search")
    campoTexto.send_keys("Biju")
    elem = driver.find_element(By.ID, "button")
    elem.click()

# Quando o arquivo executado for esse, ele vai chamar a funcao main
if __name__ == "__main__":
    main()
    