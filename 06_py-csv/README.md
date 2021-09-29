# K06 Summative Assessment

Team name: Hi-C

Team members: Andy Lin, Josephine Lee, Yaying Liang

- In terms of file I/O, we used the open function with the file name and file viewing mode as "r" so that we can tell Python that we are just reading the file, no editing involved.
- A dictionary is good for storing key-value pairs (think of it as a list of variables that you can individually assign a value to, and the list is assigned to another variable).
- Someone can initalize a dictionary by creating a variable that is assigned to a "{}" value, which may or may not contain keys (in quotes) that have a value assigned to them.
- You can look into a specific variable within a list by using the using the brackets with the title of the dictionary key you want to look into. (eg dictionary['key'])
- You can also get all the keys of a dictionary by using dictionary.keys() function, and get all the values by using the dictionary.values() function.
- A list is good for storing data that has little correspondence with each other. You can initalize a list by assigning a [] value (potentially with any other values inside) to a variable.
- You can append to a list by using the list.append() function, get list length with the len(list) function.
- Markdown stuff:
    - Start a line with "#" in order to get a large header. A line that starts with multiple "#"'s will result in a header that is smaller in size than a header that is made from one leading "#".
    - You can make a list in Markdown by using "-" in the beginning of a line, followed by a space.
    - If you need to make a newline in Markdown, don't forget to make one new line between lines.
    - Markdown is important as a documentation tool. You can make the reader understand more about the program, its purpose, and knowing more about what the code does (if someone is bad at reading code). It can also tell the user how to use the source code (building it, how to do PRs, etc).
    - You can learn how to use Markdown by looking into Markdown files and experimenting with using the different syntaxes of Markdown. You can also use a tutorial.
- Weighted randomized selection
    - We used the random.choices function, which takes in a list of values to pick a value to return, a list/sequence of floats to see which list values are weighted more set to the variable "weight", and the quanity of values to return set to a variable "k".