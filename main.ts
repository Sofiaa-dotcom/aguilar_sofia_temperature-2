let tempf = 70
while (true) {
    console.log("temperature" + input.temperature(TemperatureUnit.Fahrenheit))
    if (input.temperature(TemperatureUnit.Fahrenheit) > tempf) {
        light.setPixelColor(5, light.rgb(255, 0, 0))
    } else {
        light.clear()
    }
    
}
