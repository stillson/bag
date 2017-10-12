# bag
bag class for python. Inspired by the smalltalk class of the same name. 
It works by holding any number of elements, and returning them in a random
order. It works like the proverbial bag with a white stone and a black stone
when discussing probability. You add elements in any order, then retrieve
them using pop, getting a random element which is removed from the bag.

# usage

```python
import bag

b = bag.Bag(1, 2, 3, 'yellow', 1)
b.add(2)
#-> bag.Bag(1, 2, 3, 'yellow', 1, 2)

b.add({1,2,3})
#-> bag.Bag(1, 2, 3, 'yellow', 1, 2, {1, 2, 3})

len(b)
#-> 7

out = ''

for i in b:
    out += str(i)

out
#-> '22yellow{1, 2, 3}311'

len(b)
#-> 0

b.add(2)
b.add(1)

len(b)
#-> 2

b.pop()
#-> 1

b.pop()
#-> 2
```

# methods

`__init__(*args)`

bag.Bag() generates a new bag. Any arguments will be the initial
elements of the bag.

---

`pop()`

Removes and returns a random element from the bag.

---

`add()`

Add an element to the bag.

---

`+`

Concatenates 2 bags. Creates a new bag.

```python
a = bag.Bag(1)
b = bag.Bag(2)

a + b
#-> bag.Bag(1, 2)
```
---

`in`

Tests if an element is in the bag.

```python
a = bag.Bag(2)

1 in a
#-> False

2 in a
#-> True
```

---

`repr`

Prints a string representation of a bag. Safe for recursive values.

```python
a = bag.Bag()

repr(a)
#-> bag.Bag()

a.add(a)
#-> bag.Bag(...)
```
