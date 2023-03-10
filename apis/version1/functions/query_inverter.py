import goodwe

from apis.version1.functions.picklator import unpickl_ip
from apis.version1.functions.picklator import unpickl_sensor_list
from static.data.sensor_list import sensor_list


async def get_data():
    """Query inverter"""

    ip_address = unpickl_ip()
    sensor_list = unpickl_sensor_list()
    # print(sensor_list)

    # ip_address = '10.0.0.228'
    inverter = await goodwe.connect(ip_address)
    runtime_data = await inverter.read_runtime_data()

    sensors_dict = {}

    for sensor in inverter.sensors():
        if sensor.id_ in runtime_data and sensor.name in sensor_list:
            sensors_dict[sensor.name] = (
                str(runtime_data[sensor.id_]) + " " + sensor.unit
            )

    # print(sensors_dict)
    return sensors_dict
