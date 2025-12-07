import pyautogui, keyboard

hasToClick = False;

print('Clicando!')

while True:
    if keyboard.is_pressed('f7'):
        hasToClick = False
    if keyboard.is_pressed('f8'):
        print("clicou fora do loop")
        hasToClick = True
        
    while hasToClick:
        if keyboard.is_pressed('f7'):
            break

        currentX, currentY = pyautogui.position();
        pyautogui.click(currentX, currentY)
        
        if keyboard.is_pressed('f8'):
            print("clicou no loop")
            hasToClick = False