from Lights import Lights


def main():

    entityID = "light.third_reality_inc_3rcb01057z_light"
    hassUrl = "http://127.0.0.1:8123"
    accessToken = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJlOTQyOWUwNjExZDE0MTRhOTQzN2I0ZTM4ODJhYWE0ZCIsImlhdCI6MTc1OTkwMjQzNSwiZXhwIjoyMDc1MjYyNDM1fQ.UcwYd74WsvgW9gB8xJZexYXX6MrojJ96pGtcJuZgeEk"

    run = True
    light = Lights(entityID, hassUrl, accessToken)

    while (run):
        inputVal = input("Enter on or off: ")

        if (inputVal == "exit"):
            run = False
        elif (inputVal == "on"):
            light.On()
        elif (inputVal == "off"):
            light.Off()
        elif (inputVal == "down"):
            light.BrightnessDown()
        elif (inputVal == "up"):
            light.BrightnessUp()


# call function main
if __name__ == "__main__":
    main()
