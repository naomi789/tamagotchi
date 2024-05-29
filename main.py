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
key_0.switch_to_input(pull=digitalio.Pull.DOWN)

key_1 = digitalio.DigitalInOut(board.GP17)
key_1.switch_to_input(pull=digitalio.Pull.DOWN)

key_2 = digitalio.DigitalInOut(board.GP2)
key_2.switch_to_input(pull=digitalio.Pull.DOWN)

key_3 = digitalio.DigitalInOut(board.GP3)
key_3.switch_to_input(pull=digitalio.Pull.DOWN)

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
    rowstart=1, # idk why 80??? why not (0,0)???
    backlight_pin=backlight,
)


while True:
    if key_0.value:
        print("Key 0 pressed")
        # convert png to index bmp: https://learn.adafruit.com/creating-your-first-tilemap-game-with-circuitpython/indexed-bmp-graphics
        bitmap = displayio.OnDiskBitmap("/images/hello-world.bmp")
        # forked from: https://learn.adafruit.com/circuitpython-display-support-using-displayio/display-a-bitmap
        tile_grid = displayio.TileGrid(bitmap, pixel_shader=bitmap.pixel_shader)
        group = displayio.Group()
        group.append(tile_grid)
        display.root_group = group
    if key_1.value:
        print("Key 1 pressed")
        # Do something for key 1 press
    if key_2.value:
        print("Key 2 pressed")
        # Do something for key 2 press
    if key_3.value:
        print("Key 3 pressed")
        # Do something for key 3 press
    # Add a small delay to avoid CPU intensive polling
    time.sleep(2)

