import pyautogui
import random
import time

def random_mouse_movement():
    width, height = pyautogui.size()
    x, y = random.randint(0, width), random.randint(0, height)
    pyautogui.moveTo(x, y, duration=random.uniform(0.5, 1.5))

def random_mouse_click():
    pyautogui.click()

def main():
    try:
        total_elapsed_time = 0
        time_threshold = float(input("Enter the time threshold in seconds: "))

        while total_elapsed_time < time_threshold:
            random_mouse_movement()
            random_mouse_click()
            sleep_duration = random.uniform(1, 5)
            total_elapsed_time += sleep_duration
            time.sleep(sleep_duration)

        print(f"Script terminated. Elapsed time: {total_elapsed_time} seconds.")
    except KeyboardInterrupt:
        print("Script terminated.")

if __name__ == "__main__":
    main()
