from playwright.sync_api import sync_playwright
import pyautogui as pa, os, json, shutil
from pathlib import Path
from datetime import datetime
from auxi import wait_for_img

nome_arq,desc = "", ""
path_project = os.path.dirname(__file__)
with open(os.path.join(path_project,'config.json'), 'r') as cc: config_json = json.load(cc)
pasta = os.path.join(path_project,config_json['toupload_folder'])
pasta_postado = os.path.join(path_project,config_json['uploaded_folder'])
arquivos = sorted(Path(pasta).iterdir(), key=os.path.getmtime, reverse=True)


if len(arquivos) > 0:
    for arquivo in arquivos:
        data_modificacao = datetime.fromtimestamp(os.path.getmtime(arquivo))
        # print(f"{arquivo.name} - Modificado em: {data_modificacao}")
        arq_path = arquivo.name
        nome_arq = os.path.join(pasta,arq_path)
        nome_arq_postado = os.path.join(pasta_postado,arq_path)
        desc = arq_path.split(".")[:-1][0]
        print(nome_arq)
        print(desc)
        break
else:
    print("SEM ARQUIVOS PARA POSTAR!")
    quit()

# input()

def postar(playwright):
    pathlocal = os.getenv('LOCALAPPDATA')
    user_data_dir = os.path.join(pathlocal,"Google\\Chrome\\User Data")
    browser = playwright.chromium.launch_persistent_context(
        user_data_dir,
        headless=False,
        executable_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    )

    page = browser.new_page()

    page.goto("https://instagram.com")

    page.get_by_role("link", name="Nova publicação Criar").click()
    pa.sleep(2)
    page.get_by_role("button", name="Selecionar do computador").click()

    wait_for_img(os.path.join(path_project, 'data/EXPLORER_nome.png'),tempo=20,clicar=True,dx=50,dy=0)
    pa.write(nome_arq)
    pa.press('enter')

    pa.sleep(0.2)
    page.locator("button").filter(has_text="Selecionar corte").click()
    # input("Selecionar corte")
    pa.sleep(0.2)
    page.get_by_role("button", name="Original Ícone de contorno de").click()
    # input("Original Ícone de contorno de")
    pa.sleep(0.2)
    page.get_by_role("button", name="Avançar").click()
    # input("Avançar")
    pa.sleep(0.2)
    page.get_by_role("button", name="Avançar").click()
    # input("Avançar")
    pa.sleep(0.2)
    page.get_by_role("textbox", name="Escreva uma legenda...").click()
    # input("Escreva uma legenda...")
    pa.sleep(0.2)
    page.get_by_role("textbox", name="Escreva uma legenda...").fill(desc)
    # input("Escreva uma legenda...")
    pa.sleep(0.2)
    page.get_by_role("button", name="Compartilhar").click()
    # input("Compartilhar")

    pa.sleep(40)
    print("Movendo pra pasta de postados...")
    shutil.move(nome_arq, nome_arq_postado)
    print(f"{nome_arq} Postado!")

    browser.close()

with sync_playwright() as playwright: postar(playwright)