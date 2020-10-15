from random import randint
from random import random

starter=["Fujoshi-chan","-. . ... ..."]
start_count=[0,0]
wordlist=[]
count=[]
message_list=[]

def openfile():
        """
        open file and use functions for each line in data
        in:nothing
        out:depending on functions in-line
        """
        infile=open("vallie_marc.txt","r",encoding='utf-8')
        choice=int(input("Welke chatter wil je als basis gebruiken?\n"))
        data=infile.readlines()
        for line in data:
                chat_index=getchatter(line)
                if line.count(starter[choice])!=0:
                        words=removeNewlines(line,chat_index)
                        getwords(words)
                del data[0]

        infile.close()
        makeNewchats(choice)

        
        n_chat=sum(start_count)
        for i in range(len(start_count)):
                start_count[i]=float(start_count[i]/n_chat)
        print("start_count",start_count)
        print("n_chat",n_chat)
        print("len(wordlist)",len(wordlist))
        print("len(count)",len(count))
        print("count",count[wordlist.index("banaan")])
        print("count",count)
        print("len(count[0])",len(count[0]))



def getchatter(c_line):
        """
        Get the chatters and put them into a starter
        in:line
        out:starter list with all the people that chat,
                with all reoccurances
        """
        global start_count
        global starter
        if c_line.count(":")>0 and c_line.count("-")>0 and len(c_line)>18\
           and c_line[0].isdigit() and c_line[3].isdigit():
                        #print(line)
                stripe_index=c_line.index("-")
                double_index=stripe_index+\
                c_line[stripe_index:].index(":")
                        
                chatter=c_line[stripe_index+2:double_index]
                if starter.count(chatter)==1:
                        start_count[starter.index(chatter)]+=1

                return double_index+2
        else:
                return 0


def removeNewlines(n_line,n_index):
        """
        Removes all newlines in the messages
        in: line, index of starting message
        out: words without the newlines
        """
        words=n_line[n_index:].split(" ")
        for word in range(len(words)):
                #Removes all newlines in the sentences
                if words[word].count("\n")>0:
                        #print("je moeder",words[word].index("\n"))
                        words[word]=words[word][:words[word].index("\n")]
                        #print(words[word])
        return words

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
        last_word=" "
        for word in w_words:
                word=word.lower()
                """
                If word is found, add one to the count of the index
                        of the word
                Add +1 to the relative (to last_word)
                """
                if word in wordlist:
                        if last_word!=" ":
                                count[wordlist.index(last_word)]\
                                        [wordlist.index(word)]+=1  
                #if not found
                #add it to the wordlist
                #count should get a new instance
                #relative count gets a new instance for each list
                else:
                        wordlist.append(word.lower())
                        count.append([])
                        for i in range(len(count)):
                                while len(count[i])<len(count):
                                        count[i].append(0)
                        
                        #print(len(wordlist))
                        if last_word!=" ":
                                count[wordlist.index(last_word)]\
                                [wordlist.index(word)]+=1
                        
                last_word=word
                
        #print(w_words)

def makeNewchats(c_choice):
        """
        Makes new messages based on all the words listed before
        in:person chosen to check

        """
        global message_list
        count_sorted=[z[:] for z in count]
        #print("count",count[0])
        count_sorted=sortlist(count_sorted)
        #print("count_sorted",count_sorted[0])
        #print("count",count[0])
        last_word=wordlist[(randint(0,len(wordlist)-1))]
        r=0
        #sentences
        relative()
        for i in range(100):
                message=starter[c_choice]+":"
                #words
                for j in range(randint(5,25)):
                        r=random()
                        #find the random word
                        for k in range(len(count_sorted[wordlist.index(last_word)])):
                                if count_sorted[wordlist.index(last_word)][k]>r:
                                        #Finds the specific word used
                                        #By reversing the cumulative sum in sortlist (by doing, current minus last)
                                        #find the index of that in count
                                        #Then use that index for the word in the wordlist

                                        
                                        #print(j)
                                        #print(k)
                                        #print(r)
                                        print("k",count_sorted[wordlist.index(last_word)][k])
                                        print("k-1",count_sorted[wordlist.index(last_word)][k-1])
                                        print("k- k-1",(count_sorted[wordlist.index(last_word)][k]) - (count_sorted[wordlist.index(last_word)][k-1]))
                                        #print("count[wordlist.index(last_word)]",count[wordlist.index(last_word)])
                                        #print("count_sorted[wordlist.index(last_word)]",count_sorted[wordlist.index(last_word)])
                                        print(wordlist)
                                        message+=" "+wordlist[count[wordlist.index(last_word)].index(\
                                                        int(1000000*\
                                                            (count_sorted[wordlist.index(last_word)][k]\
                                                             -count_sorted[wordlist.index(last_word)][k-1])))]
                                        last_word=wordlist[count[wordlist.index(last_word)].index\
                                                           (int(1000000*\
                                                                (count_sorted[wordlist.index(last_word)][k]\
                                                                 -count_sorted[wordlist.index(last_word)][k-1])))]
                                        
                message_list.append(message)
                message=""


def relative():
        """
        Takes count, makes all elements within the lists and takes their relative to the total of the list
        in:count
        out:altered count
        """
        global count
        
        for i in range(len(count)):
                total=sum(count[i])
                if total==0:
                        total=1
                for j in range(len(count[i])):
                        count[i][j]=int(1000000*(count[i][j]/total))


def sortlist(listing):
        """
        sorts for each element in a list and makes them relative to the total
        in: list
        out: sorted list
        """
        total=1
        for i in range(len(listing)):
                #print("before",listing[i])
                listing[i].sort(reverse=True)
                #print("after",listing[i])
                total=sum(listing[i])

                if total==0:
                        total=1
                
                for j in range(len(listing[i])):
                        
                        if j>0 and i==0:
                                #print(listing[i][j]+listing[i][j-1])
                                listing[i][j]=listing[i][j-1]+(listing[i][j]/total)
                        else:
                                listing[i][j]=listing[i][j]/total
        return listing
        



def main():
        openfile()
        for message in message_list:
                print(message)


main()

