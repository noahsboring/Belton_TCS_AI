from pathlib import Path
from sumolib.net import readNet

net_path = Path(__file__).resolve().parent / "osm.net.xml"
tl_id = "149161311"

net = readNet(str(net_path))

indices = []
# Each traffic light node in the network
for node in net.getTrafficLights():
    if node.getID() == tl_id:
        for logic in node.getPrograms().values():
            for phase in logic.getPhases():
                # Each logic has controlled links accessible via node.getConnections()
                for links in node.getControlledLinks():
                    for link in links:
                        if link and link[2] == tl_id and link[3] is not None:
                            indices.append(link[3])

if indices:
    print(f"TLS {tl_id} controls {len(indices)} connections; max linkIndex = {max(indices)}")
    print(f"Required phase state length = {max(indices) + 1}")
else:
    print(f"No connections found for TLS {tl_id}. "
          f'Try verifying that tl="{tl_id}" exists in {net_path}')
