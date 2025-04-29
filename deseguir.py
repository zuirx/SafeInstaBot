from playwright.sync_api import sync_playwright
import os, json

path_project = os.path.dirname(__file__)
with open(os.path.join(path_project,'config.json'), 'r') as cc: config_json = json.load(cc)

def deseguir(playwright):
    pathlocal = os.getenv('LOCALAPPDATA')
    user_data_dir = os.path.join(pathlocal,"Google\\Chrome\\User Data")
    browser = playwright.chromium.launch_persistent_context(
        user_data_dir,
        headless=False,
        executable_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    )

    page = browser.new_page()
    page.set_default_timeout(5000)
    page.goto(f"https://www.instagram.com/{config_json['your_username']}/")
    
    for r in range(0,5):
        page.get_by_role("link", name="seguindo").click()
        page.locator("._ac76 > div").first.click()

        for s in range(0,11):
            try:
                page.get_by_role("button", name="Seguindo").nth(1).click()
                page.get_by_role("button", name="Deixar de seguir").click()
            except: continue

        page.reload(timeout=15000, wait_until="domcontentloaded")

        # input("OK?")

    browser.close()

with sync_playwright() as playwright: deseguir(playwright)