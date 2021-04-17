#   FileCollection.py
#   version 1

"""
Represent a FileCollection as used in fspow
### Attributes:
    * root : FSObject
	* The directory containing the collection.

### Methods
#### Instantiator — FileCollection(root : string) : FileCollection
	* 	Note: this differs from the suggested instantiator Root.
		* Could offer Root instantiator too if wanted.
	* Creates a collection of paths of all files and directories found in the hierarchy of the root.

#### list(options) : string 
* Return list the paths of the objects in the collection
* Formerly known as ‘print’, but recall, we cannot do overloading in our context
* What about /what/ to list for each object?  Could be an enhancement
* options:
	* Only one for now
	* `dirs(“include”)`

#### apply(filter : Selector) : FileCollection
* Creates a new FileCollection object with collection containing only those FSObjects that meet the criteria in filter.
* In other words, method should be non-destructive.

#### copy(target : string) : void
* Copy all files (not directories) in the collection to the directory specified by /target/
* If the file already exists in /target/, rename it to avoid clash

#### move(target : string) : void
* Move all files (not directories) in the collection to the directory specified by /target/
* If the file already exists in /target/, rename it to avoid clash
* In v2

#### remove([options]) : void
* Delete all FSObjects in the collection
* Options:
	* rememptydirs=(true|false)
		* if true then remove directories left empty after files have been deleted, else leave them be
		* default : false
* v2

#### exec(command : string) : void
* Execute the system command specified by /string/ on every file (not directories) in the collection
* v2
"""

from pathlib import Path
import sys
from .Selector import *
from .FileCollectionIterator import *

class FileCollection:

    # root directory of file collection defaults to current directory
    root = "."
    content = []

    def __init__(self, rootPath:str="."):
        # print("FileCollection instantiated with rootPath =", rootPath)
        """
        if directory specified by rootPath exists
            set root to rootPath
        else
            warning and set to current or parent of rootPath
        """
        potentialRoot = Path(rootPath)
        if potentialRoot.exists():
            if  potentialRoot.is_dir():
                # happy
                self.root = rootPath
            else:
                # not a directory
                # set to parent if it's a path, else set to current
                if potentialRoot.parent.is_dir():
                    # parent is a dir so warn and set to that
                    self.root = potentialRoot.parent
                    sys.stderr.write("Warning: " + rootPath + " not a directory - setting file collection root to its parent " + str(self.root) + "\n")
                else: 
                    # can't establish
                    sys.stderr.write("Warning: " + rootPath + " not a directory and cannot establish parent - setting file collection root to current directory\n")
                    # but it's already done, so pass
        else:
            # potential root doesn't exist
            sys.stderr.write("Warning: " + rootPath + " not found - setting file collection root to current directory\n")          
            # and pass  
        # populate content
        self.content = []
        for path in Path(self.root).rglob("*"):
            if path.is_file():
                self.content.append(path)
#         self.content = [p for p in Path(self.root).rglob("*")]
        
    def length(self):
        return len(self.content)
    
    def __getitem__(self, index):
        """
        handle square brackets as if FileCollection object is a list
        """
        if index < len(self.content):
            return self.content[index]
        else:
            return None
        
    def __iter__(self):
        """
        permit iteration over file collection
        """
        return FileCollectionIterator(self)
        
    def list(self, options=None) -> str:
        """
        controlled by options (TODO),
        list everything under the root, returning as string, because
        I like doing it that way
        """
        retval = ""
        if options == None:
            # list everything
#             for oneEntry in Path(self.root).rglob("*"):
            for oneEntry in self.content:
                fname = str(oneEntry)
                retval += fname + "\n"                                       
        else:
            #TODO
            pass
        return retval
        

    def getRoot(self):
        return self.root    

    def apply(self, filter:Selector=None):
#         print("FileCollection.apply() called with filter =", filter)
        """
        for each item in self.content
            if it fails the test specified by filter, remove it
        """
        numberOfItems = len(self.content)
        i = 0;
        while i < numberOfItems:
            if filter.testPath(self.content[i]):
                i += 1
            else:
                self.content.pop(i)
                numberOfItems -= 1

    def copy(self, target:str=""):
        #TODO
        pass

    # v2
    # move, remove, exec
