import board
import displayio
# from adafruit_st7789 import ST7789
from adafruit_st7735r import ST7735R
import busio
import digitalio
import time
# import zipfile


# forked https://github.com/dfinein/Pico-LCd-114/blob/main/main.py
displayio.release_displays() # what does this do???
chip_spi = board.GP10
mosi = board.GP11
spi = busio.SPI(chip_spi, mosi)
tft_cs = board.GP9 # chip selection
tft_dc = board.GP8 # data command
key_0 = board.GP15
key_1 = board.GP17
key_2 = board.GP2
key_3 = board.GP3
reset = board.GP12
backlight = board.GP13

# Define keys
key_0 = digitalio.DigitalInOut(board.GP15)
key_0.switch_to_input(pull=digitalio.Pull.UP)

key_1 = digitalio.DigitalInOut(board.GP17)
key_1.switch_to_input(pull=digitalio.Pull.UP)

key_2 = digitalio.DigitalInOut(board.GP2)
key_2.switch_to_input(pull=digitalio.Pull.UP)

key_3 = digitalio.DigitalInOut(board.GP3)
key_3.switch_to_input(pull=digitalio.Pull.UP)

# forked from: https://docs.circuitpython.org/projects/st7789/en/latest/examples.html#x135
# adjusted from ST7789 to ST7735R (which includes the S version we're using):
# https://github.com/adafruit/Adafruit_CircuitPython_ST7735R
display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=reset)
display = ST7735R(
    display_bus,
    rotation=180,
    width=128,
    height=128,
    colstart=2,
    rowstart=3,
    backlight_pin=backlight,
)

pals = ["/images/friend1.bmp", "/images/friend2.bmp", "/images/friend3.bmp", "/images/friend4.bmp"]
print(pals[1])
# TODO check if 1 indexed or zero indexed
pal_index = 0
count_pals_min = 0
count_pals_max = 3
current_screen = "/images/test-welcome.bmp"

while True:
    print("current_screen is set to", current_screen)
    if not key_0.value: # LEFT BUTTON
        print("Key 0 pressed")
        pal_index = pal_index - 1
        current_screen = pals[pal_index]

    elif not key_1.value: # HEART BUTTON
        print("Key 1 pressed")
        if current_screen == "/images/test-welcome.bmp":
            current_screen = pals[pal_index]
        # confirmation screen if correct friend, then show "confirmation" screen
        elif current_screen == "/images/TODO": # TODO: name of correct friend
            current_screen = "/images/hug_confirmation.bmp"
        elif current_screen == "/images/hug_confirmation.bmp":
            # show annimation
            current_screen = "animate this"
        else:
            current_screen = "images/hug_cannot.bmp"

    elif not key_2.value: # INFO BUTTON
        print("Key 2 pressed")
        if current_screen.startswith("/images/friend") and not current_screen.endswith("info.bmp"):
            prefix = current_screen[:15]
            print(prefix)
            current_screen = prefix + "_info.bmp"
            print(current_screen)
        elif current_screen.endswith("info.bmp"):
            prefix = current_screen[:15]
            print(prefix)
            current_screen = prefix + ".bmp"
            print(current_screen)
        else:
            print("assert error in key 2")

    elif not key_3.value: # RIGHT BUTTON
        print("Key 3 pressed")
        if pal_index < count_pals_max:
            pal_index = pal_index + 1
        elif pal_index == count_pals_max:
            pal_index = count_pals_min
        current_screen = pals[pal_index]


    if current_screen == "animate this":
        # then do animation
        print("idk how to animate")
    else:
        # zip_file_path = current_screen + ".zip"
        # destination_dir = "/temp"
        # if not os.path.exists(destination_dir):
            # os.makedirs(destination_dir)
        # with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            # # Extract all the contents into the destination directory
            # zip_ref.extractall(destination_dir)
        
        bitmap = displayio.OnDiskBitmap(current_screen)
        tile_grid = displayio.TileGrid(bitmap, pixel_shader=bitmap.pixel_shader)
        group = displayio.Group()
        group.append(tile_grid)
        display.root_group = group
        time.sleep(3)
        
        
