'''
def searcher():
    import time
    # Some 4 seconds time consuming task
    book = "This is a book"
    time.sleep(4)

    while True:
        text = (yield )
        if text in book:
            print("Your text in this book")
        else:
            print("Text is not in this book")

search = searcher()
print("Search started")
next(search)
print("Next method run")
search.send("This")
'''

def Searcher():
    import time
    letter1 = "My name is biddut. i read in the department of software engineering"
    letter2 = "My name is rohan. i read in the department of software engineering"
    time.sleep(3)

    while True:
        text = (yield)
        if text in letter1:
            print("text found in letter1")

        elif text in letter2:
            print("text found in letter 2")

Search = Searcher()
print("search started")
next(Search)
input = input("Enter the search word:\n")
Search.send(input)