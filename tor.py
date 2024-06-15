import pyautogui
import keyboard
import time
from PIL import Image
import pytesseract
import pygetwindow as gw


def check_date(date_to_check, image_path='google.png'):
    """
    Check if the given date is present in the text extracted from the screenshot.
    """
    text = pytesseract.image_to_string(Image.open(image_path))
    return date_to_check in text


def screen_shot(window_title="Google Chrome", save_path='google.png'):
    """
    Take a screenshot of the specified window and save it.
    """
    window = gw.getWindowsWithTitle(window_title)[0]
    x, y, width, height = window.left, window.top, window.width, window.height
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    screenshot.save(save_path)


def find_image(path, confidence=0.9):
    """
    Locate the center of an image on the screen with a given confidence level.
    """
    return pyautogui.locateCenterOnScreen(path, confidence=confidence)


def click_on_element(element):
    """
    Move the mouse to the specified element and click it.
    """
    pyautogui.moveTo(element.x, element.y, duration=0.5)
    time.sleep(0.3)
    pyautogui.click()
    time.sleep(0.3)


def send_input(text):
    """
    Type the given text using the keyboard.
    """
    keyboard.write(text)
    time.sleep(0.7)


def perform_task_sequence(bday,city,id_number,date_to_check):
    """
    Perform a sequence of tasks to get the required information.
    """
    try:
        click_on_element(find_image("./assets/type_of_tor.PNG"))
        click_on_element(find_image("./assets/tor_shinanit.PNG"))
        click_on_element(find_image("./assets/bday.PNG"))
        send_input(bday)
        pyautogui.press('enter')
        time.sleep(1)
        
        click_on_element(find_image("./assets/choose_from_list.PNG"))
        click_on_element(find_image("./assets/shinanit.PNG"))
        time.sleep(2)
        
        click_on_element(find_image("./assets/search_for_city.PNG"))
        send_input(city)
        time.sleep(1)
        
        click_on_element(find_image("./assets/ramat_gan.PNG"))
        time.sleep(1)
        
        click_on_element(find_image("./assets/continue_step_2.PNG"))
        time.sleep(10)
        pyautogui.scroll(-500)
        time.sleep(1)
        
        screen_shot()
        
        if check_date(date_to_check):
            click_on_element(find_image("./assets/bhar.PNG"))
            time.sleep(1)
            
            click_on_element(find_image("./assets/taz_of_tor_owner.PNG"))
            send_input(id_number)
            time.sleep(1)
            
            click_on_element(find_image("./assets/hamsheh.PNG"))
            time.sleep(4)
            
            click_on_element(find_image("./assets/read_and_allow.PNG", confidence=0.7))
            time.sleep(1)
            
            click_on_element(find_image("./assets/continue_for_tor.PNG"))
        else:
            pyautogui.scroll(+500)
            print("NO DATE AVAILABLE")
            pyautogui.press("f5")
            time.sleep(4)
            perform_task_sequence(bday,city,id_number,date_to_check)
    except Exception as e:
        print(f"Error: {e}")
        perform_task_sequence(bday,city,id_number,date_to_check)


if __name__ == "__main__":
    bday = "27071999"
    city = "רמת גן"
    id_number = "207888355"
    date_to_check = '15/06/2024'
    perform_task_sequence(bday,city,id_number,date_to_check)
