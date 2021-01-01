# Key Value Data Store

This is a small library that will allow you to create key value databases.

These databases will have 32 character strings as their key and json strings as their value.

# Installation

Just include `freshworks.py` in your program directory and import it in your program.

# How to use

I'll be demonstrating the use of this class through the included [test.py](test.py) program.

Firstly, I am creating 4 valid json objects for use in my functions.

```Python
js1 = '''{
	"1":"A",
	"2":"B",
	"3":"C"
}'''
js2 = '''{
	"4":"D",
	"5":"E",
	"6":"F"
}'''
js3 = '''{
	"7":"G",
	"8":"H",
	"9":"I"
}'''
js4 = '''{
	"10":"J",
	"11":"K",
	"12":"L"
}'''
```

Now, I am importing the class for use in my Test Program.

```Python
from freshworks import Freshworks
```

Now that I have imported the class, I can instantiate it.
```Python
obj = Freshworks()
```

Once I have the object, I can call any of the functions.</br>
I'll start by calling the create() function.

```Python
obj.create("Key1", js1)
obj.create("Key2", js2)
obj.create("Key3", js3)
obj.create("Key4", js4)
```

This will create a .kvds file on my Desktop, which is just a plain text file, and add all the key value pairs in it.

Now, I'll be deleting the `Key3` entry using the delete() function.

```Python
obj.delete("Key3")
```

This will remove the `Key3` entry from the .kvds file created on my desktop.

Lastly, I can see the value of any key through the read() function.

```Python
print(obj.read("Key2"))
```
After all the above operations are performed, this is how the .kvds file will look if opened in a text editor.

```
{
    "Key1": {
        "1": "A",
        "2": "B",
        "3": "C"
    },
    "Key2": {
        "4": "D",
        "5": "E",
        "6": "F"
    },
    "Key4": {
        "10": "J",
        "11": "K",
        "12": "L"
    }
}
```
