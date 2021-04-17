#   Selector.py
#   version 1

"""
 A filter that can be applied to a FileCollection.

### Attributes

### Operations
* ‘Operators’ that act on Selector objects to produce new Selector objects.
#### union
* binary
* Produce the set union of the criteria (apply ||).
* left associative
* This may best be left to v2, thus deferring the need to bother with operator precedence.
#### intersect
* binary
* Produce the set intersection of the criteria (apply &&).
* left associative

### Methods
#### Instantiator — Selector(<criteria>) : Selector
* <criteria> is some sort of expression that would evaluate to Boolean
* Examples:
	* `size("+20M") && name(".txt")`
	* `date(“1-2Y”)`
	* `date("-2Y")`
	* `date(temp)` where temp is an identifier
	* `type("mp3")`
* From examples:
	* Boolean operators
		* &&
		* ||
		* Combinations with ‘not’?  Leave for v2.
	* size(“+20M”) evaluates to true if the file or directory size is greater than 20 MB
		* “+20M” an expression that has itself to be parsed
	* name(“.txt”) evaluates to true if the file name contains string ‘.txt’
		* “.txt” is not a regex
		* Examples of matching names will include “.txtrc”, “a.txt”, “a.txta”
	* date(“1-2Y”) evaluates to true if the file’s or directory’s last modified date (lmd) is between 1 and 2 years ago
		* To be precise about this string:
			* Let today’s date be `<d>/<m>/<y>`
			* Any file with lmd >= `<d>/<m>/<y-2>` will be included if its lmd <= `<d>/<m>/<y-1>`
	* date(“-2Y”) evaluates to true if the file’s or directory’s lmd is no more than 2 years ago (i.e. lmd <= `<d>/<m>/<y-2>`)
	* type(“mp3”) evaluates to true if the FSObject is a file and the last four characters of its name are “.mp3” 


"""

from pathlib import Path, PosixPath

class Selector:
	
	nameContains = ""

	def __init__(self, nameContains:str=""):
# 		print("Selector instantiator called with name contains =", nameContains)
		self.nameContains = nameContains
		
	"""
	determine whether the object specified by the PosixPath path meets all the
	criteria in this selector,
	returning True if it does, else false
	"""
	def testPath(self, testPath:PosixPath=None) -> bool:
		if testPath == None:
			return False
		else:
			# do the tests
			retval = True
			# test 1: nameContains
			if self.nameContains == "":
				pass
			else:
				# test nameContains
				if not testPath.match("*" + self.nameContains + "*"):
					retval = False
		
		return retval
			
			

	def __str__(self):
		return("a selector with nameContains = %s" % (self.nameContains))        
       
       
        