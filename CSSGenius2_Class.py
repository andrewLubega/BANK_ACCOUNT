# Python program to show that we can create
#instance variables inside methods

#Class for Computer Science Student
class CSSGenius2:

    # Class Varibale
    stream = "Computer Student"

    # The init metho or constructor
    def init(self, classCode):

        # Instance Variable
        self.classCode = classCode

        # Adds an instancd variable
        def getAddress(self, address):
            self.Address = address

            # Retrieves instance variable
            def getAddress(self):
                return self.Address

# Driver Code
a = CSSGenius2
a.setAddress("Noida, UP")
print(a.getAddress())
