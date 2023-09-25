from selenium import webdriver
from selenium.webdriver.common.by import By

# URL del sitio web de Airbnb
url = "https://www.airbnb.com.ec/"

# Inicializar el controlador del navegador Chrome
driver = webdriver.Chrome()

# Abrir la página web de Airbnb
driver.get(url)

# Esperar a que la página se cargue completamente (puedes ajustar el tiempo de espera según sea necesario)
driver.implicitly_wait(10)

try:
    # Encontrar todos los elementos que coinciden con el selector CSS para los títulos
    title_elements = driver.find_elements(By.CSS_SELECTOR, "div[id^='title_']")

    # Encontrar todos los elementos que coinciden con el selector CSS para las distancias
    distance_elements = driver.find_elements(By.CSS_SELECTOR, "div[data-testid='listing-card-subtitle'] span span")

    # Encontrar todos los elementos que coinciden con el selector CSS para las fechas
    date_elements = driver.find_elements(By.CSS_SELECTOR, "div[data-testid='listing-card-subtitle'] span span")

    # Encontrar todos los elementos que coinciden con el selector CSS para los valores
    price_elements = driver.find_elements(By.CSS_SELECTOR, "div.pquyp1l span._14y1gc ._tyxjp1")

    # Recorrer y mostrar títulos, distancias, fechas y valores
    for title_element, distance_element, date_element, price_element in zip(title_elements, distance_elements, date_elements, price_elements):
        title = title_element.text
        distance = distance_element.text
        date = date_element.text
        price = price_element.text

        # Imprimir título, distancia, fecha y valor
        print("Título:", title)
        print("Distancia:", distance)
        print("Fechas:", date)
        print("Valor:", price)
        print("=" * 40)

except Exception as e:
    print("Error:", str(e))

finally:
    # Cerrar el navegador
    driver.quit()
