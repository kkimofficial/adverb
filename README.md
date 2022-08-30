# adverb: pipe operator

DISCLAIMER: THIS WORK IS NOT NECESSARILY A REPRESENTATION OF ANY PAST OR CURRENT EMPLOYER OF MINE

## Introduction

It is a very basic attempt to provide pipe functionality similar to R magrittr library and it's %>% operator

## Installation

Import
```python
>>> from adverb import Adverb
>>> p = Adverb
```

## Overview

- `p(x) >> p(f)` is equalent to `f(x)`

```python
>>> p(-2) >> p(print)
-2
```

- `p(x) >> p(f) >> p(g)` is equalent to `g(f(x))`

```python
>>> p(-2) >> p(abs) >> p(print)
2
```

- `p(x) >> p(f, y)` is equalent to `f(x, y)`

```python
>>> p(-2) >> p(pow, 2) >> p(print)
4
```

- `p(x) >> p(f, y, p)` is equalent to `f(y, x)`

```python
>>> p(-2) >> p(pow, 2, p) >> p(print)
0.25
```


In some cases piped object is not the first argument in the list, so Adverb object can be used as an indicator of argument position
```python
>>> f = Adverb
>>> f(2) >> f(lambda x, y: x ** y, 3, f) >> f(print)
9
```

In order to "unwrap" object the chain must be closed with Adverb object
```python
>>> f = Adverb
>>> result = f(2) >> f(lambda x, y: x ** y, 3, f) >> f
>>> print(result)
9
```

Example with filter and map (where filter and map are standard Python functions) applied to array
```python
>>> f = Adverb
>>> f([1, 2, 3]) >>\
      f(filter, lambda x: x > 1, f) >>\
      f(map, lambda x: x ** 2, f) >>\
      f(list) >>\
      f(print)
[4, 9]
```
The above is equalent in terms of standard function notation
```python
>>> print(list(map(lambda x: x ** 2, filter(lambda x: x > 1, [1, 2, 3]))))
[4, 9]
```
