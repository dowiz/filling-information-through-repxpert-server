from getting_a_list_for_searching import getting_list
from getting_data_from_repxpert_server import get_data
import time

data = getting_list()

for i in data:
    data = get_data(i[1], i[2])

    with open('log.txt', 'a') as file:

        try:
            file.write(i[0] + " " + data["name"] + " " +
                       data["brand"] + " Success" + "\n")
            print(data["name"], data["brand"], "Success")
        except KeyError:
            try:
                file.write(i[0] + " " + i[1] + " " +
                           i[2] + " " + data["error"] + "\n")
                print(i[1], i[2], data["error"])
            except KeyError:
                file.write(i[0] + " " + i[1] + " " + i[2] + " " +
                           "KeyError" + "\n")
                print(i[1], i[2], "KeyError")

    time.sleep(300)
