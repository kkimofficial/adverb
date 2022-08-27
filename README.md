# magrittp: very basic attempt to provide pipe functionality similar to magrittr library from R

DISCLAIMER: THIS WORK IS NOT NECESSARILY A REPRESENTATION OF ANY PAST OR CURRENT EMPLOYER OF MINE

## 1) Examples

###
```python
import operator
from magrittp import Magrittp

f = Magrittp
f(2) >> f(operator.pow, f, 3) >> f(print)
```
