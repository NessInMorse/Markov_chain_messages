from random import randint, choices
from sys import getsizeof
from time import time, localtime, asctime
#all users should be put in this list
#e.g. starter= ["NessinMorse","-. . ... ..."] etc.
starter = []

start_count = [0 for i in starter]
wordlist = []
count = []
message_list = []


def openfile():
        """
        open file and use functions for each line in data
        in:nothing
        out:depending on functions in-line
        """
        begin=int(time())
        infile = open("name_of_file", "r", encoding='utf-8')
        choice = int(input("What chatter would you like to choose from?\n {starter}\n"))
                data = infile.readlines()
        start=FindSentence(data[0:int(len(data)/10)])
        infile.close()
        for line in data:
                if line.find("chat")==-1 or line.find("end-to-end")==-1:
                        if starter[choice] in line:
                                line=line.split(":")[start][1:]
                                words = removeNewlines(line)
                                getwords(words)
        infile.close()
        makeNewchats(choice)
        return begin

def FindSentence(lines):
        """
        Finds the median for the amount of :'s in a chat
        in: 10% of the lines in the chat
        out: the median of :'s
        """
        double=[]
        median=0
        count=0
        for line in lines:
                double.append(line.count(":"))
        unique=set(double)
        for element in unique:
                if double.count(element)>count:
                        count=double.count(element)
                        median=element
        return median


def removeNewlines(message):
        """
        Removes all newlines in the messages
        in: line, index of starting message
        out: words without the newlines
        """
        words=message.split()
        for word in range(len(words)):
                #Removes all newlines in the sentences
                if words[word].count("\n") > 0:
                        #print("je moeder",words[word].index("\n"))
                        words[word] = words[word][:words[word].index("\n")]
                        #print(words[word])
        
        for i in range(len(words)):
                if words[i].find(".") !=- 1\
                   or words[i].find("?") !=- 1\
                   or words[i].find(",") != -1\
                   or words[i].find("\'") != -1\
                   or words[i].find("\"") != -1:
                        words[i] = removeElements(words[i])
                if len(words[i]) > 30:
                        words[i] = ""
                        
                
        return words


def removeElements(word):
        word=list(word)
        while word.count(".") > 0 or word.count("?") > 0 or word.count(",") > 0\
              or word.count("\'") > 0 or word.count("\"") > 0:
                if word.count(".") > 0:
                        word.remove(".")
                if word.count("?") > 0:
                        word.remove("?")
                if word.count(",") > 0:
                        word.remove(",")
                if word.count("\'") > 0:
                        word.remove("\'")
                if word.count("\"") > 0:
                        word.remove("\"")

        return "".join(word)


def getwords(w_words):
        """
        get all the words and put them in lists
        in: line, point of start message
        out: all words, their relative reoccurance
        """
        global wordlist
        global count
        #print("w_line",w_line)
        #print("w_words",w_words)
        last_word = " "
        for word in w_words:
                word=word.lower()
                """
                If word is found, add one to the count of the index
                        of the word
                Add +1 to the relative (to last_word)
                """

                #if not found
                #add it to the wordlist
                #count should get a new instance
                #relative count gets a new instance for each list
                
                if word not in wordlist:
                        wordlist.append(word)
                        count.append([])
                        for i in range(len(count)):
                                count[i].append(0)
                                while len(count[i])<len(count):
                                        count[i].append(0)



                if last_word != " ":
                        count[wordlist.index(last_word)]\
                        [wordlist.index(word)] += 1
                        
                last_word = word
                
        #print(w_words)


def makeNewchats(c_choice):
        """
        Makes new messages based on all the words listed before
        in:person chosen to check

        """
        global message_list
        #count_sorted=[z[:] for z in count]
        #print("count",count[0])
        #count_sorted=sortlist(count_sorted)
        #print("count_sorted",count_sorted[0])
        #print("count",count[0])
        
        #sentences
        for i in range(100):
                message = starter[c_choice]+":"
                last_word = randint(0,len(wordlist)-1)
                #words
                for j in range(randint(5,25)):
                        new_word=count[last_word].index(choices(count[last_word],count[last_word])[0])
                        message+=" "+wordlist[new_word]
                        last_word=new_word
                                        
                message_list.append(message)
                message = ""


def main():
        begin=openfile()
        spring=open("analysis.txt","a",encoding='utf-8')
        spring.write(f"\n{asctime(localtime(time()))}____________________________________________________________\n")
        for message in message_list:
                print(message)
                spring.write(f"{message}\n")
        spring.close()
        end=int(time())
        print(f"Computing took {end-begin} seconds")


main()

