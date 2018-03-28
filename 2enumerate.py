
# enumerate(sequence, start=0)

##
#Return an enumerate object. sequence must be a sequence, an iterator, or some other object which supports iteration.
##


seasons = ['Spring', 'Summer', 'Fall', 'Winter']
enumerate(seasons)   #<enumerate object at 0x10d137be0>  .    Return an enumerate object
list(enumerate(seasons))  #[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
list(enumerate(seasons), start=1)  #[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
