class FileCollectionIterator:
    """
    To iterate over FileCollection
    """
    
    def __init__(self, fc):
        self._fc = fc
        self._index = 0
        
    def __next__(self):
        if self._index  < (len(self._fc.content)):
            retval = self._fc.content[self._index]
            self._index += 1
            return retval
        else:
            raise StopIteration