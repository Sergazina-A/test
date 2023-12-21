from appium.webdriver.common.mobileby import MobileBy


def locators():
    locator_dict = {
    'login/registration': (MobileBy.ACCESSIBILITY_ID, 'Вход/Регистрация'),
    # 'login_text_editor': (MobileBy.XPATH, "//android.widget.EditText[@bounds='[48,706][672,802]']"),
    'login_text_editor2': (MobileBy.XPATH, "//android.widget.EditText[@text='+7']"),
    'pass_text_editor': (MobileBy.XPATH, "//android.widget.EditText[@bounds='[48,612][672,708]']"),
    'login_button': (MobileBy.ACCESSIBILITY_ID, "Войти"),
    'open_new_depoz_or_schet': (MobileBy.ACCESSIBILITY_ID, "Открыть новый депозит или счет"),
    'close': (MobileBy.ACCESSIBILITY_ID, "Маска"),
    'telefon-parol': (MobileBy.ACCESSIBILITY_ID, "Телефон Пароль"),
    'thirdexample': (MobileBy.XPATH, "//android.widget.EditTxt[@bounds='[0,100][720,1094]']"),
    }
    return locator_dict

