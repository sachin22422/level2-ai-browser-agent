# get_mouse_pos.py
import pyautogui
import time

print("🕒 You have 10 seconds to hover your mouse over the element...")
for i in range(10, 0, -1):
    print(f"⏳ {i} seconds remaining...")
    time.sleep(1)

x, y = pyautogui.position()
print(f"📍 Your mouse is at: ({x}, {y})")
