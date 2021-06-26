from tkinter import*
sec=00
min_=00
hr=00
def stop_func():
	root.after_cancel(id_)
	start['state']='active'
def add():
	global min_
	global sec
	global hr
	global id_
	sec+=1
	id_=root.after(1000,add)
	if sec<=10:
		data.set(f'0{sec}')
	if sec>=10:
		data.set(f'{sec}')
	
	if sec>=59:
		sec-=59
		min_+=1
		if min_<=10:
			data_1.set(f'0{min_}')
			data.set(f'00')
		if min_>=10:
			data_1.set(f'{min_}')
			data.set(f'00')

	if min_>=59:
		min_-=59
		hr+=1
		if hr<=10:
			data_2.set(f'0{min_}')
			data_1.set(f'00')
		if hr>=10:
			data_2.set(f'{min_}')
			data_1.set(f'00')

def start_func():
	add()
	start['state']='disabled'
def reset_func():
	global sec
	global min_
	global hr
	global data
	global data_1
	global date_2
	sec=0
	min_=0
	hr=0
	data.set('00')
	data_1.set('00')
	data_2.set('00')
	start['state']='active'#active for button.
	root.after_cancel(id_)
root=Tk()
root.title('StopWatch')
root.geometry('315x215')
hr_data=IntVar()
min_data=IntVar()
sec_data=IntVar()
data=IntVar()
data_1=IntVar()
data_2=IntVar()
a=Label(root,text=':',font=('Courier New',50))
b=Label(root,text=':',font=('Courier New',50))
sec_lab=Label(root,textvariable=data,text=sec,font=('Courier',50))
data.set('00')
sec_lab.place(x=230)
min_label=Label(root,textvariable=data_1,text=min_,font=('Courier',50))
data_1.set('00')
min_label.place(x=125)
hr_label=Label(root,textvariable=data_2,text=hr,font=('Courier',50))
data_2.set('00')
hr_label.place(x=15)
stop=Button(root,text='Stop',command=stop_func,font=('Courier',15,'bold'),borderwidth=5,bg='cyan3',fg='white',activeforeground='white',activebackground='cyan3')
stop.place(x=20,y=125)#START STOP RESET
start=Button(root,text='Start',command=start_func,font=('Courier',15,'bold'),borderwidth=5,bg='orange',fg='white',activeforeground='white',activebackground='orange')
start.place(x=115,y=125)
reset=Button(root,text='Reset',command=reset_func,font=('Courier',15,'bold'),borderwidth=5,bg='black',fg='white',activeforeground='white',activebackground='black')
reset.place(x=215,y=125)
a.place(x=200,y=-2)
b.place(x=90,y=-2)
mainloop()
