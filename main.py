import board
import displayio
# from adafruit_st7789 import ST7789
from adafruit_st7735r import ST7735R
import busio
import digitalio
import time


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
    colstart=1,
    rowstart=2,
    backlight_pin=backlight,
)

pals = ["/images/friend1.bmp", "/images/friend2.bmp", "/images/friend3.bmp", "/images/friend4.bmp"]
pal_index = 1
current_screen = "/images/test-welcome.bmp"

while True:
    print("current_screen is set to", current_screen)
    if not key_0.value:
        print("Key 0 pressed")
        pal_index = pal_index - 1
        current_screen = pals[pal_index]

    if not key_1.value:
        print("Key 1 pressed")
        # confirmation screen if correct friend, then show "confirmation" screen
        if current_screen == "/images/TODO": # TODO: name of correct friend
            current_screen = "/images/hug_confirmation.bmp"
        else if current_screen == "/images/hug_confirmation.bmp":
            # show annimation
            current_screen = "animate this"
        else:
            current_screen = "images/hug_cannot.bmp"

    if not key_2.value:
        print("Key 2 pressed")
        # see info screen if on correct friend
        # else show "prototype doesn't have info on this friend"
        # if correct friend, then show "info" screen
        if current_screen == "/images/TODO": # TODO: name of correct friend
            current_screen = "/images/info.bmp"
        else if current_screen == "/images/hug_confirmation.bmp":
            # show annimation
            current_screen = "animate this"
        else:
            current_screen = "/images/hug_cannot.bmp"

    if not key_3.value:
        print("Key 3 pressed")
        pal_index = pal_index + 1
        current_screen = pals[pal_index]


    if current_screen == "animate this":
        # then do animation
        print("idk how to animate")
    else: 
        bitmap = displayio.OnDiskBitmap(current_screen)
        tile_grid = displayio.TileGrid(bitmap, pixel_shader=bitmap.pixel_shader)
        group = displayio.Group()
        group.append(tile_grid)
        display.root_group = group
        time.sleep(3)
        
        
