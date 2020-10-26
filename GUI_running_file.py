from random import randint, choice
from sys import getsizeof
from time import time, localtime, asctime
from os import getcwd, listdir
from tkinter import Tk, Frame, Button, mainloop, Label, messagebox, Entry, StringVar,Radiobutton, IntVar

starter = []
start_count = []

wordlist = []
count = []
message_list = []
dir_list = listdir(getcwd())
data=[]
start=0
begin=0
class DnaMenu:
        def __init__(self):
                self.main_window = Tk()
                self.title_frame = Frame(self.main_window)
                self.files_frame = Frame(self.main_window)
                self.run_file = Frame(self.main_window)
                self.messages_frame = Frame(self.main_window)
                self.choice_frame = Frame(self.main_window)
                self.review_frame = Frame(self.main_window)

                self.file=IntVar()
                self.chatter=IntVar()
                lijst=[]
                chatlist = []

                self.file_label = Label(self.title_frame,
                                        text="__Choose what file to open__")
                self.file_label.pack(side="left")


                
                for i in range(len(dir_list)):
                        lijst.append(Radiobutton(self.files_frame,
                                        text=f"{dir_list[i]}",
                                        variable=self.file,
                                        value=i))

                self.run = Button(self.run_file,
                                        text="Run file",
                                        command=self.runFile)

                for element in lijst:
                        element.pack()
                self.run.pack(side="left")




                
                self.title_frame.pack()
                self.files_frame.pack()
                self.run_file.pack()
                self.messages_frame.pack()
                self.choice_frame.pack()
                
                

        def runFile(self):
                """
                Adds new options and a run button for following step
                in: choice of which file to open
                out: list of chatters in that file to choose from
                """
                self.run.destroy()
                global data
                global start
                file = self.file.get()
                infile = open(f"{dir_list[file]}", "r", encoding='utf-8')
                data=infile.readlines()
                start=self.FindSentence(data[0:int(len(data)/10)])
                self.FindChatter(start,data[0:int(len(data)/10)])
                infile.close()

                
                listing = []
                self.chatter_label = Label(self.messages_frame,
                                           text="Which chatter\n would you like to generate fake messages for")
                self.chatter_label.pack()
                for element in range(len(starter)):
                        listing.append(Radiobutton(self.messages_frame,
                                        text=f"{starter[element]}",
                                        variable=self.chatter,
                                        value=element))
                        listing[element].pack()
                self.chatter_button = Button(self.choice_frame,
                                        text="Run program",
                                        command=self.runchatter)
                self.chatter_button.pack()
                #self.chatlist.pack()

        def runchatter(self):
                """
                Runs the rest of the program using the chatter input
                in: input in the chatter radiobuttons
                out: 100 messages built by Markov chains
                        with the chat as data points

                """
                self.main_window.destroy()
                self.openfile()
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
                        som+=sum(i)
                print(f"{som} Datapoints out of {len(data)} lines")
                


                
        def openfile(self):
                """
                open file and use functions for each line in data
                in:nothing
                out:depending on functions in-line
                """
                self.main_window.destroy
                global begin
                begin=int(time())
                choice = self.chatter.get()
                c=0
                print(f"running with {starter[choice]}")
                print(f"{len(data)} lines")
                for line in data:
                        if line.count(":")>=start and (line.find("chat")==-1 or line.find("end-to-end")==-1):
                                #print(line)
                                line=line.split(":")
                                if starter[choice] in line[start-1]:
                                        words = self.removeNewlines(line[start][1:])
                                        self.getwords(words)
                                        c+=1
                self.makeNewchats(choice)
                return begin, c

        def FindSentence(self,lines):
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


        def FindChatter(self,message_index,lines):
                global starter
                for line in lines:
                        line=line.split(":")
                        if len(line)>3:
                                if line[message_index-1][5:] not in starter:
                                        print(line[message_index-1][5:])
                                        starter.append(line[message_index-1][5:])


        def removeNewlines(self,message):
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
                                words[i] = self.removeElements(words[i])
                        if len(words[i]) > 30:
                                words[i] = ""
                                
                        
                return words


        def removeElements(self,word):
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

        def getwords(self,w_words):
                """
                get all the words and put them in lists
                in: line, point of start message
                out: all words, their relative reoccurance
                """
                global wordlist
                global count
                #print("w_line",w_line)
                #print("w_words",w_words)
                last_word = ""
                if wordlist==[]:
                        wordlist.append(last_word)
                        count.append([])

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
                        count[wordlist.index(last_word)].append(wordlist.index(word))

                else:
                        count[wordlist.index(last_word)].append(wordlist.index(word))
                        
                last_word = word
        #print(w_words)


        def makeNewchats(self,c_choice):
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
                        last_word = 0
                        #words
                        for j in range(randint(5,25)):
                                if count[last_word]!=[]:
                                        new_word=choice(count[last_word])
                                else:
                                        new_word=0
                                message+=" "+wordlist[new_word]
                                last_word=new_word

                        message_list.append(message)
                        message = ""


dna_menu = DnaMenu()

