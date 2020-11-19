let tempf = 80
while (true) {
    console.log("temperature" + input.temperature(TemperatureUnit.Fahrenheit))
    if (tempf > 60) {
        light.setAll(light.rgb(255, 0, 0))
    } else if (70 < tempf && tempf > 40) {
        light.setAll(light.rgb(0, 255, 0))
    } else {
        light.setAll(light.rgb(0, 0, 255))
    }
    
}
