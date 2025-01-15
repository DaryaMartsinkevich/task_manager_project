import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def test_login_and_add_to_cart():
    # Настройка WebDriver
    options = Options()
    options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Шаг 1: Перейти на страницу логина
        driver.get("https://www.saucedemo.com")

        # Шаг 2: Ввести данные для авторизации
        username = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        login_button.click()

        # Шаг 3: Проверить, что пользователь на странице инвентаря
        assert "inventory" in driver.current_url, "Не удалось перейти на страницу инвентаря"

        # Шаг 4: Добавить товар в корзину
        product_name = "Sauce Labs Backpack"  # Название товара
        add_to_cart_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        # import pdb
        # pdb.set_trace()
        add_to_cart_button.click()

        # Шаг 5: Проверить, что товар добавлен (значок корзины)
        cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert cart_badge.text == "1", "Товар не добавлен в корзину"

        # Шаг 6: Перейти в корзину
        cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_icon.click()

        # Шаг 7: Проверить, что в корзине отображается добавленный товар
        cart_item_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
        assert cart_item_name == product_name, f"Ожидался товар '{product_name}', но найден '{cart_item_name}'"

        # Шаг 8: Перейти к оформлению покупки
        checkout = driver.find_element(By.ID, 'checkout')
        checkout.click()
        # import pdb
        # pdb.set_trace()
        assert driver.current_url == 'https://www.saucedemo.com/checkout-step-one.html', 'Неверный URL'

        # Шаг 9: Вводим валидные данные
        first_name = driver.find_element(By.ID, 'first-name')
        last_name = driver.find_element(By.ID, 'last-name')
        postal_code = driver.find_element(By.ID, 'postal-code')
        continue_button = driver.find_element(By.ID, 'continue')

        first_name.send_keys('Darya')
        last_name.send_keys('Ivanova')
        postal_code.send_keys('1234565')
        continue_button.click()

        # Шаг 10: Проверяем URL
        # import pdb
        # pdb.set_trace()
        assert driver.current_url == 'https://www.saucedemo.com/checkout-step-two.html', 'Неверный URL'

        # Шаг 11: Проверяем наличие товара в заказе
        item_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
        assert item_name == product_name

    finally:
        # Закрытие браузера
        driver.quit()
