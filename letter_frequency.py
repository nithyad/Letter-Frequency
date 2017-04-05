#
# This file looks at the letter frequencies using the Project Gutenberg data. Functions includes weighted first letter counts, frequency of the last letter, and the 
# frequency of a letter at a given index.
# 

import csv

#
# readcsv is a starting point - it returns the rows from a standard csv file...
#
def readcsv( csv_file_name ):
    """ readcsv takes as
         + input:  csv_file_name, the name of a csv file
        and returns
         + output: a list of lists, each inner list is one row of the csv
           all data items are strings; empty cells are empty strings
    """
    try:
        csvfile = open( csv_file_name, newline='' )  # open for reading
        csvrows = csv.reader( csvfile )              # creates a csvrows object

        all_rows = []                               # we need to read the csv file
        for row in csvrows:                         # into our own Python data structure
            all_rows.append( row )                  # adds only the word to our list

        del csvrows                                  # acknowledge csvrows is gone!
        csvfile.close()                              # and close the file
        return all_rows                              # return the list of lists

    except FileNotFoundError as e:
        print("File not found: ", e)
        return []



#
# write_to_csv shows how to write that format from a list of rows...
#  + try   write_to_csv( [['a', 1 ], ['b', 2]], "smallfile.csv" )
#
def write_to_csv( list_of_rows, filename ):
    """ readcsv takes as
         + input:  csv_file_name, the name of a csv file
        and returns
         + output: a list of lists, each inner list is one row of the csv
           all data items are strings; empty cells are empty strings
        How to run: give in a list, and then the excel document to put it in
    """
    try:
        csvfile = open( filename, "w", newline='' )
        filewriter = csv.writer( csvfile, delimiter=",")
        for row in list_of_rows:
            filewriter.writerow( row )
        csvfile.close()

    except:
        print("File", filename, "could not be opened for writing...")


#
# csv_to_html_table_starter
#
#   Shows off how to create an html-formatted string
#   Some newlines are added for human-readability...
#
def csv_to_html_table_starter( csvfilename ):
    """ csv_to_html_table_starter
           + an example of a function that returns an html-formatted string
        Run with 
           + result = csv_to_html_table_starter( "example_chars.csv" )
        Then run 
           + print(result)
        to see the string in a form easy to copy-and-paste...
        how to run: give an excel document, and this method will print the items in HTML
        Used this to make the html document letter_frequencies.html
    """
    LoR = readcsv( csvfilename ) 
    # probably should use the readcsv function, above!
    html_string = '<table>'    # start with the table tag

    # a lot of loops (2)
    # from list_of_rows !
    for Row in LoR:
        html_string += '<tr>'
        for Column in Row:
            html_string += '<td>'
            html_string += Column
            html_string += '</td>'
        html_string += '</tr>'
    html_string += '</table>'
    return html_string


from collections import *
#
# unweighted counting of first letters!
#
def UWcount():
    """ returns a dictionary (defaultdict) of
        unweighted first-letter counts from 
        the file wds.csv
    """
    LoR = readcsv( "wds.csv" )  # List of rows
    #print("LoR is", LoR)
    counts = defaultdict(int)
    for Row in LoR:
        word = str(Row[0])      # the word is at index 0
        num  = float(Row[1])    # its num occurrences is at index 1
        first_letter = word[0]  # the first letter of the word
        counts[first_letter] += 1   # add one to that letter's counts
    # done with for loop
    return counts

def Wcount(function):
    """ returns a dictionary (defaultdict) of
        the weighted first-letter counts from 
        the file wds.csv
        uses relative frequency
        How to Use: input a function and it will gives the relative frequency of the inputs 
    """
    givenDict = function
    count = 0
    for i in givenDict:
        count += givenDict[i]

    for c in givenDict:
        givenDict[c] = (givenDict[c])/count
    return givenDict

def lasLetter():
    """ returns the relative frequency of the last
        -letter counts from the file wds.csv
        How to use: Just run method- looks at the last letter of the given file
        will print dictionary and print to frequencies
    """
    LoR = readcsv( "wds.csv" )  # List of rows
    #print("LoR is", LoR)
    counts = defaultdict(int)
    for Row in LoR:
        word = str(Row[0])      # the word is at index 0
        num  = float(Row[1])    # its num occurrences is at index 1
        first_letter = word[len(word)-1]  # the first letter of the word
        counts[first_letter] += 1   # add one to that letter's counts
    # done with for loop
    
    new_dict = (Wcount(counts))
    print(new_dict)
    new_list = []
    for i in new_dict:
        new_list += [[i, new_dict[i]]]
    
    return(write_to_csv( new_list, "frequencies.csv" ))

    
def mostfrequency(letter):
    """ returns the relative frequency of the
    how often the letter appears in
    each index.
    How to run: Give a letter, in string format, to see the number of times it appears in each index
    Will print out dictionary as well as put it in frequencies.csv
    """
    LoR = readcsv( "wds.csv" )  # List of rows
    #print("LoR is", LoR)
    counts = defaultdict(int)
    for Row in LoR:
        word = str(Row[0])      # the word is at index 0
        num  = float(Row[1])    # its num occurrences is at index 1
        for i in range(len(word)):
            if str(word[i]) == letter:
                counts[i] += 1
    
    new_dict = (Wcount(counts))
    print(new_dict)
    new_list = []
    for i in new_dict:
        new_list += [[i, new_dict[i]]]
    
    return(write_to_csv( new_list, "frequencies.csv" ))


""""
Examples to run individually in order

#given function, will return the unweighted counting of the first letters
UWcount()

#will return the weighted counting (aka relative frequency) of the first letters
Wcount(UWcount())

#will return the weighted counting of the last letters and will post to frequencies.csv
lasLetter()

#will return the weighted counting of the index's t appears in and will post to frequencies.csv
#mostfrequency('t')

#will take in frequencies.csv which will now contain the index's t appears in and will create an html tag for it
csv_to_html_table_starter('frequencies.csv')
""""