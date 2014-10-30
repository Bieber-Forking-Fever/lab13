#########################################
#
#         70-100pt - Making a game
#
#########################################


# 70pt - Add buttons for left, right and down that move the player circle
# 100pt - using lab 11 as an example, add in three horizontally scrolling "enemies"
# Make them scroll at different speeds and directions.



from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=600, background='white')
player = drawpad.create_oval(390,580,410,600, fill="red")

# Create your "enemies" here, before the class


class MyApp:
	def __init__(self, parent):
       	    global drawpad
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    self.up = Button(self.myContainer1)
       	    self.up.configure(text="up", background= "green")
       	    self.up.grid(row=0,column=1)

       	    self.left = Button(self.myContainer1)
       	    self.left.configure(text="left", background= "green")
       	    self.left.grid(row=1,column=0)

       	    self.right = Button(self.myContainer1)
       	    self.right.configure(text="Right", background= "green")
       	    self.right.grid(row=1,column=2)

       	    self.down = Button(self.myContainer1)
       	    self.down.configure(text="Down", background= "green")
       	    self.down.grid(row=3,column=1)


       	    # Bind an event to the first button
       	    self.up.bind("<Button-1>", self.upClicked)
            self.down.bind("<Button-1>", self.downClicked)
            self.left.bind("<Button-1>", self.leftClicked)
            self.right.bind("<Button-1>", self.rightClicked)
       	    
       	    # No need to edit this - just includes the drawpad into our frame
       	    drawpad.pack(side=BOTTOM)
	
	def animate(self):
	    global drawpad
	    global player
	    # Remember to include your "enemies" with "global"
	    	
		
	def upClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,-20)
	def downClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,20)
	def leftClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,-20,0)
	def rightClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,20,0)


circle = drawpad.create_oval(20, 20, 100, 100, fill='green')
circle2 = drawpad.create_oval(120, 120, 200, 200, fill='green')
direction = 5

def animate2():
    global direction
    # Get the x and y co-ordinates of the circle
    x1, y1, x2, y2 = drawpad.coords(circle)

    drawpad.move(circle,direction,0)
    if x2 > 800: 
        drawpad.move(circle,-800,0)
        direction = 5

    drawpad.after(1, animate)



def animate():
    global direction
    # Get the x and y co-ordinates of the circle
    x1, y1, x2, y2 = drawpad.coords(circle2)

    drawpad.move(circle2,direction,0)
    if x2 > 800: 
        drawpad.move(circle2,-800,0)
        direction = 5

    drawpad.after(1, animate)













animate2()
animate()		
app = MyApp(root)
root.mainloop()