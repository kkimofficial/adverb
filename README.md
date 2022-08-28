# adverb: pipe operator

DISCLAIMER: THIS WORK IS NOT NECESSARILY A REPRESENTATION OF ANY PAST OR CURRENT EMPLOYER OF MINE

## Introduction

It is a very basic attempt to provide pipe functionality similar to R magrittr library and it's %>% operator

## Overview

## Examples

Import
```python
>>> from adverb import Adverb
```

Piped object passed as a first argument to a function by default
```python
>>> f = Adverb
>>> f(2) >> f(lambda x, y: x ** y, 3) >> f(print)
8
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
