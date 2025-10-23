from pathlib import Path
import xml.etree.ElementTree as ET

here = Path(__file__).resolve().parent
net_path = here / "osm.net.xml"   # << adjust if your net file is named differently
TL_ID = "149161311"

tree = ET.parse(net_path)
root = tree.getroot()

indices = []
# strict match: tl="149161311"
for conn in root.iter("connection"):
    if conn.get("tl") == TL_ID and conn.get("linkIndex") is not None:
        indices.append(int(conn.get("linkIndex")))

if not indices:
    # Sometimes the net stores connections under a cluster tl id that wraps your id.
    # Fallback: find any tl whose value CONTAINS the id as a substring.
    for conn in root.iter("connection"):
        tlval = conn.get("tl")
        if tlval and TL_ID in tlval and conn.get("linkIndex") is not None:
            indices.append(int(conn.get("linkIndex")))

if indices:
    print(f"TLS {TL_ID} connections found: {len(indices)}")
    print(f"max linkIndex = {max(indices)}  -> required phase state length = {max(indices)+1}")
else:
    print(f"No <connection tl=\"{TL_ID}\"> entries found in {net_path}")
