from collections import Counter


def trafficSwitch(prediction):
    classList = []
    for i in prediction['predictions']:
        classList.append(i['class'])

        # Create a Counter object
    counter = dict(Counter(classList))
    print(type(dict(counter)))
    print(counter)
    for objType, totalCount in counter.items():
        print("{} {} detected in the image".format(totalCount, objType))

    print("counter length: " + str(len(counter)))
    if len(counter) != 0:
        for item, count in counter.items():
            if (item == 'ambulance' or item == 'firetruck') and count >= 1:
                light_color = 'green'
            elif (item == 'Elderly Person' or item == 'Wheelchair') and count >= 1:
                light_color = 'green'
            elif item == 'person' and count >= 2:
                light_color = 'green'
            else:
                light_color = 'green'
    else:
        light_color = 'green'

    return light_color