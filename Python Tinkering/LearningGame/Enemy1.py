class Enemy1:

##  nmeCount = 0
##   Common base class for all enemies

   def __init__(self):
##      self.enemy_trait = Enemy.random_enemy()
      self.enemy_name = enemy_trait[0]
      self.enemy_hit_points = enemy_trait[1]
      self.enemy_attack_str = enemy_trait[2]
      self.enemy_dodge = enemy_trait[3]
      self.enemy_accuracy = enemy_trait[4]
      enemy = [self.enemy_name, self.enemy_hit_points, self.enemy_attack_str, self.enemy_dodge, self.enemy_accuracy]
   ##   Enemy.nmeCount += 1
   ##   Enemy.displayEnemy(self)
      return enemy
   ##      self.name = name
   ##      self.salary = salary
   ##      Employee.nmeCount += 1

def random_enemy():
   '''(None) -> list

   Returns a list of enemy details for a randomly selected enemy

   >>>random_enemy()
   enemy
   '''
   import random

##   list_of_enemies = [count(), alpha()]
   list_of_enemies = make_enemy_list()
   random_selection = random.randrange(0, len(list_of_enemies))
   
   print ("Your enemy is a ", list_of_enemies[random_selection][0], ".")
   print ("It's just a little guy with ", list_of_enemies[random_selection][1], "hp.")
   
   return list_of_enemies[random_selection]

def make_enemy_list():

   '''(None) -> list of list of [str, numbers]

   Returns a list of enemies and their attributes

   >>>make_enemy_list()
   list of enemies
   '''

   import random
   enemy_list = []

   name = 'Count'
   hit_points = random.randrange(1, 100+1)
   attack_str = random.randrange(10, 30+1)
   dodge = random.randrange(30, 50+1)
   accuracy = random.randrange(40, 60+1)
   count_trait = [name, hit_points, attack_str, dodge, accuracy]
   enemy_list.append(count_trait)

   name = 'Alpha'
   hit_points = random.randrange(1, 100+1)
   attack_str = random.randrange(10, 30+1)
   dodge = random.randrange(30, 50+1)
   accuracy = random.randrange(40, 60+1)
   alpha_trait = [name, hit_points, attack_str, dodge, accuracy]
   enemy_list.append(alpha_trait)

   name = 'Tonneuve'
   hit_points = random.randrange(1, 100+1)
   attack_str = random.randrange(10, 30+1)
   dodge = random.randrange(30, 50+1)
   accuracy = random.randrange(40, 60+1)
   tonneuve_trait = [name, hit_points, attack_str, dodge, accuracy]
   enemy_list.append(tonneuve_trait)
  
   return enemy_list

def displayCount(self):
  print ("Total Enemies %d" % Enemy.nmeCount)

def displayEnemy(self):
##   print ("Name : ", self.name,  ", Salary: ", self.salary)
   print ("Your enemy is a ", self.enemy_name, ".")
   print ("It's just a little guy with ", self.enemy_hit_points, "hp.")

      
##"This would create first object of Employee class"
##emp1 = Employee("Zara", 2000)
##"This would create second object of Employee class"
##emp2 = Employee("Manni", 5000)
##emp1.displayEmployee()
##emp2.displayEmployee()
##print ("Total Employee %d" % Employee.empCount)
##

