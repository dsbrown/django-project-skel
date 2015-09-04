#!/usr/bin/env python 
# -*- coding: utf-8 -*-

###################################################################################
#                 Loads all of the weight tables at one go
#
# assuming they are in the specified directory and named: 
#   ContractWeights.xlsx
#   EngineeringWeights.xlsx
#   PriceWeights.xlsx
#   ScaleWeights.xlsx
#   SecurityWeights.xlsx
#   SpecsWeights.xlsx
#
# Author: David S. Brown
# Last Major Change: 28 August 2015
#
####################################################################################
import argparse
import sys
from subprocess import call
from os.path import isdir
from os import getcwd, system

PATH_TO_PYTHON = "/usr/local/bin/python"
FILES   = ('ContractWeights.xlsx','PriceWeights.xlsx','SecurityWeights.xlsx','EngineeringWeights.xlsx','ScaleWeights.xlsx','SpecsWeights.xlsx',)
TABLES  = ('ContractWeights','PriceWeights','SecurityWeights','EngineeringWeights','ScaleWeights','SpecsWeights',)
parser  = argparse.ArgumentParser(description="Program to make it easier to read all weight tables into SPECS Django server",)
# Template File with fields to replace
parser.add_argument("-d", "--dir", nargs="?", dest="dir", required=True, 
                    help="path to the directory containing the weight spreadsheets")

# Prints help if no arguments
if len(sys.argv)==1:
    parser.print_help()
    sys.exit(1)


args = parser.parse_args()
d = getcwd()
print("CWD: %s",d)
if isdir(args.dir):
    for i, file in enumerate(FILES):
        cmd_line = "%s/../../../manage.py loadweightdata --path %s/%s --table %s"%(d,args.dir,file,TABLES[i])
        print "calling: [%s %s]"%(PATH_TO_PYTHON,cmd_line)
        #call([PATH_TO_PYTHON, cmd_line])
        system(PATH_TO_PYTHON+" "+cmd_line)


