#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2016 Felipe Gallego. All rights reserved.
#
# This is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Scripts for intelligent agents.
"""
import random

# ---------------------------------- Table driven agent.

TABLE_TDA = dict()
N_TDA = 4

def init_table_driven_agent():
    # The table is just a multiplication table.
    for i in range(11):
        TABLE_TDA.update( { i : i*N_TDA } )
    
    random.seed(1) 
    
    return random.sample(xrange(1, MAX_VAL_SRA + 1), 5)     

def table_driven_agent(perceptions):
    
    for p in perceptions:
        print "%s * %s = %s" % (str(p), str(N_TDA), str(TABLE_TDA[p]))

# ---------------------------------- Simple reflex agent.

# States for the simple reflex agent.
MAX_VAL_SRA = 10
ACTIONS_SRA = [ "A", "B", "C"]
LEVELS_SRA = [ 2, 5, 7 ]
RULES_SRA = [ [True, False, False], [True, False, True], [False, True, True] ]

def init_simple_reflex_agent():
    
    random.seed(1)
    
    return [ random.sample(xrange(1, 11), 3) for _ in range(10) ]    

def interpret_input(perception):
    
    state = []
    
    for i in range(len(perception)):
        state.append(perception[i] > LEVELS_SRA[i])
    
    return state

def rule_match(state, rules):
    
    action_taken = False
    
    for i in range(len(rules)):
        if rules[i] == state:
            print "Action %s" % ACTIONS_SRA[i]
            action_taken = True
            
    if not action_taken:
        print "No action taken."

def simple_reflex_agent(perceptions):

    state = interpret_input(perceptions)
        
    rule_match(state, RULES_SRA)
        
# ---------------------------------- Model based reflex agent.  

def init_model_based_reflex_agent():
    
    pass

def model_based_reflex_agent(perceptions):
    
    pass

# ---------------------------------- Launch the agents.      
            
def launch():
    
    print "----------- Table driven agent"
    
    perceptions = init_table_driven_agent()
    
    table_driven_agent(perceptions)
        
    print "----------- Simple reflex agent"
    
    perceptions = init_simple_reflex_agent()
    
    for p in perceptions:
        print "-> Perception: %s" % str(p)
        simple_reflex_agent(p)    