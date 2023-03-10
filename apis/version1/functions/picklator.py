import pickle


def pickle_sensors_to_list(sensors):
    """If inverter found return data"""

    with open("./static/data/sensors_list", "wb") as sensors_file:
        pickle.dump(sensors, sensors_file)
        # print(f"Writing sensors {sensors} to file {sensors_file.name}")


def pickle_ip(ip):
    """Pickle ip adress"""

    with open("static/data/ip", "wb") as ip_file:
        pickle.dump(ip, ip_file)
        # print(f"Writing ip {ip} to file {ip_file.name} ")

        return 1


def unpickl_ip():
    """Load ip form pickled data"""

    with open("static/data/ip", "rb") as currrent_ip:

        try:
            while True:

                ip_data = pickle.load(currrent_ip)
                if ip_data:
                    return ip_data

                """If no ip search for inverter"""
                search_inverter()

        except EOFError:
            pass


def unpickl_sensor_list():
    """Unpickle saved sensors from settings"""

    with open("static/data/sensors_list", "rb") as saved_sensors:

        try:
            while True:

                sensors_list = pickle.load(saved_sensors)
                if sensors_list:

                    return sensors_list

                return 0

        except EOFError:
            pass


#
#
# def unpickl_data():
#     """Load dictionary form pickled data"""
#
#     last_item = "data/last_entry"
#
#
#     with open(last_item, 'rb') as last:
#         try:
#             while True:
#                 data = pickle.load(last)
#         except EOFError:
#             pass
#
#
#     return last
#
#
# def process_data(sensors_dict):
#
#
#         today = sensors_dict["Timestamp"]
#         filename = "data_"+today[0:10]
#         last_entry = "data_now"
#
#
#         with open('data/'+filename, 'ab+') as file0:
#             pickle.dump(sensors_dict, file0)
#
#         with open('data/last_entry', 'w') as file1:
#
#             for key in sensors_dict:
#                 file1.write(f"{key} : {sensors_dict[key]} \n")
#                 #print(f"{key} : {sensors_dict[key]} \n")
#
#             file1.close()
#
#
#         print(f"{today}  {filename}")
