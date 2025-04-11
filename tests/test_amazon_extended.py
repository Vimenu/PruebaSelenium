import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def driver():
    driver_path = r"C:\Selenium\chromedriver.exe"
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument(r"--user-data-dir=C:\Users\ghost\AppData\Local\Google\Chrome\User Data")
    options.add_argument("--profile-directory=Profile 1")

    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    if not os.path.exists("capturas"):
        os.makedirs("capturas")

    yield driver
    driver.quit()

def captura(driver, nombre):
    path = f"capturas/{nombre}.png"
    driver.save_screenshot(path)
    print(f"[✔] Captura guardada: {path}")

def test_amazon_busqueda(driver):
    print("[...] Abriendo Amazon")
    driver.get("https://www.amazon.com/-/es/")
    time.sleep(2)
    captura(driver, "01_inicio")

    print("[...] Realizando búsqueda")
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys("wireless headphones")
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)
    captura(driver, "02_busqueda")

    print("[...] Aplicando filtro de envío gratis")
    try:
        free_shipping = driver.find_element(By.XPATH, "//span[text()='Free Shipping by Amazon']")
        free_shipping.click()
        time.sleep(3)
        captura(driver, "03_filtro_envio_gratis")
    except:
        print("[⚠] Filtro no disponible, continuando...")

    print("[...] Seleccionando producto")
    products = driver.find_elements(By.CSS_SELECTOR, ".s-title-instructions-style .a-text-normal")
    if products:
        products[0].click()
        time.sleep(3)
        captura(driver, "04_producto_seleccionado")
    else:
        pytest.fail("No se encontraron productos.")

    print("[...] Cambiando a pestaña del producto")
    driver.switch_to.window(driver.window_handles[-1])

    print("[...] Extrayendo información del producto")
    try:
        title = driver.find_element(By.ID, "productTitle").text.strip()
        price = driver.find_element(By.CSS_SELECTOR, ".a-price .a-offscreen").text.strip()
        rating = driver.find_element(By.ID, "acrPopover").get_attribute("title")
        print(f"[✔] Producto: {title}")
        print(f"[✔] Precio: {price}")
        print(f"[✔] Rating: {rating}")
        captura(driver, "05_info_producto")
    except:
        print("[⚠] No se pudo extraer la información del producto.")
        captura(driver, "05_error_info_producto")
        pytest.fail("No se pudo extraer la información del producto.")
