from playwright.sync_api import sync_playwright
import time, os, random

path_project = os.path.dirname(__file__)

def get_random_line_and_remove(file_path):
    with open(file_path, 'r', encoding='utf-8') as file: lines = file.readlines()
    if not lines: return None
    chosen_line = random.choice(lines).strip()
    lines.remove(chosen_line + '\n')
    with open(file_path, 'w', encoding='utf-8') as file: file.writelines(lines)
    return chosen_line

def seguir(playwright):

    pathlocal = os.getenv('LOCALAPPDATA')
    user_data_dir = os.path.join(pathlocal,"Google\\Chrome\\User Data")
    browser = playwright.chromium.launch_persistent_context(
        user_data_dir,
        headless=False,
        executable_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    )

    page = browser.new_page()

    meme_page = get_random_line_and_remove(os.path.join(path_project,'data/meme_pgs.txt'))

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