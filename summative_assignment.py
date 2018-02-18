"""Making available test data for 32 sensor clusters"""
#create a dict to hold sensor readings for the 32 sensor clusters
#dict will be filled up with random numbers
import random
major_sensor_cluster_data = dict()
sensor_cluster_data = dict()

#run a loop to create dummy data values

for i in range(1,33):
    for j in range(1,17):
        sensor_cluster_data[j] = random.random()
        #creating a nested dict to store data
    major_sensor_cluster_data['cluster',i] = sensor_cluster_data
# pulling out the key list to sort
clusterkeys = major_sensor_cluster_data.keys()
clusterkeys.sort()
for key in clusterkeys:
    print (key, major_sensor_cluster_data[key])






