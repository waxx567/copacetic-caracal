'''
You are developing an application to manage sensor data for IoT systems. Specifically, the sensor readings are stored in a binary search tree (BST) structure where each node contains a single unique timestamp as the node's key along with a sensor reading. You need to design functionality to retrieve all sensor readings in order that were recorded within a specific time range, while doing so, you have noticed that something is not working as expected.
'''
class SensorDataNode:
    def __init__(self, timestamp, reading):
        self.timestamp = timestamp
        self.reading = reading
        self.left = None
        self.right = None

def get_readings_in_range(node, start_time, end_time):
    readings = []
    if node is None:
        return readings
    
    if start_time <= node.timestamp <= end_time:
        readings.append((node.timestamp, node.reading))

    if start_time < node.timestamp:
        readings.append(get_readings_in_range(node.left, start_time, end_time))
    
    if end_time > node.timestamp:
        readings.append(get_readings_in_range(node.right, start_time, end_time))
