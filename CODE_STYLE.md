# Code style

This is a guideline that describes more specific parts of the code style used in this project.

## Python


### Line length
Unlike [PEP8](https://www.python.org/dev/peps/pep-0008/), the hard limit for all lines is `90` characters wide. The recommended limit is somewhere between 80 to 88 characters.

It is recommended to set your editor's soft wrap setting at 90 and press <kbd>enter</kbd> or <kbd>return</kbd> at every soft line break. That'll help you wrap strings easier. But it won't really help when you plan to expand them (e.g. docstrings) in the future for it may not be the most optimal setting. So use your own discretion.

**What happens if I have a _very_ long string? How should I split it up?**

If your string is a one liner, meaning it won't have any newlines, you should split it up via **implicit string concatenation**. For example, change this:

```python
print("Some super-duper long string that will go over the recommended line limit of 80 to 88 characters. This is definitely going to go past the 90 character hard limit.")
```

to this:

```python
print("Some super-duper long string that will go over the recommended line limit of 80 "
"to 88 characters. This is definitely going to go past the 90 character hard limit.")
```
And if you have f-strings, you can just put an `f` in front of every separate string. It'll concatenate normally, without any errors.

**What about comments?**

Comments should be wrapped around as well. Turn something like this:
```python
# (90 characters is the width of this comment)============================================
# NOTE: Wrap this comment so that it won't go past the 90 character hard limit. So yeah, this is a long comment
```
into this:
```python
# (90 characters is the width of this comment)============================================
# NOTE: Wrap this comment so that it won't go past the 90 character hard limit. So yeah,
# this is a long comment
```
Also, **remove trailing whitespace!** They really suck.

**What about my code?**

If your code goes past the 90 character limit, your code is too complicated.

Try to simplify it by using built-in functions, separate it
into functions, use python's `itertools`, or use recursion instead.

Python is for readability. But speaking about performance....

### Performance and preferred styles

Ok, so I know that you shouldn't be doing pre-mature optimizations in python. But the thing is, what if **it's code style**? It is.

If you require a specific type of object as one of your parameters (when defining a function), the recommended approach is to use type hints. This will reduce 
unnecessary function calls and will greatly improve readability, code maintainability, and user experience (especially if you use a linter such as [MyPy](http://mypy-lang.org/)). 

What about `try`/`except`s? And `if`/`elif`/`else` statements?

The answer is, it depends. It depends on the type of situation.

As described in the [python documentation](https://docs.python.org/3/faq/design.html#how-fast-are-exceptions):

>A try/except block is extremely efficient if no exceptions are raised. Actually catching an exception is expensive. In versions of Python prior to 2.0 it was common to use this idiom:
```
try:
    value = mydict[key]
except KeyError:
    mydict[key] = getvalue(key)
    value = mydict[key]
```
>This only made sense when you expected the dict to have the key almost all the time. If that wasn’t the case, you coded it like this:
```
if key in mydict:
    value = mydict[key]
else:
    value = mydict[key] = getvalue(key)
```
>For this specific case, you could also use `value = dict.setdefault(key, getvalue(key))`, but only if the `getvalue()` call is cheap enough because it is evaluated in all cases.
