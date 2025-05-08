import pytest
from appium import webdriver
from appium.options.ios import XCUITestOptions

@pytest.fixture(scope="session")
def driver():
    options = XCUITestOptions()
    options.platform_name = "iOS"
    options.platform_version = "18.4.1"
    options.device_name = "iPhone X"
    options.udid = "00008020-000445CC0E99002E"
    options.bundle_id = "com.securenettech.smartlink7"

    # Use set_capability for custom caps not covered by properties
    options.set_capability("automationName", "XCUITest")
    options.set_capability("xcodeOrgId", "3JLG8N5656")
    options.set_capability("xcodeSigningId", "iPhone Developer")
    options.set_capability("usePrebuiltWDA", True)
    options.set_capability("useNewWDA", False)
    options.set_capability("appium:useClassChain", True)

    driver = webdriver.Remote("http://localhost:4723", options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
