
#Problem 1
"""Making available test data for 32 sensor clusters"""
#create a dict to hold sensor readings for the 32 sensor clusters
#dict will be filled up with random numbers
import random
import datetime
import csv

major_sensor_cluster_data = dict()
sensor_cluster_data = dict()

#run a loop to create dummy data values

for i in range(1,33):
    sensor_cluster_data.clear()
    for j in range(1,17):

        sensor_cluster_data[j] = random.random()

        #creating a nested dict to store data

    major_sensor_cluster_data['cluster',i] = sensor_cluster_data

# pulling out the key list to sort
clusterkeys = major_sensor_cluster_data.keys()
clusterkeys.sort()
for key in clusterkeys:

    #printing the ordered sensor data for 32 clusters with 16 sensor readings per cluster
    print (key, major_sensor_cluster_data[key])
    continue


#Problem 2

#writing the data created in the nested dict in to a csv file for permanence

with open('sensor_data_store.csv', 'w') as sensor_output:
    writer = csv.writer(sensor_output,delimiter ='\t')
    # loop through the dicts to write it in a csv file
    for key in clusterkeys:

        #enrich dataset by adding time of writing in to file

        now =datetime.datetime.now()

        sensor_readings = major_sensor_cluster_data

        for readings in sensor_readings:
            print readings
            writer.writerow([now, key, readings])







