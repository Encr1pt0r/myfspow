#   FSObject.py
#   version 1

"""
This might end up being redundant - may get away with using pathlib alone
Required for [[Language draft 1 use cases/Changing file attributes]]
* Represents a file or directory.

### Attributes
* parent : FSObject:  the FSObject that is the parent of this; null if this is the root directory (not that this should happen)
* path : string : the path of this object, relative to parent
* fstype : string : whether this is a “directory” or a “file”; in future, might be relevant whether symlink, but keeping it simple for now (hence just a string)
* name : the name of the FSObject

### Methods
#### rename(newName : string)
* Rename the FSObject with newName
* If another FSObject called newName already exists, rename it to avoid clash
* We don't fuss about with "file extensions" - let's be OS agnostic
"""

from pathlib import Path

class FSObject:

    # convention for avoiding clashes:
    """
    Would it be right to use the convention ' Copy 1', ' Copy 2', etc?
    I would feel uncomfortable doing this, as (a) we're not copying,
    and (b) it looks too much like what the OS would do.
    Oh, and (c) I hate having spaces stuck in file names unless I specifically
    say so.
    Can't use 'dup' for duplicate, becaue that's too much like 'copy'.
    Oh and btw, let's not use caps, because they're a pain to have to type.
    I know: just add some number or afterwards.
    I'm really tempted to just go with uuid, but people might hate me for it...     
    """

    def __init__(self, parent=None, path:str="", fstype:str="", name:str=""):
        self.parent = parent
        self.path = path
        self.fstype = fstype
        self.name = name

#         print("FSObject intantiated:", self)
        

    def rename(self, newName:str=""):
        #TODO
        """
            strip newName of illegal file or dir name characters
            trim it
            if we have anything left
                if an object in the file system with this name already exists
                    do something or other to make the new name unique
                else {no name clash}
                    ok to proceed = true
                if ok to proceed, do the renaming
            else {nothing left}
                warning >stderr
                noop
        """
        pass

    def __str__(self):
        if self.parent == None:
            parentString = "(none)"
        else:
            parentString = "another FSObject"
        return "parent={}, path={}, fstype={}, name={}".format(parentString, self.path, self.fstype, self.name)