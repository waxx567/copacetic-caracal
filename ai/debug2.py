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
        readings.append(node.reading)

    if start_time < node.timestamp:
        readings += get_readings_in_range(node.left, start_time, end_time)

    if end_time > node.timestamp:
        readings += get_readings_in_range(node.right, start_time, end_time)

    return readings

#          10
#         /  \
#        5    15
#            /  \
#          12    20

root = SensorDataNode(10, 'Reading-10')
root.left = SensorDataNode(5, 'Reading-5')
root.right = SensorDataNode(15, 'Reading-15')
root.right.left = SensorDataNode(12, 'Reading-12')
root.right.right = SensorDataNode(20, 'Reading-20')

# Define time range [10, 15] inclusive.
start_time = 10
end_time = 15

readings_in_range = get_readings_in_range(root, start_time, end_time)
print("Readings within range:", readings_in_range)