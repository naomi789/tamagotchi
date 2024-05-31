import asyncio
import keypad
import board
import displayio
from adafruit_st7735r import ST7735R
import busio
import digitalio
import time
import adafruit_imageload

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

async def catch_pin_transitions():
    """Print a message when pin goes low and when it goes high."""
    with keypad.Keys((key_0, key_1, key_2, key_3),
                        value_when_pressed=False) as keys:
        while True:
            event = keys.events.get()
            if event and  event.pressed:
                print("Key {} was pressed".format(event.key_number))
                game_state.key_press(event.key_number)
            await asyncio.sleep(0)

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

class GameState:
    friends_gardens = {
        "friend1": "friend1",
        "friend2": "friend2",
        "friend3": "friend3",
        "friend4": "friend4",
    }
    
    map = {
        "welcome": [None, "friend1", None, None],
        "friend1": [friends_gardens["friend4"], "friend1_hugconfirm", "friend1_info", friends_gardens["friend2"]],
        "friend2": [friends_gardens["friend1"], "friend2_hugconfirm", "friend2_info", friends_gardens["friend3"]],
        "friend3": [friends_gardens["friend2"], "friend3_hugconfirm", "friend3_info", friends_gardens["friend4"]],
        "friend4": [friends_gardens["friend3"], "friend4_hugconfirm", "friend4_info", friends_gardens["friend1"]],
        "friend1_info": [None, None, "friend1", None], 
        "friend2_info": [None, None, "friend2", None],
        "friend3_info": [None, None, "friend3", None],
        "friend4_info": [None, None, "friend4", None],
        "friend1_hugconfirm": [None, "friend1_hugbase", None, None],
        "friend2_hugconfirm": [None, "friend2_hugbase", None, None],
        "friend3_hugconfirm": [None, "friend3_hugbase", None, None],
        "friend4_hugconfirm": [None, "friend4_hugbase", None, None]
        }
    flower_counts = {
        "friend1": 0,
        "friend2": 8,
        "friend3": 6,
        "friend4": 11,
        }
    find_gardens = {
        0: "friend1",
        .34: "friend1_flower1",
        .68: "friend1_flower2",
        1.02: "friend1_flower3", 
        8: "friend2",
        8.34: "friend2_flower1",
        8.68: "friend2_flower2",
        9.02: "friend2_flower3", 
        6: "friend3",
        6.34: "friend3_flower1",
        6.68: "friend3_flower2",
        7.02: "friend3_flower3", 
        11: "friend4",
        11.34: "friend4_flower1",
        11.68: "friend4_flower2",
        12.02: "friend4_flower3",
    }
    
    def __init__(self):
        self.state = "welcome"
        self.update_screen()

    def key_press(self, key_number):
        self.state = self.map[self.state][key_number]
        print("New state", self.state)
        self.update_screen()

    def update_screen(self):
        if not "hugbase" in self.state:
            display_image("/images/{}.bmp".format(self.state))
        else:
            display_hug("/images/{}.bmp".format(self.state))
            current_friend = self.state[:7]
            print("current_friend: {}".format(current_friend))
            # update count of flowers 
            old_count = self.flower_counts[current_friend]
            new_count = old_count + .34
            self.flower_counts[current_friend] = new_count
            print("new count: {}".format(self.flower_counts[current_friend]))

            # if I have a new photo, then update image
            print("self.find_gardens[new_count]: {}".format(self.find_gardens[new_count]))
            self.friends_gardens[current_friend] = self.find_gardens[new_count]
            
            print("self.flower_counts[current_friend]: {}".format(self.flower_counts[current_friend]))
            
            if (self.flower_counts[current_friend] < 1.03) and (self.flower_counts[current_friend] > 1.01):
                print("first flower!!")
                display_image("/images/{}_flowercongrats.bmp".format(current_friend))
                time.sleep(3)
                
            # and return to the correct friend's screen
            self.state = current_friend
            display_image("/images/{}.bmp".format(current_friend))
            
            
            
def load_partial_image(image_path, x, y):
    bitmap, palette = adafruit_imageload.load(
        image_path,
        bitmap=displayio.Bitmap,
        palette=displayio.Palette)
    tile_grid = displayio.TileGrid(bitmap, pixel_shader=palette, x=x, y=y)
    return tile_grid

def display_hug(image):
    # create the compound image
    image_top_text = image[:16] + "hugscroll"
    tile_grid_hearts = load_partial_image("/images/{}.bmp".format("hugheartscroll"), x=0, y=0)  # about 33 pixels tall
    tile_grid_text = load_partial_image("{}.bmp".format(image_top_text), x=70, y=0) # about 33 pixels tall
    tile_grid_bottom_critters = load_partial_image(image, x=0, y=33)  # about 93 pixels tall
    
    group = displayio.Group()
    group.append(tile_grid_hearts)
    group.append(tile_grid_text)
    group.append(tile_grid_bottom_critters)
    display.root_group = group
    
    # Scroll the images to the left
    for x in range(0, display.width):
        tile_grid_hearts.x = -x
        tile_grid_text.x = display.width - x

        if tile_grid_text.x <= 0:
            temp = tile_grid_hearts
            tile_grid_hearts = tile_grid_text
            tile_grid_text = temp
            tile_grid_text.x = display.width

        time.sleep(0.05)


        
        
def display_image(image):
    bitmap, palette = adafruit_imageload.load(
                        image,
                        bitmap=displayio.Bitmap,
                        palette=displayio.Palette)
    tile_grid = displayio.TileGrid(bitmap, pixel_shader=palette)
    group = displayio.Group()
    group.append(tile_grid)
    display.root_group = group

async def main():
    global game_state
    game_state = GameState()
    interrupt_task = asyncio.create_task(catch_pin_transitions())
    await asyncio.gather(interrupt_task)

asyncio.run(main())

