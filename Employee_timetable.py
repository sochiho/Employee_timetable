
'''Write a function which takes employees unavailable times to find the
times available to book a group meeting. Inputs are taken as Tuples and output can be times of unavailabilty or
of availabilty'''

'''Times are defined as
9.00 = 1, 9.30 = 2, 10.00 = 3, 10.30 = 4, 11.00 = 5, 11.30 = 6, 12.00 = 7, 12.30 = 8
13.00 = 9, 13.30 = 10, 14.00 = 11, 14.30 = 12, 15.00 = 13, 15.30 = 14 ... until 17.30 = 18 '''

import numpy


def meet_times(x):
    '''This functon finds availabilty of employees'''

    #Check to ensure input list is greater than one
    if len(x) <=1:
        print 'No. of employees must be greater than 1'
        return

    def time(x):
        '''Nested function for converting integer to string for time using remainder function, %'''
        if x%2 != 0:
            tt = str((x + 1) /2 + 8) + ":00"
        else:
            tt = str(x/2 +8) + ":30"
        return tt

    # order tuple list by 1st and 2nd element
    sort_times = sorted(x)

    # empty lists for storing     
    store = []
    time_store = []

    # initial and final for 1st element of sorted array
    initial = sort_times[0][0]
    final = sort_times[0][1]

    # for loop starting at element 1 as 0 is already initialise above
    for i in range(1, len(sort_times)):

        # compare initial and final to comp_i and comp_f
        comp_i = sort_times[i][0]
        comp_f = sort_times[i][1]

        # if between initial and final
        if comp_i >= initial and comp_i <= final:                
            if comp_f > final:
                final = comp_f

       # else store as the time window
        else:
            store.append([final, comp_i])
            time_store.append([time(final), time(comp_i)])
            initial = comp_i
            final = comp_f

        # if it's the final test
        if i == len(sort_times) -1 and sort_times[i][1] < 18:
            store.append([final, 18])
            time_store.append([time(final), time(18)])

    # if no times are avaliable
    if len(store) == 0:
        return "No times are available"
        
    else:
        print "----------------\nTimes avaliable: \n----------------"
        for times in time_store:
            print (" " + times[0] + " - " + times[1])
        print "----------------"

        # return the store array - could return time_store array too                          
        return store

# Test variables
a = (1, 3)
b = (11, 12)
c = (6, 9)
d = (2, 5)
e = (1, 5)
f = (2, 3)
g = (1, 4)
h = (1, 5)
i = (2, 8)
j = (11, 14)
k = (16, 18)

em_times= [a, b, c, d, e, f, g, h, i, j, k]

# test
meet_times(em_times)

