import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self,**kwargs):
    assert len(list(kwargs))>0  , "Must contain at least one ball"
    assert sum(kwargs.values())>0,"Must contain at least one ball (dict values)" 
    self.contents=[]
    for k,v in kwargs.items():
      for c in range(v):
        self.contents.append(k)
  def draw(self,nb_balls_draw):
    return_copy_contents=[]
    if nb_balls_draw > len(self.contents):
      return self.contents
    else:
      for i in range(nb_balls_draw):
        random_pick=random.choice(self.contents)
        self.contents.remove(random_pick)
        return_copy_contents.append(random_pick)
      return return_copy_contents
def hat2_in_hat1(hat1,hat2):
  hat11=copy.deepcopy(hat1)
  hat22=copy.deepcopy(hat2)
    #returns True if all balls in hat 2 exist in h1 else returns False
  ret=False
  for h2 in hat22:
      if h2 in hat11:
          hat11.remove(h2)
          ret=True
      else:
          ret=False
          break
          return ret
  return ret


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  
  expected_hat_contents=[]
  for k,v in expected_balls.items():
      for c in range(v):
        expected_hat_contents.append(k)
  
  drawn_list=[]
  for exp in range(num_experiments):
    copy_hat=copy.deepcopy(hat)
    drawn_list.append(copy_hat.draw(num_balls_drawn))
    
  M=0
  for drawn in drawn_list:
    if hat2_in_hat1(drawn,expected_hat_contents):
      
      M+=1
     
  return M/num_experiments

