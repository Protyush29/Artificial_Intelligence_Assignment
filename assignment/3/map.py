import numpy as np
from numpy import *
np.set_printoptions(threshold=np.inf)
from Queue import Queue
import time


class Node(object):
    def __init__(self,parent,val,depth):
        self.parent=parent
        self.val=val
	self.depth=depth
    def get_val(self):
        return self.val
    def get_parent(self):
        return self.parent

    def get_depth(self):
	return self.depth
        
        
#Getting Inputs Ready
def get_content(path):
        with  open(path) as f:
            content = f.readlines()
	#print content
        content= [list(x.strip()) for x in content]
        map_content = np.asanyarray(content,dtype='|S6')
        return map_content


#finding the path
def print_path(goal,map_content,out,goal_count):
        
        node=goal.get_parent()
        while(True):
            
            
            pos=node.get_val()
            if map_content[pos] != 's':
                map_content[pos]='o'
                node=node.get_parent()
                map_content_string=""
                for i in range(map_content.shape[0]):
                	for j in range(map_content.shape[1]):
                		map_content_string+=map_content[i][j]
                	map_content_string+='\n'
                	
                f = open(out+'path.txt', 'w')
	        file_contents = f.write(map_content_string.decode('unicode-escape').encode('utf-8'))
		
	        f.close()
                
                #below code for visualizing path in files [out+'path.txt']
                '''
	        f = open(out+'path.txt', 'r')
		file_contents = f.read()
		print (file_contents)
		f.close()
		'''
		      
            else: break
                
           
        return


#Function for Breadth first search


