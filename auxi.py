import pyautogui as pa

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