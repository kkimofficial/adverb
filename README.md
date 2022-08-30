# adverb: pipe operator

DISCLAIMER: THIS WORK IS NOT NECESSARILY A REPRESENTATION OF ANY PAST OR CURRENT EMPLOYER OF MINE

## Introduction

It is a very basic attempt to provide pipe functionality similar to R magrittr library and it's %>% operator. It might improve code readability in cases when there are a lot of nested brackets.

## Installation

Import
```python
>>> from adverb import Adverb
>>> p = Adverb
```

## Overview

- `p(x) >> p(f)` is equivalent to `f(x)`. Piped object implicitly passed to a function

```python
>>> p(-2) >> p(print) # print(-2)
-2
```

- `p(x) >> p(f) >> p(g)` is equivalent to `g(f(x))`. Sequences can be of any length

```python
>>> p(-2) >> p(abs) >> p(print) # print(abs(-2))
2
```

- `p(x) >> p(f, y)` is equivalent to `f(x, y)`. By default piped object passed as a first argument to the function despite the number of arguments

```python
>>> p(-2) >> p(pow, 2) >> p(print) # print(pow(-2, 2))
4
```

- `p(x) >> p(f, y, p)` is equivalent to `f(y, x)`. When piped object needs to be passed explicitly (for example, when it needs to be somewhere other than the first argument in the list), then Adverb class objet can be used as a placeholder

```python
>>> p(-2) >> p(pow, 2, p) >> p(print) # print(pow(2, -2))
0.25
```

- In order to "unwrap" object and get the final value the chain must be closed with Adverb class object
```python
>>> result = p(-2) >> p(pow, 2) >> p
>>> print(result)
4
```

- Pipes can be combined with + operator. Effectively it is a way of creating complex lambda functions
```python
>>> sequence = p(pow, 2) + p(print)
>>> p(-2) >> sequence
4
```

- More complex example with filter and map (where filter and map are standard Python functions) applied to array
```python
>>> sequence = p(filter, lambda x: x > 1, p) + p(map, lambda x: x ** 2, p) + p(list) + p(print)
>>> p([1, 2, 3]) >> sequence
[4, 9]
```
