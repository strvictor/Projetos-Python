from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())



driver.get("https://www.altaimpressao.com.br/produtos/epson-workforce-c5710-com-bulk-ink/")