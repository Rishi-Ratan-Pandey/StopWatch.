from tkinter import*
sec=00
min_=00
# use elf when thre is a chance to get both satement true
hr=00
def stop_func():
	pass
def add():
	global min_
	global sec
	global hr
	sec+=1
	print(sec)
	root.after(1000,add)
	if sec<=10:
		data.set(f'0{sec}')
	if sec>=10:
		data.set(f'{sec}')
	if sec>=59:
		sec-=59
		min_+=1
		data_1.set(min_)
	if min_>=59:
		min_-=59
		hr+=1
		data_2.set(hr)
def start_func():
	add()
def reset_func():
	pass
def main():
	global data
	global data_1
	global data_2
	global hr
	global min_
	global sec
	global root
	root=Tk()
	root.title('StopWatch')
	root.geometry('315x200')
	hr_data=IntVar()
	min_data=IntVar()
	sec_data=IntVar()
	data=IntVar()
	data_1=IntVar()
	data_2=IntVar()
	sec_lab=Label(root,textvariable=data,text=sec,font=('Courier',50))
	data.set(f'00')
	sec_lab.pack()
	min_label=Label(root,textvariable=data_1,text=min_,font=('Courier',50))
	data_1.set(min_)
	min_label.pack()
	hr_label=Label(root,textvariable=data_2,text=hr,font=('Courier',50))
	data_1.set(hr)
	hr_label.pack()
	stop=Button(root,text='Stop',command=stop_func,font=('Courier',15,'bold'),borderwidth=5,bg='cyan3',fg='white',activeforeground='white',activebackground='cyan3')
	stop.place(x=20,y=125)#START STOP RESET
	start=Button(root,text='Start',command=start_func,font=('Courier',15,'bold'),borderwidth=5,bg='orange',fg='white',activeforeground='white',activebackground='orange')
	start.place(x=115,y=125)
	start=Button(root,text='Reset',command=reset_func,font=('Courier',15,'bold'),borderwidth=5,bg='black',fg='white',activeforeground='white',activebackground='black')
	start.place(x=215,y=125)
	root.mainloop()
if __name__=='__main__':
	main()
	# hr=Label(root,text=hr,textvariable=hr_data,font=('Courier',50,'bold'))
	# hr.place(x=50,y=35)
	# min_labesec_labLabel(root,text=min_,font=('Courier',50,'bold'))
	# min_label.place(x=125,y=35)
	# sec_labesec_labLabel(root,text=sec,font=('Courier',50,'bold'))
	# sec_label.place(x=200,y=35