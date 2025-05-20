import pyautogui as pa, random

def wait_for_img(img, tempo=60, clicar=False, dx=0, dy=0, passit=False):
    print('\n- finding image:\n',img)

    while tempo != 0:
        print(' ... ', tempo);   tempo -= 1;  pa.sleep(1)
        if pa.locateOnScreen(img, confidence=0.9):
            print('found: ',img)
            if clicar:
                print('clicking: ',img)
                x, y = pa.locateCenterOnScreen(img, confidence=0.85)
                pa.click(x+dx,y+dy)
            print('\n')
            return True
            
    if passit:
        pa.sleep(2)
        if (tempo == 0): raise ValueError('! not found !')
        return False
    
def get_random_line_and_remove(file_path):
    with open(file_path, 'r', encoding='utf-8') as file: lines = file.readlines()
    if not lines: return None
    chosen_line = random.choice(lines).strip()
    lines.remove(chosen_line + '\n')
    with open(file_path, 'w', encoding='utf-8') as file: file.writelines(lines)
    return chosen_line