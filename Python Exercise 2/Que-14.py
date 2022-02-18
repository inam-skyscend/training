# Create a text document using the justification methods.


x="hello everyone"
y="Python string method rjust() returns the string right justified in a string of length width. Padding is done using the specified fillchar (default is a space). The original string is returned if width is less than len(s)."
z="This function center aligns the string according to the width specified and fills remaining space of line with blank space if ‘ fillchr ‘ argument is not passed."
print(x.ljust(24,"-"))
print(y.rjust(250))
print(z.center(200))

