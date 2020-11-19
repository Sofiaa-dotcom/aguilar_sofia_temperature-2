tempf= 75
while True:
    print("temperature" + input.temperature(TemperatureUnit.FAHRENHEIT))
    if input.temperature(TemperatureUnit.FAHRENHEIT) > tempf:
        light.set_pixel_color(5, light.rgb(255,0,0))
    elif tempf < 70:
     if input.temperature(TemperatureUnit.FAHRENHEIT) < tempf:
         light.set_pixel_color(6, light.rgb(0,128,0))
else:
    light.clear()