tempf= 80
while True:
    print("temperature" + input.temperature(TemperatureUnit.FAHRENHEIT))
    if tempf > 60:
        light.set_all(light.rgb(255, 0, 0))
    elif 70 < tempf > 40:
        light.set_all(light.rgb(0, 255, 0))
    else:
        light.set_all(light.rgb(0, 0, 255))