def bfs(map_path,out):
            
            
            map_content=get_content(map_path)
            map_path_state=get_content(map_path)
            map_queue=Queue()
            start_point=np.where(map_content=='s')
            
	    root=Node(None,start_point,1)
            iteration_count=map_content.shape[0]*map_content.shape[1]
            print iteration_count
            goal_count=0
            goal_position=list()
            
            map_queue.put(root)
            


            while (iteration_count>0):
		
                iteration_count-=1
                
                if map_queue.empty():
                    break
                    
                Possible_direction=[0,0,0,0]
                node=map_queue.get()
                node_pos=node.get_val()
                
                
                
                
                if map_content[node_pos]!='s':
                    map_content[node_pos]='d'
                    
                if map_content[node_pos[0]-1,node_pos[1]]=='*' or map_content[node_pos[0]-1,node_pos[1]]==' ':
                    
		   child=Node(node,(node_pos[0]-1,node_pos[1]),node.get_depth()+1)
		   map_queue.put(child)
		   Possible_direction[0]=1

                   if map_content[node_pos[0]-1,node_pos[1]]=='*':
                    	k=node_pos[0]-1
                    	m=node_pos[1]
                        goal_position.append((int(k),int(m)))
                        goal_count+=1
                        print_path(child,map_path_state,out,goal_count)
                       
                   map_content[node_pos[0]-1,node_pos[1]]='.'    
                    
                       
		        

                if map_content[node_pos[0],node_pos[1]+1]=='*' or map_content[node_pos[0],node_pos[1]+1]==' ':
                    
                    child=Node(node,(node_pos[0],node_pos[1]+1),node.get_depth()+1)
                    map_queue.put(child)
                    Possible_direction[3]=1
                    if map_content[node_pos[0],node_pos[1]+1]=='*':
                    	k=node_pos[0]
                    	m=node_pos[1]+1
                        goal_position.append((int(k),int(m)))
                        goal_count+=1
                        print_path(child,map_path_state,out,goal_count)
                        
                    map_content[node_pos[0],node_pos[1]+1]='.'    
                
                        
                        

                if map_content[node_pos[0]+1,node_pos[1]]=='*' or map_content[node_pos[0]+1,node_pos[1]]==' ':
                    
                    child=Node(node,(node_pos[0]+1,node_pos[1]),node.get_depth()+1)
                    map_queue.put(child)
                    Possible_direction[1]=1

                    if map_content[node_pos[0]+1,node_pos[1]]=='*':
                    	k=node_pos[0]+1
                    	m=node_pos[1]
                        goal_position.append((int(k),int(m)))
                        goal_count+=1
                        print_path(child,map_path_state,out,goal_count)
			
                        
                    map_content[node_pos[0]+1,node_pos[1]]='.'   
                    
                        

                if map_content[node_pos[0],node_pos[1]-1]=='*' or map_content[node_pos[0],node_pos[1]-1]==' ':
	            child=Node(node,(node_pos[0],node_pos[1]-1),node.get_depth()+1)
                    map_queue.put(child)
                    Possible_direction[2]=1
                    
                    if map_content[node_pos[0],node_pos[1]-1]=='*':
                    	k=node_pos[0]
                    	m=node_pos[1]-1
                        goal_position.append((int(k),int(m)))
                        goal_count+=1
                        print_path(child,map_path_state,out,goal_count)
                    map_content[node_pos[0],node_pos[1]-1]='.'  
                    
                    
                    
                    
                if Possible_direction == [1,0,0,0]:
                    map_content[node_pos] = "\u2575"
                elif Possible_direction == [0,1,0,0]:
                    map_content[node_pos] = "\u2577"
                elif Possible_direction == [0,0,1,0]:
                    map_content[node_pos] = "\u2576"
                elif Possible_direction == [0,0,0,1]:
                    map_content[node_pos] = "\u2574"
                elif Possible_direction == [1,1,0,0]:
                    map_content[node_pos] = "\u2502"
                elif Possible_direction == [1,0,1,0]:
                    map_content[node_pos] = "\u2514"
                elif Possible_direction == [1,0,0,1]:
                    map_content[node_pos] = "\u2518"
                elif Possible_direction == [0,1,1,0]:
                    map_content[node_pos] = "\u250C"
                elif Possible_direction == [0,1,0,1]:
                    map_content[node_pos] = "\u2510"
                elif Possible_direction == [0,0,1,1]:
                    map_content[node_pos] = "\u2500"
                elif Possible_direction == [0,1,1,1]:
                    map_content[node_pos] = "\u252C"
                elif Possible_direction == [1,0,1,1]:
                    map_content[node_pos] = "\u2534"
                elif Possible_direction == [1,1,1,1]:
                    map_content[node_pos] = "\u253C"
                elif Possible_direction == [1,1,0,1]:
                    map_content[node_pos] = "\u2524"
                elif Possible_direction == [1,1,1,0]:
                    map_content[node_pos] = "\u251C"
                else:
                    map_content[node_pos] = "\u2576"
                 
                map_content_string=""
                for i in range(map_content.shape[0]):
                	for j in range(map_content.shape[1]):
                		map_content_string+=map_content[i][j]
                	map_content_string+='\n'
                	
                f = open(out+'.txt', 'w')
		f.write(map_content_string.decode('unicode-escape').encode('utf-8'))
		
		f.close()
                	   
                #below code for visualization
                
                    
                '''
		f = open(out+'.txt', 'r')
		file_contents = f.read()
		print (file_contents)
		f.close()
		#time.sleep(0.1)
		'''

            for i in goal_position:
                map_content[i]='G'
            
            map_content_string=""
            for i in range(map_content.shape[0]):
		for j in range(map_content.shape[1]):
			map_content_string+=map_content[i][j]
		map_content_string+='\n'
                	
            f = open(out+'.txt', 'w')
            f.write(map_content_string.decode('unicode-escape').encode('utf-8'))
		
            f.close()  
            print ("\n Goals discoverable by BFS for the map is= {}".format(goal_count))
            print ("Goal positions are={}".format(goal_position))
            return (goal_count,goal_position)
        
'''             
goal_count_1,goal_pos_1=bfs("map1.txt",'out1_bfs')       
goal_count_2,goal_pos_2=bfs("map2.txt",'out2_bfs') 
goal_count_3,goal_pos_3=bfs("map3.txt",'out3_bfs') 
'''

#Function for Depth first search


