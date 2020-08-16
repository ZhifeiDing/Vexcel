#!/usr/bin/env python3
##############################################################
## Filename : Vexcel.py
## Author   : zhifei ding
## Description :
##
##############################################################

# -*- coding : utf-8 -*-

import re
import os
import getpass
import time
import argparse
import sys
import json
import subprocess
from collections import defaultdict
import shutil
import xlrd

user = getpass.getuser()
timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def parse_args():
    parser = argparse.ArgumentParser(description='Vexcel : verilog integration tool', 
        epilog='a powerful verilog integration tool combined with excel and python')
    parser.add_argument('-e','--extract', dest='extract_port', required=False, 
        type=str, default=False, 
        help='extract ports from verilog to excel')
    parser.add_argument('-i','--input', dest='input_excel', required=True, 
        type=str, default='multi_ibex.xlsx', 
        help='specify the input excel filename')
    return parser.parse_args()
    

def valid_args(args):
    pass

def parse_excel(args):

    workbook = xlrd.open_workbook(args.input_excel)

    data_sheets = workbook.sheet_names()
    for sheet in data_sheets:
        table = workbook.sheet_by_name(sheet)
        nrows = table.nrows
        ncols = table.ncols
        row_content = table.row_values(0)

def extract_port(args):

def run():
    args = parse_args()
    valid_args(args)

    if args.extract_port is True:
        extract_port(args)

if __name__ == '__main__':
    run()