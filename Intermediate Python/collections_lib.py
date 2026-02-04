from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

# Counter
a = "aaaaabbbbbbbccccc"
my_counter = Counter(a)
print(my_counter) # returns dictionary of values
print(my_counter.items()) # both keys and values
print(my_counter.keys()) # only keys
print(my_counter.values()) # only values
print(my_counter.most_common(1)) # one most common element; returned as tuple
print(my_counter.most_common(2)) # two most common element
print(my_counter.most_common(2)[0]) # first of two most common element
print(my_counter.most_common(2)[0][0]) # first element of first of two most common element
print(my_counter.elements()) # returns iterables
print(list(my_counter.elements())) # returns iterables

# namedtuple
Point = namedtuple('Point', 'x, y') # or Point = namedtuple('Point', 'x y')
pt = Point(-1, 4)
print(pt)
print(pt.x, pt.y)

# OrderedDict
ordered_d = OrderedDict()
ordered_d['b'] = 2
ordered_d['a'] = 1
ordered_d['d'] = 4
ordered_d['c'] = 3
print(ordered_d)

# defaultdict ---> does cause key_error
d = defaultdict(int)
d['a'] = 1
d['c'] = 3
d['d'] = 4
d['b'] = 2
print(d['a']) # returns 1
print(d['e']) # returns default value = 0 as e is not present in dictionary

# deque
deq = deque()
deq.append(1)
deq.append(2)
deq.append(3)
print(deq)
deq.appendleft(4)
deq.appendleft(5)
deq.appendleft(6)
print(deq)
deq.remove(1)
print(deq)
deq.pop()
print(deq)
deq.extend([11, 12, 13])
print(deq)
deq.extendleft([21, 22, 23])
print(deq)
deq.rotate(1) # rotate all elements to right by 1
print(deq)
deq.rotate(2) # rotate all elements to right by 2
print(deq)
deq.rotate(-2) # rotate all elements to left by 2
print(deq)
deq.clear()
print(deq)