#Python program to show that we can create
# instance variables inside methods

#Class for Computer Science Student
class CSSGenius2:

    # Class Variable
    stream = 'Computer Science'

    # The init method method or constructor
    def __init__(self, classCode):

        #Instance Variable
        self.classCode = classCode

    # Adds an instance variable
    def setAddress(self, address):
        self.address = address

    # Retrieves instance variable
    def getAddress(self):
        return self.address

# Driver Code
a = CSSGenius2('101')
a.setAddress("1600 Pennsylvania Ave")
print(a.getAddress())
