import numpy as np
import math
import itertools
import time

def distance_calculation_point(point1,point2):
        x1,y1=point1[1],point1[2]
        x2,y2=point2[1],point2[2]
        return(math.sqrt((x1-x2)**2+(y1-y2)**2))
def distance_calculation_sequence(sequence):
        length=sequence.shape[0]
        distance=0
        for i in range(length):
            if i==length-1:
                distance+=distance_calculation_point(sequence[i],sequence[0])
            else:
                distance+=distance_calculation_point(sequence[i],sequence[i+1])
        return distance


def user_input(path):
        map_content=np.loadtxt(path,dtype={'names': ('city', 'latitude', 'longitude'),'formats': ('S15', 'f4', 'f4')},delimiter=",",skiprows=1)
        return map_content

def possible_successor_calculations(sequence):
        length=sequence.shape[0]
        sequence_calculated=list()

        for i in range(length):
            #swaping to find possible successors

            if i==length-1:

                sequence_of_choice=np.copy(sequence)
                temp=np.copy(sequence_of_choice[i])
                sequence_of_choice[i]=sequence_of_choice[0]
                sequence_of_choice[0]=temp

                sequence_calculated.append((sequence_of_choice,distance_calculation_sequence(sequence_of_choice)))

            else:

                sequence_of_choice=np.copy(sequence)
                temp=sequence_of_choice[i].copy()
                sequence_of_choice[i]=sequence_of_choice[i+1]
                sequence_of_choice[i+1]=temp
                sequence_calculated.append((sequence_of_choice,distance_calculation_sequence(sequence_of_choice)))
        return np.array(sequence_calculated)

def print_distance_list(sequence_calculated):  #distance when a list of sequence given
    print sequence_calculated[0,0].shape
    for i in range(sequence_calculated.shape[0]):
        print "Distance={}>{}".format(i+1,sequence_calculated[i,1])

def print_distance(sequence):  #distance when a one sequence is given
    print sequence[1]


def steepest_ascend_hill_climbing(path):
    map_content=user_input(path)
    initial=possible_successor_calculations(map_content)
    successors_list=possible_successor_calculations(map_content)
    present_distance=distance_calculation_sequence(map_content)
    count=5

    while(True):
        row_min=np.argmin(successors_list[:,1][np.newaxis]) #minimum distance index
        successor_min_dis=successors_list[row_min,1]
        successor_next=successors_list[row_min,0]
        print "Distance={}".format(successor_min_dis)


        if present_distance>successor_min_dis and count!=0:
            present_distance=successor_min_dis
            successors_list=possible_successor_calculations(successor_next)


        else:
            if count>0:
                count-=1
                print "Best case derived="
                print successor_next
                if count!=0:
                    row=np.random.randint(0,initial.shape[0])
                    print "random start point being given row={}".format(row)
                    successors_list=possible_successor_calculations(initial[row,0])
                    present_distance=distance_calculation_sequence(initial[row,0])

            if count==0: break


print "steepest_ascend_hill_climbing output"
steepest_ascend_hill_climbing("cities_full.txt")


def simple_hill_climbing(path):
    map_content=user_input(path)
    successor_used=map_content
    present_distance=distance_calculation_sequence(successor_used)
    initial=possible_successor_calculations(map_content)
    successor_possible=possible_successor_calculations(map_content)
    index,count=0,5

    while(True):

        limit=successor_possible.shape[0]
        if successor_possible[index,1]<present_distance and index<limit and count!=0:
            successor_used=successor_possible[index,0]
            successor_possible=possible_successor_calculations(successor_used)
            present_distance=distance_calculation_sequence(successor_used)
            print "Distance {}".format(present_distance)
            index=0
        else:
            if index<limit-1:
                index+=1
                continue



            if index==limit-1 and count>0:
                count-=1
                print "count is:{}".format(count+1)
                print "Best case recieved is:"
                print successor_used
                row=np.random.randint(0,initial.shape[0])
                print "random start point being given row={}".format(row)
                successor_used=initial[row,0]
                successor_possible=possible_successor_calculations(successor_used)
                present_distance=distance_calculation_sequence(successor_used)
                index=0

            else:   break

print "simple_hill_climbing output"
simple_hill_climbing("cities_full.txt")

def simulated_annealing(path,start,period):
    map_content=user_input(path)
    successor_used=map_content
    present_distance=distance_calculation_sequence(successor_used)
    initial=possible_successor_calculations(map_content)
    successor_possible=possible_successor_calculations(map_content)
    index,count=0,10
    T=1000

    while(True):
        if time.time()>start+period:
            break
        T=T*(0.999)
        row=np.random.randint(0,successor_possible.shape[0])
        successor_used=successor_possible[row,0]
        successor_dis=successor_possible[row,1]
        print("Distance={}".format(present_distance))
        if present_distance>successor_dis:
            present_distance=successor_dis
            successor_possible=possible_successor_calculations(successor_used)

        else:
            E=present_distance-successor_dis
            pro=np.exp(E/T)
            if(np.random.random_sample()<pro):
                present_distance=successor_dis
                successor_possible=possible_successor_calculations(successor_used)
time1=1200 #20 mins
simulated_annealing("cities_full.txt",time.time(),time1)
