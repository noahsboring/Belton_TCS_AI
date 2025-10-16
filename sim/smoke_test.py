import traci

# Test if SUMO is connected

SUMO_CFG = "sim/osm.sumocfg"

def main():
    traci.start(["sumo", "-c", SUMO_CFG, "--start"])
    print(" Connected to SUMO")

    tls_ids = traci.trafficlight.getIDList()
    print("Traffic lights found:", tls_ids)

    for step in range(20):
        traci.simulationStep()
    traci.close()
    print(" Simulation finished successfully")

if __name__ == "__main__":
    main()
