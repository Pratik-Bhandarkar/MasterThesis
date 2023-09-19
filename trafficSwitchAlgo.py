from collections import Counter
import streamlit as st


def trafficSwitch(prediction):
    classList = []
    for i in prediction['predictions']:
        classList.append(i['class'])

        # Create a Counter object
    counter = dict(Counter(classList))
    # print(type(dict(counter)))
    print(counter)
    for objType, totalCount in counter.items():
        # print("{} {} detected in the image".format(totalCount, objType))
        st.write("{} {} detected in the image".format(totalCount, objType))

    # print("counter length: " + str(len(counter)))
    if len(counter) != 0:

        for item, count in counter.items():
            print(item+''+str(count))
            if (item == 'ambulance' or item == 'firetruck') and count >= 1:
                light_color = 'red'
                # print("reeeeeeeeeeeed")
                break
            elif (item == 'Elderly Person' or item == 'Wheelchair' or item == 'peopleWithWheelchair' or item == 'not wheel chair') and count >= 1:
                light_color = 'green'
                print("herererereeeeeeee")
                print(light_color)
                break
            elif (item == 'person' or item == 'people ') and count >= 2:
                print("herere????")
                light_color = 'green'
                break
            else:
                light_color = 'red'
                print("haha red")
    else:
        light_color = 'green'

    return light_color
