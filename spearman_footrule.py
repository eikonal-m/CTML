# -*- coding: utf-8 -*-
"""

Challenge #2: Spearman’s Footrule Distance

Suppose we have several different methods for scoring a set of items; perhaps 
we’re asking different people, or using different scoring algorithms. We’d like
 to figure out how to aggregate these to produce a single combined ranking.
A useful tool here is Spearman’s Footrule Distance which computes the distance
 between two rankings (Don’t worry, we don’t expect you to have heard of this 
                       before, we expect you to do some Googling…)
Your task here is to implement a function with the following signature:
def sumSpearmanDistances(scores, proposedRanking):
    
Calculate the sum of Spearman’s Footrule Distances for a given proposedRanking.
scores : A dict of {itemId: tuple of scores} e.g. {‘A’: [100, 0.1], ‘B’: [90, 0.3], ‘C’: [20, 0.2]}
means that item ‘A’ was given a score of 100 by metric 1 and a score of 0.1 by metric 2 etc
proposedRanking : An ordered list of itemIds where the first entry is the proposed-best and last entry is
the proposed worst e.g. [‘A’, ‘B’, ‘C’]
    
Please think about splitting your function into appropriate sub-functions and 
add tests to demonstrate that everything works as expected. You may assume in 
your implementation that higher score = better. You can implement this as a 
Jupyter notebook, or a standalone Python module.    
 
@author: mikeyrobinson@hotmail.com

versions of libraries
---------------------
numpy          1.19.2
pandas         1.1.3

"""

import pandas as pd
import numpy as np

# Notes about implementation------------------------------------
# convert the dictionary to a dataframe for simplicity. 
# Also used numpy for quickly sorting and indexing.

# use proposed "best" ranking to work out the distance to the next set
# e.g. A,B,C is indexed 1,2,3 (100,90,20), however the next metric is 
# ranked B,C,A (0.3,0.2,0.1).  therefore the distance will be calculated
# based on the index shift A,B,C v B,C,A = 2+1+1 = 4
# in this implementation the smaller the distance the more similar the lists
# e.g. if A=0.3, B=0.2, C=0.1 would give 0+0+0 = 0 
# from Generalized Distances between Rankings Ravi Kumar & Vassilvitskii
# http://theory.stanford.edu/~sergei/slides/www10-metrics.pdf - slide 10

def sumSpearmanDistances(scores, proposedRanking):
    
    #insert test to check length of scores & proposed ranking
    if len(scores) != len(proposedRanking):
        print("Warning: the length of scores and proposedRanking are not the same")
    
    df = pd.DataFrame.from_dict(scores)
    df_columns = df.columns
    
    df_1st_col = df.loc[0]
    df_2nd_col = df.loc[1]
    
    # test inputs proposed ranking and correct order of scores
    test_rankcheck = rankcheck(proposedRanking, df_columns, df_1st_col)

    # calculate the distance
    SpearmanDistance = indexCount(df_1st_col, df_2nd_col)
    
    return SpearmanDistance 
    
    
def rankcheck(proposedRanking, df_columns, df_1st_col):
    #function to check that the 'base' proposed ranking is in descending order & 
    #that the conversion from dict to df is in order
    #a = proposedRanking
    #b = df_columns
    
    rank_test = proposedRanking==df_columns
    
    if False in rank_test:
        print("Error: Proposed ranking and scores rank are not the same")
    else:
        print("Pass: Proposed ranking and scores rank are identical")
    
    descend_test = df_1st_col.equals(df_1st_col.sort_values(ascending=False))
    
    if descend_test == False:
        print("Error: Proposed ranking is not in descending order")
    else:
        print("Pass: Proposed ranking is correct")
    
    return print('------Rank check complete------')
        
    
def indexCount(d1, d2):
    #function to convert the indexs' of the two inputs & then calculate the 
    #distance moved per feature
    
    ind1=d1.argsort(axis=0)  #get index
    ind2=d2.argsort(axis=0)  #get index

    #rind1=ind1[::-1] #reverse index
    #rind2=ind2[::-1] #reverse index
    
    rind_abs = np.absolute(ind1-ind2) #calculate the distances moved per feature
    rind_tot = sum(rind_abs)  # total distance = SpearmanDistance
    
    indxSum = rind_tot
    
    return indxSum


    
if __name__ == '__main__':
    #scores = {'A': [100, 0.1], 'B': [90, 0.3], 'C': [20, 0.2]}
    #increased to length 4 to test it works with more than 3 inputs
    # quick test with two different inputs
    s1 = {'A': [100, 0.5], 'B': [90, 0.4], 'C': [20, 0.3], 'D': [10, 0.05]}
    s2 = {'A': [100, 0.1], 'B': [90, 0.3], 'C': [20, 0.2], 'D': [10, 0.6]}
          
    proposedRanking = ['A', 'B', 'C', 'D']
    
    spear_dist1 = sumSpearmanDistances(s1,proposedRanking)
    print('Spearman Distance is:.....', '%0.2f' %spear_dist1, "\n")
    
    spear_dist2 = sumSpearmanDistances(s2,proposedRanking)
    print('Spearman Distance is:.....', '%0.2f' %spear_dist2, "\n")

    print("..............................................................................\n"
          "Results of two tests show that when comparing two different inputs s1 and s2 \n",
          "s1 = ", s1, "\n",
          "s2 = ", s2, "\n",
          "that the Spearmans Distance is: \n",
          "s1 = %0.2f" %spear_dist1, "\n"
          " s2 = %0.2f" %spear_dist2, "\n"
          " s1 is setup to show 2 different scoring metrics that give identical rankings \n",
          "whereby s2 shows that by changing the 2nd score metrics the distance is increased \n",
          "and subsequently the similarity bewteen the two lists is reduced")


#------------------------------------------------------------
__author__ = "Michael Robinson"
__copyright__ = "Copyright 2021, M Robinson"
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "M Robinson"
__status__ = "Prototype"

