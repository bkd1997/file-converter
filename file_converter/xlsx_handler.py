from __future__ import division

import xlrd
import chardet
import csv
import os
import glob
import sys
import xlsxwriter
import pyexcel
import json
import pprint
import collections
import warnings
import numpy as np
import pyexcel

warnings.filterwarnings('ignore')

class XlsxHandler(object):
    """ The XlsxHandler class. 
    """

    def __init__(self,file_name):
        """ Initialize the XlsxHandler instance.
            
            :param file_name: The name of the xlsx file that will be converted
            :type file_name: str
            :param dictionary: A blank dictionary that will be used to temporarily store the contents of the xlsx file
            :type dictionary: Dictionary 
        """
        self.file_name = file_name
        self.dictionary = {}
        

    def count_populated_columns(self,row):
        """ A function to return a count of populated columns per row in an array.

        :param row: A row of data containing columns
        :returns: An integer representing the number of populated columns 
        """
        
        return len([c for c in row if len(unicode(c).strip()) > 0])


    def get_stdev(self,rows):
        """ A function to get the standard deviation of the rows. 

        :param rows: This is the number of rows
        :type row: int
        :returns: The standard deviation of how many rows are blank
        :rtype: int
        """
        return np.abs(rows - np.mean(rows)) / np.std(rows)


    def get_first_index_after_title(self,stdevs):
        """ A function to return the index of the first row after the titles.

        :param stdevs: A numpy 1d array of standard deviations
        :type stdevs: int
        :returns: An integer index of the first row after the title sections
        :rtype: int 
        """

        match_list = stdevs < 3
        what = np.argwhere(match_list==True)
        if len(what) > 0:
            return np.argwhere(match_list==True)[0][0]
        else:
            return 0
        

    def _decode_reencode(self, row):
        """ A function to set encoding of the file to be read in utf8 instead of ascii.

        :param rows:
        :type rows: int
        :returns: the rows with the correct encoding 
        """
        if type(row) is list:
            row = [u'{}'.format(c) for c in row]
            return u'{}'.format(u''.join(row).encode('utf8')).encode('utf8')
        else:
            return u'{}'.format(row)

 
    def xlsx_to_dict(self):
        """ A function that converts an xlsx file to a dictionary that contains its data.
            
        :returns: A dictionary that contains the data from the xlsx file
        :rtype: dictionary
        """

        data = []
        sheet = pyexcel.get_sheet(file_name=self.file_name)
        sheet_array = sheet.to_array()
        row_lens = [self.count_populated_columns(r) for r in sheet_array]
        stdev_analysis = self.get_stdev(row_lens)
        first_row = self.get_first_index_after_title(stdev_analysis)
        sheet.delete_rows(range(0, first_row)) # Delete the title rows
        sheet.name_columns_by_row(0) # Give the sheet columns names

        headers = sheet.colnames
        for (idx, row) in enumerate(sheet):
            if idx != 0:
                data.append({k: unicode(v).strip() for (k, v) in zip(headers, row)})
        return dict(headers=headers, data=data)
 
    
    #This method converts a list of dictionaries to an xlsx file
    @classmethod
    def dict_to_xlsx(cls, dictionary, new_file_name):
        """ A function that converts a dictionary into an xlsx.

        :param dictionary: A dictionary that contains headers and its data of a sv file
        :type dictionary: dictionary
        :param new_file_name: The name of the new xlsx file that will be created
        :type: str
        :returns: the new_file_name
        :rtype: str
        """

        a = dictionary
        test=[]
        test.append(a['headers'])
        for i in a['data']:
            test.append([i.get(head, '') for head in a['headers']])
        b = dict(test=test)
        pyexcel.save_book_as(bookdict=b, dest_file_name=new_file_name)
        return new_file_name

       