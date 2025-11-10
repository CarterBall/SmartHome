from smarthome_code.scripts.thermometer import thermometer


def main():

    entityID = "sensor.unk_manufacturer_unk_model_temperature"
    hassUrl = "http://127.0.0.1:8123"
    accessToken = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJlOTQyOWUwNjExZDE0MTRhOTQzN2I0ZTM4ODJhYWE0ZCIsImlhdCI6MTc1OTkwMjQzNSwiZXhwIjoyMDc1MjYyNDM1fQ.UcwYd74WsvgW9gB8xJZexYXX6MrojJ96pGtcJuZgeEk"

    run = True
    temp = thermometer(entityID, hassUrl, accessToken)

    while (run):
        inputVal = input("C for Celsius or F for Fahrenheit or exit: ")

        if (inputVal == "exit"):
            run = False
        elif (inputVal == "C"):
            temp.celsius()
        elif (inputVal == "F"):
            temp.fahrenheit()


# call function main
if __name__ == "__main__":
    main()
