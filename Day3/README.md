# Day 3: User Info Console Application

## Overview

This Python script is a simple console application that lets users input names and ages, store them in lists, and display the collected information. It uses a menu-driven interface for easy interaction.

## Features

- **Input Name(s):** Enter one or more names (separated by spaces) to add to the name list.
- **Input Age(s):** Enter one or more ages (separated by spaces) to add to the age list. The program checks that all ages are numeric.
- **Print User Info:** Display all names and ages entered so far.
- **Exit:** Quit the program.

## How to Use

1. Run the script.
2. Use the menu to select an option:
    - `1`: Input Name(s)
    - `2`: Input Age(s)
    - `3`: Print all entered names and ages
    - `4`: Exit the program

## Example

```plaintext
1. Input Name
2. Input Age
3. Print User Info
4. Exit
Choose an option (1-4): 1
Enter your name: Alice Bob

1. Input Name
2. Input Age
3. Print User Info
4. Exit
Choose an option (1-4): 2
Enter your age: 25 30

1. Input Name
2. Input Age
3. Print User Info
4. Exit
Choose an option (1-4): 3
You entered names: ['Alice', 'Bob']
You entered ages: [25, 30]
```

## Notes

- You can enter multiple names or ages at once, separated by spaces.
- The program will prompt again if you enter invalid ages (non-numeric values).

## License

This project is for educational purposes.
