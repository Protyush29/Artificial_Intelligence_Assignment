import numpy as np

class Node(object):
    """docstring for Node. Contains the state of each puzzle with hueristic score,depth and parent. Puzzle is an np array and depth and hueristic is numeric and parent is object of Node type"""
    def __init__(self, parent ,puzzle ,depth ,hueristic):
        self.puzzle = puzzle
        self.parent = parent
        self.depth = depth
        self.hueristic = hueristic
        self.score=self.depth+self.hueristic
    def get_puzzle(self):
        return self.puzzle
    def get_parent(self):
        return self.parent
    def get_depth(self):
	    return self.depth
    def get_heuristic(self):
	    return self.heuristic
    def get_score(self):
	    return self.score

#printing the path
def print_path(goal):

        node=goal.get_parent()
        while(True):
            print(node.get_puzzle())
            if node.get_parent!=None:
                node=node.get_parent

            else: break
            return


# manhatten distance
def calculate_heuristic_score(puzzle):
        goal_state = np.array([[1,2,3],[4,5,6],[7,8,0]])
        heuristic=0
        for i in range(puzzle.shape[0]):
            for j in range(puzzle.shape[1]):
                row,column=np.where(goal_state==puzzle[i,j])
                heuristic=heuristic+np.abs(row-i)+np.abs(column-j)
        return heuristic



def A_star_algorithm():

        goal_state = np.array([[0,1,2],[3,4,5],[6,7,8]])
        start_state = np.array([[8,7,6],[5,1,4],[2,0,3]])
        root = Node(None ,start_state ,1 ,calculate_heuristic_score(start_state))
        Tree_list=list()
        Tree_list.append(root)

        while(True):

            if len(Tree_list)==0:
                break
            node=Tree_list.pop()
            puzzle=node.get_puzzle()
            puzzle1=np.copy(puzzle)
            puzzle2=np.copy(puzzle)
            puzzle3=np.copy(puzzle)
            puzzle4=np.copy(puzzle)


            if np.array_equal(puzzle,goal_state):
                print ("Puzzle Solved! Printing path")
                print_path(node)
                break

            else:
                empty_block_row,empty_block_column=np.where(puzzle==0)
                if empty_block_column+1>=0 and empty_block_column+1<goal_state.shape[1]:


                    temp=puzzle1[empty_block_row,empty_block_column+1]
                    puzzle1[empty_block_row,empty_block_column+1]=0
                    puzzle1[empty_block_row,empty_block_column]=temp
                    child = Node(node ,puzzle1 ,node.get_depth()+1 ,calculate_heuristic_score(puzzle1))

                    Tree_list.append(child)


                if empty_block_column-1>=0 and empty_block_column-1<goal_state.shape[1]:


                    temp=puzzle2[empty_block_row,empty_block_column-1]
                    puzzle2[empty_block_row,empty_block_column-1]=0
                    puzzle2[empty_block_row,empty_block_column]=temp
                    child = Node(node ,puzzle2 ,node.get_depth()+1 ,calculate_heuristic_score(puzzle2))

                    Tree_list.append(child)

                if empty_block_row-1>=0 and empty_block_row-1<goal_state.shape[0]:


                    temp=puzzle3[empty_block_row-1,empty_block_column]
                    puzzle3[empty_block_row-1,empty_block_column]=0
                    puzzle3[empty_block_row,empty_block_column]=temp
                    child = Node(node ,puzzle3 ,node.get_depth()+1 ,calculate_heuristic_score(puzzle3))

                    Tree_list.append(child)

                if empty_block_row+1>=0 and empty_block_row+1<goal_state.shape[0]:


                    temp=puzzle4[empty_block_row+1,empty_block_column]
                    puzzle4[empty_block_row+1,empty_block_column]=0
                    puzzle4[empty_block_row,empty_block_column]=temp
                    child = Node(node ,puzzle4 ,node.get_depth()+1 ,calculate_heuristic_score(puzzle4))

                    Tree_list.append(child)


                Tree_list=sorted(Tree_list, key=lambda Node: Node.score)
                Tree_list.reverse()

                continue

A_star_algorithm()


def Greedy_algorithm():

        goal_state = np.array([[0,1,2],[3,4,5],[6,7,8]])
        start_state = np.array([[8,7,6],[5,1,4],[2,0,3]])
        root = Node(None ,start_state ,1 ,calculate_heuristic_score(start_state))
        Tree_list=list()
        Tree_list.append(root)

        while(True):

            if len(Tree_list)==0:
                break
            node=Tree_list.pop()
            puzzle=node.get_puzzle()
            puzzle1=np.copy(puzzle)
            puzzle2=np.copy(puzzle)
            puzzle3=np.copy(puzzle)
            puzzle4=np.copy(puzzle)


            if np.array_equal(puzzle,goal_state):
                print ("Puzzle Solved! Printing path")
                print_path(node)
                break

            else:
                empty_block_row,empty_block_column=np.where(puzzle==0)
                if empty_block_column+1>=0 and empty_block_column+1<goal_state.shape[1]:


                    temp=puzzle1[empty_block_row,empty_block_column+1]
                    puzzle1[empty_block_row,empty_block_column+1]=0
                    puzzle1[empty_block_row,empty_block_column]=temp
                    child = Node(node ,puzzle1 ,node.get_depth()+1 ,calculate_heuristic_score(puzzle1))

                    Tree_list.append(child)


                if empty_block_column-1>=0 and empty_block_column-1<goal_state.shape[1]:


                    temp=puzzle2[empty_block_row,empty_block_column-1]
                    puzzle2[empty_block_row,empty_block_column-1]=0
                    puzzle2[empty_block_row,empty_block_column]=temp
                    child = Node(node ,puzzle2 ,node.get_depth()+1 ,calculate_heuristic_score(puzzle2))

                    Tree_list.append(child)

                if empty_block_row-1>=0 and empty_block_row-1<goal_state.shape[0]:


                    temp=puzzle3[empty_block_row-1,empty_block_column]
                    puzzle3[empty_block_row-1,empty_block_column]=0
                    puzzle3[empty_block_row,empty_block_column]=temp
                    child = Node(node ,puzzle3 ,node.get_depth()+1 ,calculate_heuristic_score(puzzle3))

                    Tree_list.append(child)

                if empty_block_row+1>=0 and empty_block_row+1<goal_state.shape[0]:


                    temp=puzzle4[empty_block_row+1,empty_block_column]
                    puzzle4[empty_block_row+1,empty_block_column]=0
                    puzzle4[empty_block_row,empty_block_column]=temp
                    child = Node(node ,puzzle4 ,node.get_depth()+1 ,calculate_heuristic_score(puzzle4))

                    Tree_list.append(child)


                Tree_list=sorted(Tree_list, key=lambda Node: Node.heuristic)
                Tree_list.reverse()

                continue

Greedy_algorithm()
