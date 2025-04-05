import subprocess
import pyautogui
import webbrowser
import time
import os
import pyperclip
import win32gui
import win32print

# Enable PyAutoGUI fail-safe to allow mouse escape
pyautogui.FAILSAFE = True

# Directory where image assets are stored
ASSET_DIR = os.path.join(os.path.dirname(__file__), 'assets')

def launch_chrome_with_proxy_and_extension():
    chrome_path = r"C:\Users\Sachin Gupta\AppData\Local\Google\Chrome\Application\chrome.exe"
    extension_path = os.path.abspath("my_extension")  # Ensure this folder contains a valid extension
    proxy = os.getenv("CHROME_PROXY")  # Read proxy from environment variable

    chrome_args = [
        chrome_path,
        "--new-window",
        "--disable-popup-blocking",
        f"--load-extension={extension_path}"
    ]

    if proxy:
        chrome_args.append(f"--proxy-server={proxy}")
        print(f"🌐 Proxy enabled: {proxy}")
    else:
        print("🚫 No proxy set. Continuing without it.")

    print("🧠 Launching Chrome with proxy + extension...")
    subprocess.Popen(chrome_args)

def get_display_scale():
    # Detect the current Windows display scale (100%, 125%, etc.)
    hdc = win32gui.GetDC(0)
    dpi = win32print.GetDeviceCaps(hdc, 88)
    scale = int(dpi / 96 * 100)
    return str(scale)

def get_fallback_coords(name):
    display_scale = get_display_scale()

    coords_map = {
        "email field": {
            "100": (972, 253),
            "125": (960, 323),
            "150": (947, 387),
            "175": (943, 445)
        },
        "password field": {
            "100": (948, 292),
            "125": (939, 370),
            "150": (958, 440),
            "175": (949, 516)
        },
        "sign-in button": {
            "100": (975, 347),
            "125": (964, 436),
            "150": (956, 527),
            "175": (968, 618)
        },
        "search box": {
            "100": (824, 119),
            "125": (824, 158),
            "150": (788, 188),
            "175": (893, 229)
        }
    }

    return coords_map.get(name, {}).get(display_scale, None)

def highlight_click(x, y):
    pyautogui.moveTo(x, y)
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(0.2)

def find_and_click(images, fallback_coords=None, confidence=0.7, name="element"):
    for image_name in images:
        path = os.path.join(ASSET_DIR, image_name)
        try:
            location = pyautogui.locateCenterOnScreen(path, confidence=confidence)
            if location:
                print(f"📍 Found {name} at {location}")
                highlight_click(*location)
                return True
        except Exception:
            continue

    if fallback_coords:
        print(f"⚠️ Fallback to coordinates for {name}: {fallback_coords}")
        highlight_click(*fallback_coords)
        return True

    print(f"❌ {name} not found and no fallback provided.")
    return False

def run_amazon_login():
    launch_chrome_with_proxy_and_extension()
    time.sleep(5)

    print("🟢 Opening Amazon login page...")
    webbrowser.open("https://www.amazon.in/gp/sign-in.html")
    time.sleep(6)

    # Step 1: Enter email
    email_images = [f"amazon_email_{scale}.png" for scale in ("100", "125", "150", "175")]
    if find_and_click(email_images, fallback_coords=get_fallback_coords("email field"), name="email field"):
        pyautogui.write("sachin22422@iiitd.ac.in")
        time.sleep(0.3)
        pyautogui.press("enter")
        print("➡️ Submitted email using Enter")

        time.sleep(7)

        # Step 2: Enter password
        print("🔁 Reached password section")
        password_images = [f"amazon_password_{scale}.png" for scale in ("100", "125", "150", "175")]
        if find_and_click(password_images, fallback_coords=get_fallback_coords("password field"), name="password field"):
            time.sleep(0.5)

            pyautogui.hotkey("ctrl", "a")
            pyautogui.press("backspace")
            time.sleep(0.3)

            print("✏️ Typing password via clipboard...")
            pyperclip.copy("Amazon@123")
            pyautogui.hotkey("ctrl", "v")
            time.sleep(1.2)

            # Step 3: Sign in
            signin_images = [f"amazon_signin_{scale}.png" for scale in ("100", "125", "150", "175")]
            find_and_click(signin_images, fallback_coords=get_fallback_coords("sign-in button"), name="sign-in button")
            print("✅ Login flow complete.")

    time.sleep(6)

    # Step 4: Search product
    print("🔎 Searching for iPhone 15...")
    search_images = [f"search_box_{scale}.png" for scale in ("100", "125", "150", "175")]
    if find_and_click(search_images, fallback_coords=get_fallback_coords("search box"), name="search box"):
        pyautogui.hotkey("ctrl", "a")
        pyautogui.press("backspace")
        pyautogui.write("iPhone 15", interval=0.1)
        pyautogui.press("enter")
        print("✅ Search submitted.")

if __name__ == "__main__":
    run_amazon_login()
