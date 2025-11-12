from smarthome_code.scripts.powerMonitor import PowerMonitor


def main():

    entityID = "sensor.third_reality_inc_3rsp02028bz_power"
    hassUrl = "http://127.0.0.1:8123"
    accessToken = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJlOTQyOWUwNjExZDE0MTRhOTQzN2I0ZTM4ODJhYWE0ZCIsImlhdCI6MTc1OTkwMjQzNSwiZXhwIjoyMDc1MjYyNDM1fQ.UcwYd74WsvgW9gB8xJZexYXX6MrojJ96pGtcJuZgeEk"

    run = True
    power = PowerMonitor(entityID, hassUrl, accessToken)

    while (run):
        inputVal = input("W for Watts or exit: ")

        if (inputVal == "exit"):
            run = False
        elif (inputVal == "W"):
            power.watts()


# call function main
if __name__ == "__main__":
    main()
