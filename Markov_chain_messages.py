from random import randint, choice
from sys import getsizeof
from time import time, localtime, asctime
from os import getcwd, listdir


def openfile():
        """
        open file and use functions for each line in data
        in:nothing
        out:depending on functions in-line
        """
        starter = []
        wordlist = []
        count = []
        message_list = []


        dir_list = listdir(getcwd())
        file=""
        while file not in range(len(dir_list)):
                file=input(f"Which file would you like to open?\n {dir_list}\n").strip()
                print(file)
                if file.isdigit():
                        file=int(file)
                elif file in dir_list:
                        file=dir_list.index(file)
                
        begin=int(time())
        infile = open(f"{dir_list[file]}", "r", encoding='utf-8')
        data = infile.readlines()
        start=FindSentence(data[0:int(len(data)/10)])
        FindChatter(start,data[0:int(len(data)/10)],starter)
        print(starter)
        infile.close()
        choice = int(input("Welke chatter wil je als basis gebruiken?\n"))
        c=0
        for line in data:
                if line.count(":")>=start and (line.find("chat")==-1 or line.find("end-to-end")==-1):
                        #print(line)
                        line=line.split(":")
                        if starter[choice] in line[start-1]:
                                words = removeNewlines(line[start][1:])
                                wordlist,count=getwords(words,wordlist,count)
                                c+=1
        infile.close()
        messagelist=makeNewchats(choice,starter,wordlist,count)
        return begin, c, messagelist, count

def FindSentence(lines):
        """
        Finds the mode for the amount of :'s in a chat
        in: 10% of the lines in the chat (list)
        out: the mode of :'s (int)
        """
        double=[]
        mode=0
        count=0
        for line in lines:
                double.append(line.count(":"))
        unique=set(double)
        for element in unique:
                if double.count(element)>count:
                        count=double.count(element)
                        mode=element
        return mode


def FindChatter(message_index,lines,c_starter):
        for line in lines:
                line=line.split(":")
                if len(line)>3:
                        if line[message_index-1][5:] not in c_starter:
                                print(line[message_index-1][5:])
                                c_starter.append(line[message_index-1][5:])
        return c_starter


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


def getwords(w_words,w_wordlist,w_count):
        """
        get all the words and put them in lists
        in: line, point of start message
        out: all words, their relative reoccurance
        """
        #print("w_line",w_line)
        #print("w_words",w_words)
        last_word = ""
        if w_wordlist==[]:
                w_wordlist.append(last_word)
                w_count.append([])
        c=0
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

                if word not in w_wordlist:
                        w_wordlist.append(word)
                        w_count.append([])
                        w_count[w_wordlist.index(last_word)].append(w_wordlist.index(word))

                else:
                        w_count[w_wordlist.index(last_word)].append(w_wordlist.index(word))
                if c==len(w_words)-1:
                        w_count[w_wordlist.index(word)].append(w_wordlist.index(""))
    
                c+=1
                last_word = word
        return w_wordlist,w_count
                
        #print(w_words)


def makeNewchats(c_choice,c_starter,c_wordlist,c_count):
        """
        Makes new messages based on all the words listed before
        in:person chosen to check

        """
        #count_sorted=[z[:] for z in count]
        #print("count",count[0])
        #count_sorted=sortlist(count_sorted)
        #print("count_sorted",count_sorted[0])
        #print("count",count[0])
        message_list=[]
        
        #sentences
        for i in range(100):
                message = c_starter[c_choice]+":"
                last_word = 0
                new_word = 0
                c=0
                #words
                while (new_word!=0 or c==0) and c<100:
                        if c_count[last_word]!=[]:
                                new_word=choice(c_count[last_word])
                                message+=" "+c_wordlist[new_word]
                                last_word=new_word
                        else:
                                new_word=0
                        
                        c+=1                 
                message_list.append(message)
                message = ""
        return message_list


def main():
        begin, messages, message_list, count = openfile()
        spring=open("analysis.txt","a",encoding='utf-8')
        spring.write(f"\n{asctime(localtime(time()))}____________________________________________________________\n")
        for message in message_list:
                print(message)
                spring.write(f"{message}\n")
        spring.close()
        end=int(time())
        print(f"\nComputing took {end-begin} seconds")
        som=0
        for i in count:
                som+=len(i)
        print(f"{som} Datapoints out of {messages} lines")


main()