def dfs(map_path,out):
            
            map_content=get_content(map_path)
            map_path_state=get_content(map_path)
            map_queue=list()
            start_point=np.where(map_content=='s')
            
	    root=Node(None,start_point,1)
            iteration_count=map_content.shape[0]*map_content.shape[1]
            
            goal_count=0
            goal_position=list()
            
            map_queue.append(root)
            


            while (iteration_count>0):

                iteration_count-=1
                
                if len(map_queue)==0:
                    break
                Possible_direction=[0,0,0,0]
                node=map_queue.pop()
                node_pos=node.get_val()
                
                if map_content[node_pos]!='s':
                    map_content[node_pos]='d'
                    
                    
                
		
                    
		if map_content[node_pos[0]-1,node_pos[1]]=='*' or map_content[node_pos[0]-1,node_pos[1]]==' ':
			child=Node(node,(node_pos[0]-1,node_pos[1]),node.get_depth()+1)
			map_queue.append(child)
			Possible_direction[0]=1
			if map_content[node_pos[0]-1,node_pos[1]]=='*':
				k=node_pos[0]-1
				m=node_pos[1]
				goal_position.append((int(k),int(m)))
				goal_count+=1
				print_path(child,map_path_state,out,goal_count)
			map_content[node_pos[0]-1,node_pos[1]]='.'
		
		if map_content[node_pos[0],node_pos[1]-1]=='*' or map_content[node_pos[0],node_pos[1]-1]==' ':
			child=Node(node,(node_pos[0],node_pos[1]-1),node.get_depth()+1)
			map_queue.append(child)
			Possible_direction[2]=1
			if map_content[node_pos[0],node_pos[1]-1]=='*':
				k=node_pos[0]
				m=node_pos[1]-1
				goal_position.append((int(k),int(m)))
				goal_count+=1
				print_path(child,map_path_state,out,goal_count)
			map_content[node_pos[0],node_pos[1]-1]='.'
						
						

				   
						
						
		if map_content[node_pos[0],node_pos[1]+1]=='*' or map_content[node_pos[0],node_pos[1]+1]==' ':
			child=Node(node,(node_pos[0],node_pos[1]+1),node.get_depth()+1)
			map_queue.append(child)
			Possible_direction[3]=1
			if map_content[node_pos[0],node_pos[1]+1]=='*':
				k=node_pos[0]
				m=node_pos[1]+1
				goal_position.append((int(k),int(m)))
				goal_count+=1
				print_path(child,map_path_state,out,goal_count)
			map_content[node_pos[0],node_pos[1]+1]='.'
			
			
		if map_content[node_pos[0]+1,node_pos[1]]=='*' or map_content[node_pos[0]+1,node_pos[1]]==' ':
			child=Node(node,(node_pos[0]+1,node_pos[1]),node.get_depth()+1)
			map_queue.append(child)
			Possible_direction[1]=1
			if map_content[node_pos[0]+1,node_pos[1]]=='*':
				k=node_pos[0]+1
				m=node_pos[1]
				goal_position.append((int(k),int(m)))
				goal_count+=1
				print_path(child,map_path_state,out,goal_count)
			map_content[node_pos[0]+1,node_pos[1]]='.'    
			
		
			
			
		
			
		if Possible_direction == [1,0,0,0]:
			map_content[node_pos] = "\u2575"
		elif Possible_direction == [0,1,0,0]:
			map_content[node_pos] = "\u2577"
		elif Possible_direction == [0,0,1,0]:
			map_content[node_pos] = "\u2576"
		elif Possible_direction == [0,0,0,1]:
			map_content[node_pos] = "\u2574"
		elif Possible_direction == [1,1,0,0]:
			map_content[node_pos] = "\u2502"
		elif Possible_direction == [1,0,1,0]:
			map_content[node_pos] = "\u2514"
		elif Possible_direction == [1,0,0,1]:
			map_content[node_pos] = "\u2518"
		elif Possible_direction == [0,1,1,0]:
			map_content[node_pos] = "\u250C"
		elif Possible_direction == [0,1,0,1]:
			map_content[node_pos] = "\u2510"
		elif Possible_direction == [0,0,1,1]:
			map_content[node_pos] = "\u2500"
		elif Possible_direction == [0,1,1,1]:
			map_content[node_pos] = "\u252C"
		elif Possible_direction == [1,0,1,1]:
			map_content[node_pos] = "\u2534"
		elif Possible_direction == [1,1,1,1]:
			map_content[node_pos] = "\u253C"
		elif Possible_direction == [1,1,0,1]:
			map_content[node_pos] = "\u2524"
		elif Possible_direction == [1,1,1,0]:
			map_content[node_pos] = "\u251C"
		else:
			map_content[node_pos] = "\u2576"
		 
		map_content_string=""
		for i in range(map_content.shape[0]):
			for j in range(map_content.shape[1]):
				map_content_string+=map_content[i][j]
			map_content_string+='\n'
						
		f = open(out+'.txt', 'w')
		f.write(map_content_string.decode('unicode-escape').encode('utf-8'))
			
		f.close()
						   
		#below code for visualization
					
						
		'''
		f = open(out+'.txt', 'r')
		file_contents = f.read()
		print (file_contents)
		f.close()
		#time.sleep(0.1)
		'''

            for i in goal_position:
                map_content[i]='G'
            map_content_string=""
            for i in range(map_content.shape[0]):
        	for j in range(map_content.shape[1]):
        		map_content_string+=map_content[i][j]
        	map_content_string+='\n'
                	
            f = open(out+'.txt', 'w')
            file_contents = f.write(map_content_string.decode('unicode-escape').encode('utf-8'))
		
            f.close()  
            print ("\n Goals discoverable by DFS for the map is= {}".format(goal_count))
            print ("Goal positions are={}".format(goal_position))
            return (goal_count,goal_position)
        
             
