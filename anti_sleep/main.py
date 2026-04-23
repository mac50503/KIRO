import ctypes
import pyautogui
import time

# Windows API constants
ES_CONTINUOUS       = 0x80000000
ES_SYSTEM_REQUIRED  = 0x00000001
ES_DISPLAY_REQUIRED = 0x00000002

def prevent_sleep():
    """Tell Windows the system is in use (resets idle timer)."""
    ctypes.windll.kernel32.SetThreadExecutionState(
        ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED
    )

print("Anti-sleep activo. Ctrl+C para detener.")

try:
    while True:
        prevent_sleep()                  # reset Windows idle timer
        pyautogui.moveRel(1, 0)          # mueve 1 pixel a la derecha
        time.sleep(0.1)
        pyautogui.moveRel(-1, 0)         # regresa al lugar original
        pyautogui.press('shift')         # tecla inofensiva para reforzar actividad
        print(f"Actividad simulada - {time.strftime('%H:%M:%S')}")
        time.sleep(60)
finally:
    # Restore normal sleep behavior on exit
    ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS)
    print("Anti-sleep desactivado.")
