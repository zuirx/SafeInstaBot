from playwright.sync_api import sync_playwright
import os, json, random, time

path_project = os.path.dirname(__file__)
with open(os.path.join(path_project,'config.json'), 'r') as cc: config_json = json.load(cc)

def deseguir(playwright):

    browserprof = os.path.join(path_project, 'browser_profile')
    browser = playwright.chromium.launch_persistent_context(
        user_data_dir=browserprof,
        headless=False,
    )

    page = browser.new_page()
    page.set_default_timeout(5000)
    page.goto(f"https://www.instagram.com/{config_json['your_username']}/")
    page.get_by_role("link", name="seguindo").click()

    donenum = 0
    for t in range(0,4):
        for p in range(donenum+1,donenum+10):
            if page.locator(f"div:nth-child({p}) > div > div > div > div:nth-child(3) > div > ._acan").text_content() == "Seguindo":
                page.locator(f"div:nth-child({p}) > div > div > div > div:nth-child(3) > div > ._acan").click()
                page.get_by_role("button", name="Deixar de seguir").click()
                donenum += 1
                r_time = random.uniform(0.5, 0.9)
                time.sleep(r_time)
        print(t)
        for a in range(0,3): page.evaluate("window.scrollBy(0, 500)")

    browser.close()

with sync_playwright() as playwright: deseguir(playwright)