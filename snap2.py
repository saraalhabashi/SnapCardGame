import tkinter
from tkinter import*
import tkinter as tk
import random

class snap:
    def __init__(self,root):
        self.root = root
        
        self.label=Label(self.root,text="Snap!",font=("Segoe Print",80,"bold","italic"),bg="darkgreen",fg="white").grid(column=3,row=0,ipadx=50,ipady=30)

        self.img1 = PhotoImage(file = "button1.png")#This is User Name button
        self.button1=Button(self.root,image=self.img1,bg="darkgreen",border=0,command=self.userName).grid(column=3,row=5)

        self.img2 = PhotoImage(file = "button2.png")#This is How to play button Button
        self.button2=Button(self.root,image=self.img2,bg="darkgreen",border=0,command=self.howToPlay).grid(column=3,row=6)

        self.img3 = PhotoImage(file = "button3.png")#This is Start button
        self.button3=Button(self.root,image=self.img3,bg="darkgreen",border=0,command=self.start,state=DISABLED)#Here we DISABLED the START BUTTON until the user/player enter his/her name 
        self.button3.grid(column=3,row=7)

        self.img4 = PhotoImage(file = "button4.png")#This is Register button
        self.img5 = PhotoImage(file = "button5.png")#This is Close button
        self.cardCover = PhotoImage(file = "back.png")
        self.dealI = PhotoImage(file = "deal.png")
        
        self.ca = PhotoImage(file = "ca.png",name="ca")
        self.c2 = PhotoImage(file = "c2.png",name="c2")
        self.c3 = PhotoImage(file = "c3.png",name="c3")
        self.c4 = PhotoImage(file = "c4.png",name="c4")
        self.c5 = PhotoImage(file = "c5.png",name="c5")
        self.c6 = PhotoImage(file = "c6.png",name="c6")
        self.c7 = PhotoImage(file = "c7.png",name="c7")
        self.c8 = PhotoImage(file = "c8.png",name="c8")
        self.c9 = PhotoImage(file = "c9.png",name="c9")
        self.c10 = PhotoImage(file = "c10.png",name="c10")
        self.cj = PhotoImage(file = "cj.png",name="cj")
        self.ck = PhotoImage(file = "ck.png",name="ck")
        self.cq = PhotoImage(file = "cq.png",name="cq")

        self.Sa = PhotoImage(file = "sa.png",name="sa")
        self.S2 = PhotoImage(file = "s2.png",name="s2")
        self.S3 = PhotoImage(file = "s3.png",name="s3")
        self.S4 = PhotoImage(file = "s4.png",name="s4")
        self.S5 = PhotoImage(file = "s5.png",name="s5")
        self.S6 = PhotoImage(file = "s6.png",name="s6")
        self.S7 = PhotoImage(file = "s7.png",name="s7")
        self.S8 = PhotoImage(file = "s8.png",name="s8")
        self.S9 = PhotoImage(file = "s9.png",name="s9")
        self.S10 = PhotoImage(file = "s10.png",name="s10")
        self.Sj = PhotoImage(file = "sj.png",name="sj")
        self.Sk = PhotoImage(file = "sk.png",name="sk")
        self.Sq = PhotoImage(file = "sq.png",name="sq")

        self.da = PhotoImage(file = "da.png",name="da")
        self.d2 = PhotoImage(file = "d2.png",name="d2")
        self.d3 = PhotoImage(file = "d3.png",name="d3")
        self.d4 = PhotoImage(file = "d4.png",name="d4")
        self.d5 = PhotoImage(file = "d5.png",name="d5")
        self.d6 = PhotoImage(file = "d6.png",name="d6")
        self.d7 = PhotoImage(file = "d7.png",name="d7")
        self.d8 = PhotoImage(file = "d8.png",name="d8")
        self.d9 = PhotoImage(file = "d9.png",name="d9")
        self.d10 = PhotoImage(file = "d10.png",name="d10")
        self.dj = PhotoImage(file = "dj.png",name="dj")
        self.dk = PhotoImage(file = "dk.png",name="dk")
        self.dq = PhotoImage(file = "dq.png",name="dq")

        
        self.ha = PhotoImage(file = "ha.png",name="ha")
        self.h2 = PhotoImage(file = "h2.png",name="h2")
        self.h3 = PhotoImage(file = "h3.png",name="h3")
        self.h4 = PhotoImage(file = "h4.png",name="h4")
        self.h5 = PhotoImage(file = "h5.png",name="h5")
        self.h6 = PhotoImage(file = "h6.png",name="h6")
        self.h7 = PhotoImage(file = "h7.png",name="h7")
        self.h8 = PhotoImage(file = "h8.png",name="h8")
        self.h9 = PhotoImage(file = "h9.png",name="h9")
        self.h10 = PhotoImage(file = "h10.png",name="h10")
        self.hj = PhotoImage(file = "hj.png",name="hj")
        self.hk = PhotoImage(file = "hk.png",name="hk")
        self.hq = PhotoImage(file = "hq.png",name="hq")

        self.cardP=[self.Sa,self.S2,self.S3,self.S4,self.S5,self.S6,self.S7,self.S8,self.S9,self.S10,self.Sj,self.Sk,self.Sq,
                    self.ca,self.c2,self.c3,self.c4,self.c5,self.c6,self.c7,self.c8,self.c9,self.c10,self.cj,self.ck,self.cq,
                    self.da,self.d2,self.d3,self.d4,self.d5,self.d6,self.d7,self.d8,self.d9,self.d10,self.dj,self.dk,self.dq,
                    self.ha,self.h2,self.h3,self.h4,self.h5,self.h6,self.h7,self.h8,self.h9,self.h10,self.hj,self.hk,self.hq]

    
        #length of the user name
    def limitSizeName(self,*args):
        self.value = self.v.get()
        if len(self.value) >30:
            self.v.set(self.value[:30])
            self.note=Label(self.top,text="The user name should NOT be greater than 30 characters.",bg="darkgreen",font=("Segoe Print",10,"bold"),fg="red").grid( columnspan=3,rowspan=3,column=0,row=1)
        
    def quit(self,event):#to exsit from the window by clicking ENTER KEY from the keyboard  
        self.top.destroy()
        
    def userName(self):
        self.top=Toplevel()#To display a window that allow the user/player to enter his/her name .
        self.top.title("USER NAME")
        self.top.geometry("800x80")
        self.top.config(background="darkgreen")
        self.userName=Label(self.top,text="Enter your user name : ",bg="darkgreen",font=("Segoe Print",18,"bold","italic"),fg="white").grid(column=0,row=0)
        self.v = StringVar()
        self.v.set("")
        self.entry=Entry(self.top,width=40,textvariable=self.v)
        self.v.trace("w",self.limitSizeName)
        self.entry.bind("<Return>",self.quit)#to exsit from the window by clicking ENTER KEY from the keyboard  
        self.entry.grid(column=1,row=0)
        self.entry.focus()
        self.register=tkinter.Button(self.top,image=self.img4,bg="darkgreen",border=0,command=self.top.destroy)#to exsit from the window by clicing on REGISTER BUTTON 
        self.register.grid(column=4,row=0)
        self.button3.config(state=NORMAL)#To allow the user to use the START BUTTON 
    
    def howToPlay(self):
        self.top2=Toplevel()#To display a window that explains the idea of game. 
        self.top2.title("How To Play")
        self.top2.geometry("650x530")
        self.top2.config(background="darkgreen")
        self.text="""The simple card game - Snap!

Play snap! with your device in by clicking on start.
Easy to play:

- Click on your deck of cards to place a card on the table

- Then your opponent turns over a card

- If both cards match then it's a test of reactions.

-Can you click on your discard pile before your opponent clicks on their pile?

- The fastest player wins all the discarded cards

- The winner is the player who wins all the cards

-you have enter your name to start and deal first to play"""
        
        self.how=Message(self.top2,text=self.text,bg="darkgreen",font=("Segoe Print",11,"bold","italic"),fg="white").grid(column=0,row=0)
        self.close=tkinter.Button(self.top2,image=self.img5,bg="darkgreen",border=0,command=self.top2.destroy)
        self.close.grid(column=0,row=2)


    def dealF(self,event):#lists of cards
        random.shuffle(self.cardP)
        
        self.playerList=[]
        self.systemList=[]
        self.winerList=[]
        
        for x in range(0,26):
            self.playerList.append(self.cardP[x])
            

        for i in range(26,len(self.cardP)):
            self.systemList.append(self.cardP[i])


        self.remaining = 0
        self.remaining2 = 0 
        self.cover2.config(state=NORMAL)#TO allow the user/player to flip the cards one by one by clicking on the cover card 
        self.countdown(30)
        self.deal.config(state=DISABLED)

        #Scores for the player and system   
        self.sP=0
        self.sS=0
        

    def countdown2(self, remaining2 = None):# to count the player time to click on card if two are match

        if remaining2 is not None:

            self.remaining2 = remaining2

        if self.remaining2 > 0:

            
            self.sCard.config(command=self.snapCard)
            self.pCard.config(command=self.snapCard)
            
            self.remaining2 = self.remaining2 - 1
            
            self.top3.after(100, self.countdown2)

           

        elif self.remaining2 == 0:
            
            self.sS=self.sS+1
            self.score.config(text="Score %d" %self.sS)
            self.score2.config(text="Score %d" %self.sP)
            for winner in self.winerList:
                    self.winner=random.choice(self.winerList)
                    self.systemList.append(self.winner)
            
            self.player=random.choice(self.playerList)#To choose the next card randomly for the user/player            

            self.pCard.config(image=self.player)
            
            self.system=random.choice(self.systemList)#To choose the next card randomly for the system
            
            self.sCard.config(image=self.system)

            self.systemList.remove(self.system)#To remove cardes form the system one by one
            self.playerList.remove(self.player)#To remove cardes form the user/player one by one
            
        else:
            pass


    #Method for compairing the shown 2 cards & incrementing the score whenever there is a snap     
    def snapCard(self):
        if self.pCard.cget('image')[1:]== self.sCard.cget('image')[1:]:
                self.sP=self.sP+1
                self.score2.config(text="Score %d" %self.sP)
                self.score.config(text="Score %d" %self.sS)
                
                
                for winner in self.winerList:
                    self.winner=random.choice(self.winerList)
                    self.playerList.append(self.winner)

                                
                self.player=random.choice(self.playerList)#To choose the next card randomly for the user/player            

                self.pCard.config(image=self.player)
                
                self.system=random.choice(self.systemList)#To choose the next card randomly for the system
                
                self.sCard.config(image=self.system)

                self.systemList.remove(self.system)#To remove cardes form the system one by one
                self.playerList.remove(self.player)#To remove cardes form the user/player one by one
            
                self.countdown2(-1)
        
                
        

    def cardF(self):
            self.player=random.choice(self.playerList)#To choose the next card randomly for the user/player            

            self.pCard=Button(self.top3,image=self.player,bg="darkgreen",border=0)
            self.pCard.grid(column=2,row=2,rowspan=2,sticky=SW)
            
            self.var1=IntVar()
            self.var1.set(len(self.playerList)-1)#number of cards for the user/player 

            
            self.card=Label(self.top3,textvariable=self.var1,bg="darkgreen",font=("arial",18,"bold"),fg="white")
            self.card.grid(column=1,row=5,ipadx=100)

            self.winerList.append(self.player)#to add the deleted card into winner list


            self.system=random.choice(self.systemList)#To choose the next card randomly for the system
            
            self.sCard=Button(self.top3,image=self.system,bg="darkgreen",border=0)
            self.sCard.grid(column=0,row=2,rowspan=2,sticky=SE)
            
            self.var2=IntVar()
            self.var2.set(len(self.systemList)-1)#number of cards for the system 
            
            self.card1=Label(self.top3,textvariable=self.var2,bg="darkgreen",font=("arial",18,"bold"),fg="white")
            self.card1.grid(column=1,row=0,ipadx=100)

            self.winerList.append(self.system)#to add the deleted card into winner list

            if self.pCard.cget('image')[1:]== self.sCard.cget('image')[1:]:
                self.countdown2(10)
            else:
                pass

            if (len(self.playerList)-1 == 0 and self.sS > self.sP):# if the system list length zero

                            self.playergameOver=Toplevel()

                            self.playergameOver.geometry("700x100")

                            self.playergameOver.title("Game Over !")

                            self.playergameOver.config(background="darkgreen")
            
                            self.topgameOverLable=Label(self.playergameOver,text="Game Over !\n the COMPUTER is the WINNER \n Your score is "+str(self.sP)+" and computer score is "+str(self.sS),bg="darkgreen",font=("arial",14,"bold"),fg="white")
                            self.topgameOverLable.grid(column=1,row=2,padx=(110,0),pady=30)

                            self.cover2.config(state=DISABLED)
                            self.top3.destroy()

            elif len(self.systemList)-1==0 and self.sS<self.sP:# if the player list length zero
                

                        self.systemmgameOver=Toplevel()

                        self.systemmgameOver.geometry("700x100")

                        self.systemmgameOver.title("Game Over !")

                        self.systemmgameOver.config(background="darkgreen")
                
                        self.topgameOverLable=Label(self.systemmgameOver,text="Game Over !\n Congratulations , YOU are the WINNER \n Your score is "+str(self.sP)+" and computer score is "+str(self.sS),bg="darkgreen",font=("arial",14,"bold"),fg="white")
                        self.topgameOverLable.grid(column=1,row=2,padx=(110,0),pady=30)

                        self.cover2.config(state=DISABLED)
                        self.top3.destroy()

            elif len(self.systemList)-1 == 0 and len(self.playerList)-1 == 0 and self.sS==self.sP:

                        self.gameOver=Toplevel()

                        self.gameOver.geometry("700x100")

                        self.gameOver.title("Game Over !")

                        self.gameOver.config(background="darkgreen")
                
                        self.topgameOverLable=Label(self.gameOver,text="Game Over !\n No one wins the game \n Your score is "+str(self.sP)+" and computer score is "+str(self.sS),bg="darkgreen",font=("arial",14,"bold"),fg="white")
                        self.topgameOverLable.grid(column=1,row=2,padx=(110,0),pady=30)

                        self.cover2.config(state=DISABLED)
                        self.top3.destroy()
                        
            else:
                self.systemList.remove(self.system)#To remove cardes form the system one by one
                self.playerList.remove(self.player)#To remove cardes form the user/player one by one

            




    def start(self):
        self.top3=Toplevel()
        self.top3.title("Game Page")
        self.top3.geometry("700x450")
        self.top3.config(background="darkgreen")



            
        self.score=Label(self.top3,text="Score: ",bg="darkgreen",font=("arial",18,"bold"),fg="white")
        self.score.grid(column=0,row=0,sticky=SW)
        
        self.name=Label(self.top3,text="Computer",bg="darkgreen",font=("arial",18,"bold"),fg="white").grid(column=2,row=0,ipadx=10,sticky=SE)
        
        self.cover=Label(self.top3,image=self.cardCover,bg="darkgreen",border=0)
        self.cover.grid(column=1,row=1)


        self.timer=Label(self.top3,text="timer",bg="darkgreen",font=("arial",18,"bold"),fg="white")
        self.timer.grid(column=1,row=3,ipadx=10)

        self.deal=Button(self.top3,image=self.dealI,bg="darkgreen",border=0)
        self.deal.bind("<Button-1>", self.dealF)
        self.deal.grid(column=1,row=2)
        




        self.cover2=Button(self.top3,image=self.cardCover,bg="darkgreen",border=0,state=DISABLED,command=self.cardF)#The Button is DISABLED in order to prohibit the user/player from start playing until DEAL button is clicked
        self.cover2.grid(column=1,row=4)

        
        self.score2=Label(self.top3,text="Score: ",bg="darkgreen",font=("arial",18,"bold"),fg="white")
        self.score2.grid(column=0,row=5,sticky=NE)
        
        self.name2=Label(self.top3,textvariable=self.v,bg="darkgreen",font=("arial",18,"bold"),fg="white").grid(column=2,row=5,ipadx=10,sticky=NW)


                
    #Method for calculating the remaing time before the Game over         
    #Method for calculating the remaing time before the Game over         
    def countdown(self, remaining = None):

        if remaining is not None:

            self.remaining = remaining

        if self.remaining <= 0:

            self.timer.config(text="Time's Up !")

            self.topgameOver=Toplevel()

            self.topgameOver.geometry("700x100")

            self.topgameOver.title("Time's Up !")

            self.topgameOver.config(background="darkgreen")

            self.topgameOverLable=Label(self.topgameOver,text="Game Over !",bg="darkgreen",font=("arial",14,"bold"),fg="white")

            self.topgameOverLable.grid(column=1,row=2,padx=(110,0),pady=30)

            self.top3.destroy()

            #To know who is the winner :

            if self.sP == self.sS:

                self.topgameOverLable.config(text="Time's Up !\n No one wins the game \n Your score is "+str(self.sP)+" and computer score is "+str(self.sS))

                self.topgameOverLable.grid(column=1,row=2,padx=(180,0),pady=30)

                self.top3.destroy()

            elif self.sP < self.sS:

                self.topgameOverLable.config(text="Time's Up !\n the COMPUTER is the WINNER \n Your score is "+str(self.sP)+" and computer score is "+str(self.sS))

                self.topgameOverLable.grid(column=1,row=2,padx=(150,0),pady=30)

                self.top3.destroy()

            elif self.sP > self.sS:

                self.topgameOverLable.config(text="Time's Up !\n Congratulations , YOU are the WINNER \n Your score is "+str(self.sP)+" and computer score is "+str(self.sS))

                self.topgameOverLable.grid(column=1,row=2,padx=(110,0),pady=30)

                self.top3.destroy()
                

           

        else:

            self.timer.config(text="%d Sec Remaining" % self.remaining)

            self.remaining = self.remaining - 1

            self.top3.after(1000, self.countdown)


            
            
            


if __name__=='__main__':
    root=Tk()
    root.geometry("400x600")
    root.title("Snap game")
    root.config(background="darkgreen")
    snapGame=snap(root)
    root.mainloop()
