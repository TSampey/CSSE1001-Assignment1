###################################################################
#
#   CSSE1001/7030 - Assignment 1
#
#   Student Number:
#
#   Student Name: Thomas Sampey
#
###################################################################

#####################################
# Support given below - DO NOT CHANGE
#####################################

from assign1_support import *

#####################################
# End of support 
#####################################

# Add your code here
"""

Parses U.Q data and formats it into a list with tuples data.
[String] -> [List]
Outputs: string, string, string, string, (tuple())
"""
def load_data(dateStr):
        dateData = get_data_for_date(dateStr).splitlines()
        newData = []
        for c in dateData:
                data = c.split(',')
                time = data[0]
                temp = float(data[1])
                sun = float(data[2])
                powers = data[3:]
                i = 0
                while i < len(powers):
                        powers[i] = int(powers[i])
                        i += 1
                 
                newData.append((time, temp, sun, tuple(powers)))
        return newData
                 
"""
Iterates through data.
Outputs the maximum temperature
[string] -> [tupple]
e.g[max temperature tuple(times)]
"""
def max_temperature(data):
       maxTemp = 0
       totalDate = []
       for c in data:
               if c[1] > maxTemp:
                       maxTemp = c[1]
       for i in data:
               if maxTemp == i[1]:
                       totalDate.append(i[0])
       return (maxTemp, totalDate)

"""
Iterates through the data stored with in the variable 'data' and outputs the total amount of energy U.Q uses
[string] -> [Float]
"""

def total_energy(data):
        total = 0
        for c in data:
                for i in c[3]:
                        total=total+i
        return float(total)/60000

"""
Iterates through the data within variable 'data' and outputs the maximum power within each of the locations
e.g UQ Centre, St Lucia, (power)
[String] -> [tuple]
"""
def max_power(data):
        maxPower = [0] * len(ARRAYS)
        for c in data:
                i = 0
                while i < len(c[3]):
                        if c[3][i] > maxPower[i]:
                                maxPower[i] = c[3][i]
                        i += 1
        result = []
        i = 0
        while i < len(ARRAYS):
                result.append((ARRAYS[i],maxPower[i] / 1000.0))
                i +=1
        return result
"""
User enters display_stats(date) command and it returns the statistics of all of U.Q for the date entered
it takes in a list from load data and outputs the date, max temp, total energy, and maximum power.
[List] -> [string]
"""
def display_stats(date):  
        data = load_data(date)
        MAX_TEMP = max_temperature(data)
        TOTAL_ENERGY = total_energy(data)
        print
        print "Statistics for " + date + "\n"
        print "Maximum Temperature: " + str(MAX_TEMP[0]) +"C" + " at times " + ", ".join(MAX_TEMP[1]) 
        print
        print "Total Energy Production: {0:.1f}kWh".format(TOTAL_ENERGY)
        print
        print "Maximum Power Outputs: \n"
        for array, power in max_power(data):
                print STATS_ROW.format(array, power)

"""
Displays a user interface that allows the user to enter a command and displays the statistics of the UQ or unknown command.
[date] -> [list]
"""
def interact():
        print "Welcome to PV calculator \n\n "
        while True:
                inputs = raw_input("command: ")
                if inputs == 'q':
                        return
                ins = inputs.split()
                if (len(ins) == 2 and ins[0] == "date") or (len(ins) == 2 and ins[0] == "Date") or (len(ins) == 2 and ins[0] == "DATE"):
                        display_stats(ins[1])
                        print
                else:
                        print"Unknown command: " + inputs
                        print
                        
##################################################
# !!!!!! Do not change (or add to) the code below !!!!!
# 
# This code will run the interact function if
# you use Run -> Run Module  (F5)
# Because of this we have supplied a "stub" definition
# for interact above so that you won't get an undefined
# error when you are writing and testing your other functions.
# When you are ready please change the definition of interact above.
###################################################

if __name__ == '__main__':
    interact()
