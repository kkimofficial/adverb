# magrittp: pipe operator

DISCLAIMER: THIS WORK IS NOT NECESSARILY A REPRESENTATION OF ANY PAST OR CURRENT EMPLOYER OF MINE

## Introduction

It is a very basic attempt to provide pipe functionality similar to R magrittr library and it's %>% operator

## Overview

## Examples

Import
```python
>>> from magrittp import Magrittp
```

Piped object passed as a first argument to a function by default
```python
>>> f = Magrittp
>>> f(2) >> f(lambda x, y: x ** y, 3) >> f(print)
8
```

In some cases piped object is not the first argument in the list, so Magrittp object can be used as an indicator of argument position
```python
>>> f = Magrittp
>>> f(2) >> f(lambda x, y: x ** y, 3, f) >> f(print)
9
```
