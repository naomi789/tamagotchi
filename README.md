# tamagotchi
Similar to but different from Tamagotchi - a grad school project

# set up
## hardware
 - One Waveshare 1.44inch LCD Display Module for Raspberry Pi Pico 65K RGB Colors 128×128 Pixels (we got ours for [$15.99 on Amazon with one-day shipping](https://www.amazon.com/dp/B0957NJP97/))
 - One Pre-Soldered Header Raspberry Pi Pico W, Built-in WiFi Support 2.4 GHZ Wi-Fi 4, (we got ours for [$14.60 on Amazon with one-day shipping](https://www.amazon.com/dp/B0BK9W4H2Q/)
 - One USB-C to MicroUSB cable

## software
 - CircuitPython (9.x)

## documentation  
 - [Waveshare's documentation about the Waveshare Pico LCD 1.44](https://www.waveshare.com/wiki/Pico-LCD-1.44)
 - [Waveshare's documentation about the Raspberry Pi Pico](https://www.waveshare.com/wiki/Raspberry_Pi_Pico_W)
 - [Installing MicroPython for Raspberry Pi Pico](https://micropython.org/download/RPI_PICO/)
 - [Raspberry Pi Pico datasheet](https://datasheets.raspberrypi.com/pico/pico-datasheet.pdf) was used to confirm that pin #25 controls the LED
 - [CircuitPython for the Raspberry Pi Pico](https://circuitpython.org/board/raspberry_pi_pico_w/)
 - [Official CircuitPython libraries](https://circuitpython.org/libraries)

# to update
 - Our device is optimized for BMP images that are 128x128 pixels and are index to be black and white
 - For some versions of our prototype, we had to convert from JPG to BMP and we used [this guide](https://learn.adafruit.com/creating-your-first-tilemap-game-with-circuitpython/indexed-bmp-graphics)

# special thanks to free online tutorials
## we leaned heavily on: 
 - [How to display a BMP image using CircuitPython](https://learn.adafruit.com/circuitpython-display-support-using-displayio/display-a-bitmap)
 - [How to create an indexed BMP graphic](https://learn.adafruit.com/creating-your-first-tilemap-game-with-circuitpython/indexed-bmp-graphics)
 - [How to resize an image in GIMP](https://thegimptutorials.com/how-to-resize-image/)

## we also dabbled with: 
 - How-to set up guides ([connecting your Pi to your computer](https://apple.stackexchange.com/questions/60231/using-terminal-how-can-i-find-which-directory-is-my-usb-drive-mounted-in), [using Thonny to connect your Pi to your computer](https://microcontrollerslab.com/getting-started-raspberry-pi-pico-thonny-ide/), [connecting & reconnecting drives](https://osxdaily.com/2013/05/13/mount-unmount-drives-from-the-command-line-in-mac-os-x/), [Peter's blinking microprocessor tutorial](https://www.peterzimon.com/raspberry-pi-pico-mac-c-blink/), [How Choo's blinking microprocessor tutorial](https://howchoo.com/pi/control-leds-with-the-raspberry-pi-pico/))
 - [the Microprocessor & Arduino simulator, Wokwi](https://wokwi.com/projects/359558101922696193)
 - How-to tutorials [animating graphics on OLED screens](https://www.tomshardware.com/how-to/oled-display-raspberry-pi-pico), [building a digital photo frame](https://www.tomshardware.com/how-to/raspberry-pi-photo-frame), @ExcaliburZero's advice about the Pico](https://www.reddit.com/r/raspberrypipico/comments/pl97z6/display_an_image_on_waveshare_18_lcd_using_pico/), [how to use the buttons on a WaveShare screen](https://www.reddit.com/r/pwnagotchi/comments/g3jbei/hi_all_has_anyone_been_successful_at_making_these/), [MicroPython for graphics](https://thepihut.com/blogs/raspberry-pi-tutorials/coding-graphics-with-micropython-on-raspberry-pi-pico-displays))
 - [How to install CircuitPython](https://learn.adafruit.com/pico-w-wifi-with-circuitpython/installing-circuitpython)
 - [Common libraries for CircuitPython](https://learn.adafruit.com/welcome-to-circuitpython/circuitpython-libraries), [Blinka and other CircuitPython libraries](https://learn.adafruit.com/circuitpython-libraries-on-micropython-using-the-raspberry-pi-pico/installing-blinka-and-libraries), [Displayio and other libraries](https://learn.adafruit.com/circuitpython-display-support-using-displayio/examples)
 - [Blink & sleep tutorial for CircuitPython](https://github.com/CytronTechnologies/Getting-Started-with-Pico-W-CircuitPython/blob/main/01_blink.py)
 - [Free online image to byte converter](https://mischianti.org/images-to-byte-array-online-converter-cpp-arduino/)
 - [Removing newlines from strings](https://24toolbox.com/newline-remover/)
 - [Demo for the sibling screen, Waveshare 1.14](https://github.com/dfinein/Pico-LCd-114/)
 - [Demo for ST7789](https://docs.circuitpython.org/projects/st7789/en/latest/examples.html#x135)





