# magrittp: very basic attempt to provide pipe functionality similar to magrittr library from R

DISCLAIMER: THIS WORK IS NOT NECESSARILY A REPRESENTATION OF ANY PAST OR CURRENT EMPLOYER OF MINE

## Examples

### Import
```python
>>> from magrittp import Magrittp
```

#### Piped object passed as a first argument to a function by default
```python
>>> import operator
>>> f = Magrittp
>>> f(2) >> f(operator.pow, 3) >> f(print)
8
```

#### In some cases piped object is not the first argument in the list
```python
>>> import operator
>>> f = Magrittp
>>> f(2) >> f(operator.pow, 3, f) >> f(print)
9
```
