import csv

from geocode import Addr2Geocode

location_file = "./data/locations.csv"


def get_addresses(location_file=location_file, skip_rows=1):
    addresses = []
    with open(location_file, 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i >= skip_rows:
                address = row[1]
                district = row[3]
                full_address = "{}, {}, {}".format("香港", district, address)
                addresses.append(full_address)
    return addresses


if __name__ == "__main__":
    addresses = get_addresses()
    geocodes = []
    geocode_service = Addr2Geocode()
    for i, address in enumerate(addresses):
        print(i, address)
        lat, long = geocode_service.translate(address)
        geocodes.append((lat, long))
    print(geocodes)
    for geocode in geocodes:
        print(geocode)
