import unittest
import pickle
"""
This class creates a new object, a list.
Input: - 
Output: list
"""
class Repository:
    def __init__(self):
        self._list = []
        
    """
    This function adds a new object to the list.
    Input: object
    Output: -
    """    
        
    def addObject(self,object):
        self._list.append(object)
        
    def __len__(self):
        return len(self._list)
    
    def __str__(self):
        s = ""
        print(type(self._list))
        for i in range(len(self._list)):
            s += str(self._list[i])
        return s
    
    """
    This function removes from the list the object from the position given by the index.
    Input: index - unsigned integer
    Output: -
    """
    def removeObject(self,index):
        self._list.pop(index)
        
    """
    This functions returnes the object from the position given by the index.
    Input: index - unsigned integer
    Output: object
    """
    def getObject(self,index):
        return self._list[index]
    
    def getAll(self):
        return self._list
    
    def __iter__(self):
        self._index = -1
        return self
    
    def __next__(self):
        if self._index < len(self._list):
            result = 1 + self._index
            self._index += 1
            return result
        else:
            raise StopIteration
        
class PickleRepository(Repository):
    def __init__(self,fileName):
        Repository.__init__(self)
        self._fileName = fileName
        self._loadFile()
    
    
        
    def addObject(self, object):
        Repository.addObject(self, object)
    
        
    def delete(self,index):
        Repository.removeObject(self,index)
        
    
        
    def _loadFile(self):
        try:
            f = open(self._fileName,"rb")
            lst = pickle.load(f)
            self._list = lst
        except IOError as e:
            print(e) 
            raise IOError("Cannot load file")
        finally: 
            f.close()
        
    
class RepositoryTest(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        
    def test(self):
        list = Repository()
        list.addObject(1)
        list.addObject(2)
        assert len(list) == 2
        list.removeObject(0)
        assert len(list) == 1
        assert list.getObject(0) == 2