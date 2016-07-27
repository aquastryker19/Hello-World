# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 04:05:12 2016

@author: pi
"""

#===============================================================================
# Pyevolve version of the Infinite Monkey Theorem
# See: http://en.wikipedia.org/wiki/Infinite_monkey_theorem
# By Jelle Feringa
#===============================================================================

from pyevolve import G1DList
from pyevolve import GSimpleGA, Consts
from pyevolve import Selectors
from pyevolve import Initializators, Mutators, Crossovers
import math

sentence = """
'Just living is not enough,' said the butterfly,
'one must have sunshine, freedom, and a little flower.'
"""
#==============================================================================
# sentence = """
# 'To be or not to be, that is the question.'
# """
# 
# sentence = """
# 'In this context, almost surely is a mathematical term with a precise meaning, and the monkey is not an actual monkey, but a metaphor for an abstract device that produces an endless random sequence of letters and symbols. One of the earliest instances of the use of the monkey metaphor is that of French mathematician Emile Borel in 1913,[1] but the first instance may be even earlier. The relevance of the theorem is questionable—the probability of a universe full of monkeys typing a complete work such as Shakespeare's Hamlet is so tiny that the chance of it occurring during a period of time hundreds of thousands of orders of magnitude longer than the age of the universe is extremely low (but technically not zero). It should also be noted that real monkeys do not produce uniformly random output, which means that an actual monkey hitting keys for an infinite amount of time has no statistical certainty of ever producing any given text.'
#==============================================================================
#"""

numeric_sentence = map(ord, sentence)

def evolve_callback(ga_engine):
   generation = ga_engine.getCurrentGeneration()
   if generation%50==0:
      indiv = ga_engine.bestIndividual()
      print ''.join(map(chr,indiv))
   return False

def run_main():
   genome = G1DList.G1DList(len(sentence))
   genome.setParams(rangemin=min(numeric_sentence),
                    rangemax=max(numeric_sentence),
                    bestrawscore=0.00,
                    gauss_mu=1, gauss_sigma=4)

   genome.initializator.set(Initializators.G1DListInitializatorInteger)
   genome.mutator.set(Mutators.G1DListMutatorIntegerGaussian)
   genome.evaluator.set(lambda genome: sum(
                           [abs(a-b) for a, b in zip(genome, numeric_sentence)]
                        ))

   ga = GSimpleGA.GSimpleGA(genome)
   #ga.stepCallback.set(evolve_callback)
   ga.setMinimax(Consts.minimaxType["minimize"])
   ga.terminationCriteria.set(GSimpleGA.RawScoreCriteria)
   ga.setPopulationSize(600)
   ga.setMutationRate(0.02)
   ga.setCrossoverRate(0.9)
   ga.setGenerations(5000)
   ga.evolve(freq_stats=1)

   best = ga.bestIndividual()
   print "Best individual score: %.2f" % (best.score,)
   print ''.join(map(chr, best))

if __name__ == "__main__":
   #run_main()
   genome = G1DList.G1DList(len(sentence))
   genome.setParams(rangemin=min(numeric_sentence),
                    rangemax=max(numeric_sentence),
                    bestrawscore=0.00,
                    gauss_mu=1, gauss_sigma=4)

   genome.initializator.set(Initializators.G1DListInitializatorInteger)
   genome.mutator.set(Mutators.G1DListMutatorIntegerGaussian)
   genome.evaluator.set(lambda genome: sum(
                           [abs(a-b) for a, b in zip(genome, numeric_sentence)]
                        ))

   ga = GSimpleGA.GSimpleGA(genome)
   #ga.stepCallback.set(evolve_callback)
   ga.setMinimax(Consts.minimaxType["minimize"])
   ga.terminationCriteria.set(GSimpleGA.RawScoreCriteria)
   ga.setPopulationSize(60)
   ga.setMutationRate(0.02)
   ga.setCrossoverRate(0.9)
   ga.setGenerations(5000)
   ga.evolve(freq_stats=100)

   best = ga.bestIndividual()
   print "Best individual score: %.2f" % (best.score,)
   print ''.join(map(chr, best))