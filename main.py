#Amanda Kogut, @koguta

import machine
import utime

red_led = machine.Pin(0, machine.Pin.OUT)
yellow_led = machine.Pin(2, machine.Pin.OUT)
green_led = machine.Pin(5, machine.Pin.OUT)

while True:

  red_led.value(1)
  utime.sleep(2)

  yellow_led.value(1)
  utime.sleep(1)

  red_led.value(0)
  yellow_led.value(0)

  green_led.value(1)
  utime.sleep(2)

  green_led.value(0)

  yellow_led.value(1)
  utime.sleep(1)

  yellow_led.value(0)

