"""
-------------------------------------------------------------------------------
Name:        PythonApplication1.py
Purpose:     Sandbox development

Author:      Toni Fairbanks

Created:     2/9/2016
Copyright:   (c) Patrick Engineering 2015
-------------------------------------------------------------------------------
"""

import arcpy

import collections

def rows_as_dicts(cursor):
    """ returns rows as dicts (does not maintain field order) """
    colnames = cursor.fields
    for row in cursor:
        yield dict(zip(colnames, row))


def rows_as_ordered_dicts(cursor):
    """ returns rows as collections.OrderedDict """
    colnames = cursor.fields
    for row in cursor:
        yield collections.OrderedDict(zip(colnames, row))