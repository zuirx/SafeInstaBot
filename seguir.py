from playwright.sync_api import sync_playwright
import time, os, random, auxi as au

path_project = os.path.dirname(__file__)

def seguir(playwright):

    browserprof = os.path.join(path_project, 'browser_profile')
    browser = playwright.chromium.launch_persistent_context(
        user_data_dir=browserprof,
        headless=False,
    )

    page = browser.new_page()

    meme_page = au.get_random_line_and_remove(os.path.join(path_project,'data/meme_pgs.txt'))

    url = 'https://instagram.com/'
    url += meme_page

    page.goto(url)

    page.get_by_role("link", name="seguidores").click()

    donenumber = 0
    for p in range(0,7):
        for n in range(0+donenumber,12+donenumber): 
            if page.locator("div:nth-child(3) > div > ._acan").nth(n).text_content() == "Seguir":
                page.locator("div:nth-child(3) > div > ._acan").nth(n).click()

            donenumber+=1
            r_time = random.uniform(0.5, 0.9)
            time.sleep(r_time)

        for a in range(0,3): page.evaluate("window.scrollBy(0, 500)")

    browser.close()

with sync_playwright() as playwright: seguir(playwright)