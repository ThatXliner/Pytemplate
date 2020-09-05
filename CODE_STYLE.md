# Code style

This is a guideline that describes more specific parts of the code style used in this project.

## Python


### Line length
Unlike PEP8, the hard limit for all lines is `90` characters wide. The recommended limit is somewhere between 80 to 88 characters.

It is recommended to set your editor's soft wrap setting at 90 and press <kbd>enter</kbd> or <kbd>return</kbd> at every soft line break. That'll help you wrap 
strings easier. But won't really when you want to expand them in the future for it may not be the most optimal setting. So use your own discretion.

**What happens if I have a long string? How should I split it up?**

If your string is a one liner, you should split it up via implicit string concatenation. For example, from this:

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
Also, **remove trailing whitespace!**

**What about my code?**

If your code is indented so far that it goes past the 90 charcter limit, your code is too complicated. Try to simplify it by using built-in functions, separate it 
using functions, use python's `itertools`, or use recursion instead.
