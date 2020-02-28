from geocode import Addr2Geocode

location_file = "./data/locations.csv"


def get_addresses(location_file=location_file, skip_rows=1):
    addresses = []
    with open(location_file, 'r') as f:
        for i, line in enumerate(f.readlines()):
            if i >= skip_rows:
                address = line.split(",")[1]
                addresses.append(address)
    return addresses


if __name__ == "__main__":
    addresses = get_addresses()
    geocodes = []
    geocode_service = Addr2Geocode()
    for address in addresses:
        lat, long = geocode_service.translate(address)
        geocodes.append((lat, long))
    print(geocodes)
    with open("output.csv", 'w') as f:
        f.write("\n".join(geocodes))
