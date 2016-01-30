#Test class for IPGSdb.py 

from IPGSdb import *
from IPGSdb import deleteUsers

def testUsers():
	print "\n"
	print "---------------------------------------------------------------------------------------------------------------------"
	print "\n"
	print "START TESTING USERS CRUD FUNCTIONS"
	print "\n"
	print "---------------------------------------------------------------------------------------------------------------------"
	print readUsers()
	deleteUsers()
	print readUsers()
	A = createUsers('ayolo@yolo.com','dqsv','male','Raheja Township','mumbai','13131','1-1-2012')
	print readUsers(A)
	B = createUsers(None,'dqsv','male',None,'mumbai','13131',None)
	print readUsers(B)

	C=createUsers('ayolsca.com','dqsv','male','21','mumbai','13131','1-1-2012')
	D=createUsers('ayolscasdqas','dqsv','male','21','mumbai','13131','1-1-2012')
	print readUsers(A)
	updateUsers(A,"Dad","Dad","Dad","Dad","Dad",'1-1-2000')
	print readUsers(A)
	updateUsers(A,None,"SAD","SAD","SAD","SAD",'1-1-1994')
	print readUsers()
	print "---------------------------------------------------------------------------------------------------------------------"
	print "\n"
	print "DONE WITH USERS CRUD"
	print "\n"
	print "---------------------------------------------------------------------------------------------------------------------"
	return (C,D)


def testIssues(C):
	print "\n"
	print "---------------------------------------------------------------------------------------------------------------------"
	print "\n"
	print "START TESTING ISSUES CRUD FUNCTIONS"
	print "\n"
	print "---------------------------------------------------------------------------------------------------------------------"
	print(readIssues(None))
	print C[0]
	X=createIssues(C[0],'Big problem','This is a very big problem... Blah..Blah..Blah',12312.1231,132123.12312,'c:/ad/image/1.jpg',False,3)
	Z=createIssues(C[0],'Big problem','This is a very big problem... Blah..Blah..Blah',12312.1231,132123.12312,'c:/ad/image/1.jpg',False,3)
	print X
	print readIssues(X)
	print readIssues()
	return (X,Z)

	#Z=createIssues(C[0],'Big proqw','This is a very big problem... Blah..Blah..Blah',12312.1231,132123.12312,'c:/ad/image/1.jpg',True,3)
	#print Z
	#Y=createIssues(C[1],'Big problem','This is a very big problem... Blah..Blah..Blah',12312.1231,132123.12312,'c:/ad/image/1.jpg',True,3)
	#print Y
	#print(readIssues())
	#print(readIssues(X))
	#updateIssues(X,"dwa","adwwa",21312,12312,"wda",False,123,True)
	#print(readIssues(X))
	#print(readIssues())
	#deleteIssues(X)
	#print(readIssues(X))
	#print readIssues()
	#print readUsers()
	#deleteIssues()
	#print readIssues()

	print "---------------------------------------------------------------------------------------------------------------------"
	print "\n"
	print "DONE WITH ISSUES CRUD"
	print "\n"
	print "---------------------------------------------------------------------------------------------------------------------"


def testComments():
	pass

def testVotes(X,C):
	print "---------------------------------------------------------------------------------------------------------------------"
	print "\n"
	print "TESTING VOTES TABLE"
	print "\n"
	print "---------------------------------------------------------------------------------------------------------------------"
	print "X:",X
	print "C[0]:",C[0]
	print readUsers(C[0])
	print readIssues(X[0])

	createVotes(X[0],C[0],False)
	createVotes(X[0],C[1],False)
	print readVotes(X[0])
	createVotes(X[1],C[0],True)
	print readVotes()
	deleteVotes(X[0])
	print readVotes()
	print readVotes(X[0])
	updateVotes(X[0],C[0],True)
	print readVotes(X[0])

if __name__ == '__main__':
	C=testUsers()
	X=testIssues(C)
	testComments()
	testVotes(X,C)
	print "Success! All tests passed!"