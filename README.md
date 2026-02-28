## Flashcards
A terminal based, cli flashcard maker built with python.
The minimalism brought by the terminal provides a distraction free experience with no ai, no purchases and no flashy animations.
This is an open soruce project that you are free to download, change and customise as its made mianly to practice and for personal use.
Go use it to its fullest!
Currently in very early development, more to come.


## Installation

```bash
# Install with pipx (recommended)
pipx install git+https://github.com/demtellme/flashcards.git

# Or with pip
pip install --user git+https://github.com/demtellme/flashcards.git
```

## Uninstall Command
```bash
pipx uninstall falshcards
```
## How to use
```bash
#arguments only if necessary
fcards <command> <argument one> <argument two>
```
 ## Commands:
     i - initialise the flashcard folder
    v <folder> - view all items created in a folder, if <folder> isnt specified it will show items in the base directory
    ms <name> <folder> - makes a set of flashcards, if folder is specified it will add the set to the folder, if the folder dosent exist it will make it
    rm <name> - removes specified item
    ls <name> <folder> - open a set to learn, you get asked to define the terms in your flashcards, if folder not specified it defalts to default directory
    os <name> <folder> - opens sepecific set to practice, just normal flipping of flashcards
    cf - displays the current working folder

Made By Alex G
