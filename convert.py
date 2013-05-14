import json

streets = set()
data = []

def is_zipcode(s):
    try:
        int(s)
        return len(s) == 5
    except ValueError:
        return False

with open("softstory.txt", "r") as inf:
    curr_zipcode = ""

    for in_line in inf:
        line = in_line.strip()
        if len(line) == 0: continue
        if is_zipcode(line):
            curr_zipcode = line
            continue

        street_name, _, numbers_s = line.partition('-')
        street_name = '{} ({})'.format(street_name.strip(), curr_zipcode)
        numbers = numbers_s.strip().split(', ')

        if street_name in streets:
            print("Already processed {}!".format(street_name))
        streets.add(street_name)
        street_data = []

        for n in numbers:
            if '-' in n:
                # Range
                start_s, _, stop_s = n.partition('-')
                start = int(start_s)
                if stop_s.endswith(" 1/2"):
                    stop = int(stop_s[:-4])
                    street_data.append(stop_s)
                else:
                    stop = int(stop_s)

                if stop < start:
                    print("{} has inverted numbering".format(street_name))

                for i in range(start, stop+1):
                    street_data.append(str(i))
            else:
                street_data.append(n)

        data.append({'name': street_name, 'nums': street_data})

with open("softstory.json", "w") as outf:
    json.dump(data, outf)
