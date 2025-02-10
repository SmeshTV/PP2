import json


with open(r"C:\Users\Arman\Desktop\PP2\Lab 4\json\sample-data.json") as f:
   data = json.load(f)


imdata = data.get('imdata', [])
print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<10} {'MTU':<5}")
print("-" * 80)

for item in imdata:
    attributes = item.get('l1PhysIf', {}).get('attributes', {})
    dn = attributes.get('dn', 'N/A')
    descr = attributes.get('descr', 'inherit')
    speed = attributes.get('speed', 'N/A')
    mtu = attributes.get('mtu', 'N/A')
    print(f"{dn:<50} {descr:<20} {speed:<10} {mtu:<5}")