'''
goal_count_1,goal_pos_1=dfs("map1.txt",'out1_dfs')       
goal_count_2,goal_pos_2=dfs("map2.txt",'out2_dfs') 
goal_count_3,goal_pos_3=dfs("map3.txt",'out3_dfs') 
'''
#Function for IDFS

def idfs(map_path,out):
            
            map_content=get_content(map_path)
            map_path_state=get_content(map_path)
            
            limit=1
            
            goal_count=0
	    goal_position=list()
	    map_queue=list()
	    start_point=np.where(map_content=='s')
	    root=Node(None,start_point,1)
            iteration_count=map_content.shape[0]*map_content.shape[1]
            map_queue.append(root)

			
						
	    while (iteration_count>0 ) :
			
			
			
			
			iteration_count-=1
			
			if len(map_queue)==0:
				
				break
			Possible_direction=[0,0,0,0]
			node=map_queue.pop()
			node_pos=node.get_val()
			
			if map_content[node_pos]!='s':
				map_content[node_pos]='d'
				
				
			
			if (node.get_depth()<=limit):
				
				if map_content[node_pos[0]-1,node_pos[1]]=='*' or map_content[node_pos[0]-1,node_pos[1]]==' ':
					child=Node(node,(node_pos[0]-1,node_pos[1]),node.get_depth()+1)
					map_queue.append(child)
					Possible_direction[0]=1
					
					if map_content[node_pos[0]-1,node_pos[1]]=='*':
						k=node_pos[0]-1
						m=node_pos[1]
						goal_position.append((int(k),int(m)))
						goal_count+=1
						print_path(child,map_path_state,out,goal_count)
					map_content[node_pos[0]-1,node_pos[1]]='.'
			
				if map_content[node_pos[0],node_pos[1]-1]=='*' or map_content[node_pos[0],node_pos[1]-1]==' ':
					child=Node(node,(node_pos[0],node_pos[1]-1),node.get_depth()+1)
					map_queue.append(child)
					Possible_direction[2]=1
					
					if map_content[node_pos[0],node_pos[1]-1]=='*':
						k=node_pos[0]
						m=node_pos[1]-1
						goal_position.append((int(k),int(m)))
						goal_count+=1
						print_path(child,map_path_state,out,goal_count)
					map_content[node_pos[0],node_pos[1]-1]='.'
				
				

			   
				
				
				if map_content[node_pos[0],node_pos[1]+1]=='*' or map_content[node_pos[0],node_pos[1]+1]==' ':
					child=Node(node,(node_pos[0],node_pos[1]+1),node.get_depth()+1)
					map_queue.append(child)
					Possible_direction[3]=1
					
					if map_content[node_pos[0],node_pos[1]+1]=='*':
						k=node_pos[0]
						m=node_pos[1]+1
						goal_position.append((int(k),int(m)))
						goal_count+=1
						print_path(child,map_path_state,out,goal_count)
					map_content[node_pos[0],node_pos[1]+1]='.'
				
				
				if map_content[node_pos[0]+1,node_pos[1]]=='*' or map_content[node_pos[0]+1,node_pos[1]]==' ':
					child=Node(node,(node_pos[0]+1,node_pos[1]),node.get_depth()+1)
					map_queue.append(child)
					Possible_direction[1]=1
					
					if map_content[node_pos[0]+1,node_pos[1]]=='*':
						k=node_pos[0]+1
						m=node_pos[1]
						goal_position.append((int(k),int(m)))
						goal_count+=1
						print_path(child,map_path_state,out,goal_count)
					map_content[node_pos[0]+1,node_pos[1]]='.'    
				
			        
				if Possible_direction == [1,0,0,0]:
					map_content[node_pos] = "\u2575"
				elif Possible_direction == [0,1,0,0]:
					map_content[node_pos] = "\u2577"
				elif Possible_direction == [0,0,1,0]:
					map_content[node_pos] = "\u2576"
				elif Possible_direction == [0,0,0,1]:
					map_content[node_pos] = "\u2574"
				elif Possible_direction == [1,1,0,0]:
					map_content[node_pos] = "\u2502"
				elif Possible_direction == [1,0,1,0]:
					map_content[node_pos] = "\u2514"
				elif Possible_direction == [1,0,0,1]:
					map_content[node_pos] = "\u2518"
				elif Possible_direction == [0,1,1,0]:
					map_content[node_pos] = "\u250C"
				elif Possible_direction == [0,1,0,1]:
					map_content[node_pos] = "\u2510"
				elif Possible_direction == [0,0,1,1]:
					map_content[node_pos] = "\u2500"
				elif Possible_direction == [0,1,1,1]:
					map_content[node_pos] = "\u252C"
				elif Possible_direction == [1,0,1,1]:
					map_content[node_pos] = "\u2534"
				elif Possible_direction == [1,1,1,1]:
					map_content[node_pos] = "\u253C"
				elif Possible_direction == [1,1,0,1]:
					map_content[node_pos] = "\u2524"
				elif Possible_direction == [1,1,1,0]:
					map_content[node_pos] = "\u251C"
				else:
					map_content[node_pos] = "\u2576"
				 
			
			
				map_content_string=""
				for i in range(map_content.shape[0]):
					for j in range(map_content.shape[1]):
						map_content_string+=map_content[i][j]
					map_content_string+='\n'
				
				f = open(out+'.txt', 'w')
				file_contents = f.write(map_content_string.decode('unicode-escape').encode('utf-8'))
				f.close()
				
				
				
			else: 
				if (len(map_queue)!=0):
					limit+=1
				else: 
					#print("break2")
					break
				map_content=get_content(map_path)
				map_queue=list()
				start_point=np.where(map_content=='s')
				root=Node(None,start_point,1)
				map_queue.append(root)
				iteration_count=map_content.shape[0]*map_content.shape[1]
				goal_count=0
				goal_position=list()
				
				   
			#below code for visualization
			
				
			'''
			f = open(out+'.txt', 'r')
			file_contents = f.read()
			print (file_contents)
			f.close()
			time.sleep(0.1)
			'''
			
		

			
	    for i in goal_position:
                map_content[i]='G'
            map_content_string=""
            for i in range(map_content.shape[0]):
        	for j in range(map_content.shape[1]):
        		map_content_string+=map_content[i][j]
        	map_content_string+='\n'
                	
            f = open(out+'.txt', 'w')
            file_contents = f.write(map_content_string.decode('unicode-escape').encode('utf-8'))
		
            f.close()  
            print ("\n Goals discoverable by IDFS for the map is= {}".format(goal_count))
            print ("Goal positions are={}".format(goal_position))
            return (goal_count,goal_position)
        
             

goal_count_1,goal_pos_1=idfs("map1.txt",'out1_idfs')       
goal_count_2,goal_pos_2=idfs("map2.txt",'out2_idfs') 
goal_count_3,goal_pos_3=idfs("map3.txt",'out3_idfs') 





