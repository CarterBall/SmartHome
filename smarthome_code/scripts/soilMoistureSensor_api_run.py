from smarthome_code.scripts.soilMoistureSensor import soilMoistureSensor


def main():

    entityID = "sensor.third_reality_inc_3rsm0147z_humidity"
    hassUrl = "http://127.0.0.1:8123"
    accessToken = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJlOTQyOWUwNjExZDE0MTRhOTQzN2I0ZTM4ODJhYWE0ZCIsImlhdCI6MTc1OTkwMjQzNSwiZXhwIjoyMDc1MjYyNDM1fQ.UcwYd74WsvgW9gB8xJZexYXX6MrojJ96pGtcJuZgeEk"

    run = True
    s = soilMoistureSensor(entityID, hassUrl, accessToken)

    while (run):
        inputVal = input("S for SoilMoistureSensor or exit: ")

        if (inputVal == "exit"):
            run = False
        elif (inputVal == "S"):
            s.moisture()


# call function main
if __name__ == "__main__":
    main()
