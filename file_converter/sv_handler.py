import xlrd
import unicodecsv as csv
import os
import glob
import sys
import xlsxwriter
import pyexcel
import json

from collections import OrderedDict


class SVHandler(object):
    """ The SVHandler class.

    """
    def __init__(self,file_name):
        """ Initilize the SVHandler instance.

        :param file_name: The name of the sv file
        :type file_name: str
        :param dictionary: A blank dictionary that will be used later
        :type dictionary: dictionary
        """

        self.file_name = file_name
        self.dictionary = {}


    def sv_to_dict(self):
        """ A function that converts the sv file to a dictionary that contains the data.

        :returns: A dictionary with the headers and data from the sv file
        :rtype: dictionary
        """

        with open(self.file_name, 'r') as fp:
            headers = None
            for row in csv.reader(fp):
                if headers:
                    break
                headers = row
            data = list(csv.DictReader(fp, fieldnames=headers))
        return dict(headers=headers, data=data)


    @classmethod
    def dict_to_sv(cls, dictionary, new_file_name, delimiter):
        """ A function that will convert a dictionary with data to a sv file.

        :param dictionary: A dictionary that contains data from a sv or xlsx file that will be converted
        :type dictionary: dictionary
        :param new_file_name: The name of the new sv file being created
        :type new_file_name: str
        :param delimiter: The delimiter that the new sv file will be seperated by
        :type delimiter: str
        """

       if len(dictionary) > 0:
        fieldnames = dictionary['headers']
        keys = dictionary['data']
        with open(new_file_name, 'w') as fp:
            writer = csv.DictWriter(fp, fieldnames, delimiter=delimiter, encoding='utf-8')
            writer.writeheader()
            writer.writerows(keys)
        return new_file_name





