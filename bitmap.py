import board
import displayio
from adafruit_st7789 import ST7789
import busio

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

# forked from: https://docs.circuitpython.org/projects/st7789/en/latest/examples.html#x135
display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=reset)
display = ST7789(
    display_bus,
    rotation=180,
    width=128,
    height=128,
    rowstart=0, # idk why 80??? why not (0,0)???
    backlight_pin=backlight,
)

# forked from: https://learn.adafruit.com/circuitpython-display-support-using-displayio/display-a-bitmap
bitmap = displayio.OnDiskBitmap("/purple.bmp")
tile_grid = displayio.TileGrid(bitmap, pixel_shader=bitmap.pixel_shader)
group = displayio.Group()
group.append(tile_grid)
display.root_group = group

while True:
    pass
