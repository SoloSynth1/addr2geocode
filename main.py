import csv

from geocode import Addr2Geocode

location_file = "./data/locations.csv"


def get_addresses(location_file=location_file, skip_rows=1, address_col=1, district_col=3):
    addresses = []
    with open(location_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i >= skip_rows:
                address = row[address_col]
                district = row[district_col]
                full_address = "{}, {}, {}".format("香港", district, address)
                addresses.append(full_address)
    return addresses

def list_599c():
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


def list_confirmed():
    addresses = get_addresses("./data/confirmed_cases.csv", address_col=1, district_col=0)
    print(addresses)
    geocodes = []
    geocode_service = Addr2Geocode()
    for i, address in enumerate(addresses):
        print(i, address)
        lat, long = geocode_service.translate(address)
        geocodes.append((lat, long))
    print(geocodes)
    for geocode in geocodes:
        print(geocode)


if __name__ == "__main__":
    # list_599c()
    list_confirmed()
