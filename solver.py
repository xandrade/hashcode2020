# -*- coding: utf-8 -*-
"""#HashCode2020-GUtech.ipynb

Desert Coding - Oman @ 2020

Original file is located at
    https://colab.research.google.com/drive/1NNbJnre146ZrdqKVMSH0_QoPaBmiVcy5
"""

import numpy as np
from operator import itemgetter
import pdb

file_names = ['f_libraries_of_the_world',
               'e_so_many_books',
               'd_tough_choices',
               'c_incunabula',
               'b_read_on',
               'a_example']

def add_to_lib(l3, l4):
  global libraries
  lib =  {'library_id': len(libraries),
          'books_ids': l4, 
          'number_books': l3[0],
          'sigup_process_days': l3[1],
          'maximum_allowed_shipment': l3[2],}
  libraries.append(lib)


def add_sum_scores():
  global libraries
  for library_id, library in enumerate(libraries):
    #print(library.get('books_ids'))
    sum_scores = 0
    books_scores_ = []
    for book_id in library.get('books_ids'):
      #print(books_scores[book_id])
      sum_scores = sum_scores + books_scores[book_id]
      books_scores_.append(books_scores[book_id])
    else:
      #print(sum_scores)
      libraries[library_id]['sum_scores'] = sum_scores
      libraries[library_id]['books_scores'] = books_scores_

def process_this():

  processed_books = []

  result_library_summary = []
  result_library_book_ids = []

  remained_days = maximum_days_scanning
  acc_days = 0

  for library in libraries:

    library_id = library['library_id']
    
    #pdb.set_trace()
    if remained_days > 0:

      remained_days = remained_days - library.get('sigup_process_days')
      numbers_books_to_scan = library.get('number_books') // library.get('maximum_allowed_shipment')
      #print(library.get('number_books'), library.get('maximum_allowed_shipment'), remained_days)
      #print(numbers_books_to_scan)
      processed_books_lib_acc = 0
      processed_books_lib = []
      books_ids = library.get('books_ids')
      books_scores = library.get('books_scores')
      ind = sorted(np.lexsort((books_scores, books_ids)))
      for score, id in [(books_scores[i],books_ids[i]) for i in ind]:
        #print(score, id)
        if numbers_books_to_scan > 0:
          if (processed_books_lib_acc / numbers_books_to_scan) < remained_days:
            if id in processed_books:
              pass
            else:
              processed_books.append(id) # <- need id
              processed_books_lib_acc = processed_books_lib_acc + 1
              processed_books_lib.append(id) # <- need id
      else:
        #print(processed_books)
        #print(processed_books_lib)

        
        if len(processed_books_lib) > 0:
          result_library_summary.append([library_id, len(processed_books_lib)])
          result_library_book_ids.append(processed_books_lib)


    else:
      break

  return library_id, result_library_summary, result_library_book_ids

for file_name in file_names:

  print(file_name)

  with open('./content/extended_round/' + file_name + '.txt', 'r') as f:
    line = f.readline()
    l1 = line.replace('\n','').split(' ')
    l1 = list(map(int, l1))
    #print(l1)
    
    line = f.readline()
    l2 = line.replace('\n','').split(' ')

    l2 = list(map(int, l2))
    #print(l2)

    number_books = l1[0]
    number_libraries = l1[1]
    maximum_days_scanning = l1[2]
    books_scores = l2

    #ToDo: read file by 2 lines

    libraries = []

    while True:

      line = f.readline()
      if not line or line == '\n':
        break
      l3 = line.replace('\n','').split(' ')
      l3 = list(map(int, l3))
      #print(l3)
      
      line = f.readline()
      l4 = line.replace('\n','').split(' ')
      l4 = list(map(int, l4))
      #print(l4)

      add_to_lib(l3, l4)

    add_sum_scores()
    libraries = sorted(libraries, key=itemgetter('sum_scores', 'maximum_allowed_shipment', 'sigup_process_days'), reverse=False)
    total_libraries, result_library_summary, result_library_book_ids = process_this()

    with open('./content/extended_round/' + file_name + '.out', 'w') as fo:
          fo.write(f'{len(result_library_summary)}\n')

    #print('number of libraries processed:', len(result_library_summary))
    for library_summary, library_book_ids in zip(result_library_summary, result_library_book_ids):
      #print(results)
      with open('./content/extended_round/' + file_name + '.out', 'a') as fo:      
        for item in library_summary:
          fo.write(f'{item} ')
        else:
          fo.write('\n')
        for item in library_book_ids:
          fo.write(f'{item} ')
        else:
          fo.write('\n')