#1145141919810
import string
import random
import time
#mod
print('Welcome!!! This script is written by ifly.')
time.sleep(3)
adjs = ["Albert","good","right",'mine','black','fire','cute','love','light','dark','green','blue','long','short','interesting']
nours = ['Chen','apple','Eevee','linux','steal','people','chicken','fox','bilibili','codemao','niko',"banana",'computer']
#list
adj = random.choice(adjs)
nour = random.choice(nours)
num = random.randrange(0,100)
biaodian = random.choice(string.punctuation)
passwd = adj + nour + str(num) + biaodian
print("-" * 30)
print('Your password is %s' % passwd)
print("-"*30)

















