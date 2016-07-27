# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 00:50:08 2016

@author: pi
"""

from pyevolve import Util
from pyevolve import GTree
from pyevolve import GSimpleGA
from pyevolve import Consts
from pyevolve import Selectors
import math

rmse_accum = Util.ErrorAccumulator()

def gp_add(a, b): return a+b
def gp_sub(a, b): return a-b
def gp_mul(a, b): return a*b
def gp_sqrt(a):   return math.sqrt(abs(a))

def step_callback(gp_engine):
    if gp_engine.getCurrentGeneration() == 0:
        GTree.GTreeGP.writePopulationDot(gp_engine, "trees.jpg", start=0, end=3)
        

def eval_func(chromosome):
   global rmse_accum
   rmse_accum.reset()
   code_comp = chromosome.getCompiledCode()

   for a in xrange(0, 5):
      for b in xrange(0, 5):
         evaluated     = eval(code_comp)
         target        = math.sqrt((a*a)+(b*b))
         rmse_accum   += (target, evaluated)

   return rmse_accum.getRMSE()

def main_run():
    
   genome = GTree.GTreeGP()
   genome.setParams(max_depth=4, method="ramped")
   genome.evaluator += eval_func

   ga = GSimpleGA.GSimpleGA(genome)
   ga.setParams(gp_terminals       = ['a', 'b'],
                gp_function_prefix = "gp")
    
   #ga.stepCallback.set(step_callback)

   ga.setMinimax(Consts.minimaxType["minimize"])
   ga.setGenerations(50)
   ga.setCrossoverRate(1.0)
   ga.setMutationRate(0.25)
   ga.setPopulationSize(800)
   
 
   ga(freq_stats=1)
   best = ga.bestIndividual()
   print best
   ga.printStats()
   ga.getStatistics()
   #ga.dumpStatsDB()
#==============================================================================
#    
#    csv_adapter = DBFileCSV(identify="run1", filename="stats.csv")
#    ga.setDBAdapter(csv_adapter)
#    
#    urlpost_adapter = DBURLPost("http://localhost/post.py", identify="run1", frequency=100)
#    ga.setDBAdapter(urlpost_adapter)
#==============================================================================

if __name__ == "__main__":
   #main_run()
   genome = GTree.GTreeGP()
   genome.setParams(max_depth=6, method="ramped")
   genome.evaluator += eval_func

   ga = GSimpleGA.GSimpleGA(genome)
   ga.setParams(gp_terminals       = ['a', 'b'],
                gp_function_prefix = "gp")
                
   ga.selector.set(Selectors.GRouletteWheel)
   ga.setMinimax(Consts.minimaxType["minimize"])
   ga.setGenerations(5000)
   ga.setCrossoverRate(0.1)
   ga.setMutationRate(0.01)
   ga.setPopulationSize(10000)
   ga.setElitism(True)
   ga(freq_stats=1)
   best = ga.bestIndividual()
   print best

#==============================================================================
#    
 #main_run()
#==============================================================================
#    genome = GTree.GTreeGP()
#    genome.setParams(max_depth=6, method="ramped")
#    genome.evaluator += eval_func
# 
#    ga = GSimpleGA.GSimpleGA(genome)
#    ga.setParams(gp_terminals       = ['a', 'b'],
#                 gp_function_prefix = "gp")
#                 
#    ga.selector.set(Selectors.GRouletteWheel)
#    ga.setMinimax(Consts.minimaxType["minimize"])
#    ga.setGenerations(5000)
#    ga.setCrossoverRate(0.3)
#    ga.setMutationRate(0.03)
#    ga.setPopulationSize(1000)
#    ga.setElitism(False)
#    ga(freq_stats=1)
#    best = ga.bestIndividual()
#==============================================================================
#   print best
#    Gen. 4999 (99.98%): Max/Min/Avg Fitness(Raw) [11.89(414.16)/9.86(0.00)/9.91(9.91)]
# Gen. 5000 (100.00%): Max/Min/Avg Fitness(Raw) [14.13(414.16)/11.70(0.00)/11.77(11.77)]
# Total time elapsed: 17040.395 seconds.
# - GenomeBase
# 	Score:			 0.000000
# 	Fitness:		 11.703095
# 
# 	Params:		 {'max_depth': 6, 'method': 'ramped'}
# 
# 	Slot [Evaluator] (Count: 1)
# 	Slot [Initializator] (Count: 1)
# 		Name: GTreeGPInitializator - Weight: 0.50
# 		Doc: This initializator accepts the follow parameters:
#       
#    *max_depth*
#       The max depth of the tree
# 
#    *method*
#       The method, accepts "grow", "full" or "ramped"
# 
#    .. versionadded:: 0.6
#       The *GTreeGPInitializator* function.
#    
# 	Slot [Mutator] (Count: 1)
# 		Name: GTreeGPMutatorSubtree - Weight: 0.50
# 		Doc:  The mutator of GTreeGP, Subtree Mutator
# 
#    This mutator will recreate random subtree of the tree using the grow algorithm.
#    
#    .. versionadded:: 0.6
#       The *GTreeGPMutatorSubtree* function
#    
# 	Slot [Crossover] (Count: 1)
# 		Name: GTreeGPCrossoverSinglePoint - Weight: 0.50
# 		Doc:  The crossover of the GTreeGP, Single Point for Genetic Programming
# 
#    ..note:: This crossover method creates offspring with restriction of the
#             *max_depth* parameter.
#    
#    Accepts the *max_attempt* parameter, *max_depth* (required).   
#    
# 
# - GTree
# 	Height:			3
# 	Nodes:			8
# 
# GTreeNodeBase [Childs=1] - [gp_sqrt]
#   GTreeNodeBase [Childs=2] - [gp_add]
#     GTreeNodeBase [Childs=2] - [gp_mul]
#       GTreeNodeBase [Childs=0] - [b]
#       GTreeNodeBase [Childs=0] - [b]
#     GTreeNodeBase [Childs=2] - [gp_mul]
#       GTreeNodeBase [Childs=0] - [a]
#==============================================================================
# 
#       GTreeNodeBase [Childs=0] - [a]
# 
# - GTreeGP
# 	Expression: gp_sqrt(gp_add(gp_mul(b, b), gp_mul(a, a)))
#==============================================================================
#==============================================================================
# 
# #2
# genome = GTree.GTreeGP()
#    genome.setParams(max_depth=6, method="ramped")
#    genome.evaluator += eval_func
# 
#    ga = GSimpleGA.GSimpleGA(genome)
#    ga.setParams(gp_terminals       = ['a', 'b'],
#                 gp_function_prefix = "gp")
#                 
#    ga.selector.set(Selectors.GRouletteWheel)
#    ga.setMinimax(Consts.minimaxType["minimize"])
#    ga.setGenerations(5000)
#    ga.setCrossoverRate(0.3)
#    ga.setMutationRate(0.03)
#    ga.setPopulationSize(1000)
#    ga.setElitism(True)
#    ga(freq_stats=1)
#    best = ga.bestIndividual()
#    print best
# Gen. 4996 (99.92%): Max/Min/Avg Fitness(Raw) [15.81(977.82)/13.14(0.00)/13.17(13.17)]
# Gen. 4997 (99.94%): Max/Min/Avg Fitness(Raw) [13.83(714.68)/11.49(0.00)/11.53(11.53)]
# Gen. 4998 (99.96%): Max/Min/Avg Fitness(Raw) [13.00(438.51)/10.78(0.00)/10.83(10.83)]
# Gen. 4999 (99.98%): Max/Min/Avg Fitness(Raw) [12.24(382.90)/10.14(0.00)/10.20(10.20)]
# Gen. 5000 (100.00%): Max/Min/Avg Fitness(Raw) [14.10(1245.41)/11.73(0.00)/11.75(11.75)]
# Total time elapsed: 17853.219 seconds.
# - GenomeBase
# 	Score:			 0.000000
# 	Fitness:		 11.727062
# 
# 	Params:		 {'max_depth': 6, 'method': 'ramped'}
# 
# 	Slot [Evaluator] (Count: 1)
# 	Slot [Initializator] (Count: 1)
# 		Name: GTreeGPInitializator - Weight: 0.50
# 		Doc: This initializator accepts the follow parameters:
#       
#    *max_depth*
#       The max depth of the tree
# 
#    *method*
#       The method, accepts "grow", "full" or "ramped"
# 
#    .. versionadded:: 0.6
#       The *GTreeGPInitializator* function.
#    
# 	Slot [Mutator] (Count: 1)
# 		Name: GTreeGPMutatorSubtree - Weight: 0.50
# 		Doc:  The mutator of GTreeGP, Subtree Mutator
# 
#    This mutator will recreate random subtree of the tree using the grow algorithm.
#    
#    .. versionadded:: 0.6
#       The *GTreeGPMutatorSubtree* function
#    
# 	Slot [Crossover] (Count: 1)
# 		Name: GTreeGPCrossoverSinglePoint - Weight: 0.50
# 		Doc:  The crossover of the GTreeGP, Single Point for Genetic Programming
# 
#    ..note:: This crossover method creates offspring with restriction of the
#             *max_depth* parameter.
#    
#    Accepts the *max_attempt* parameter, *max_depth* (required).   
#    
# 
# - GTree
# 	Height:			3
# 	Nodes:			8
# 
# GTreeNodeBase [Childs=1] - [gp_sqrt]
#   GTreeNodeBase [Childs=2] - [gp_add]
#     GTreeNodeBase [Childs=2] - [gp_mul]
#       GTreeNodeBase [Childs=0] - [a]
#       GTreeNodeBase [Childs=0] - [a]
#     GTreeNodeBase [Childs=2] - [gp_mul]
#==============================================================================
#==============================================================================
#       GTreeNodeBase [Childs=0] - [b]
#       GTreeNodeBase [Childs=0] - [b]
# 
# - GTreeGP
# 	Expression: gp_sqrt(gp_add(gp_mul(a, a), gp_mul(b, b)))
#==============================================================================
