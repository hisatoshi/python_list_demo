#coding:utf-8
#python3.4.3で動作
#python2系列は動かないと思う
#使い方：コマンドライン引数を適当に



import sys
import time
import random

def speedDemo() :
    input = [x for x in range(9999999)]

    startTime=time.time()
    outputFor=[]
    for x in input :
        outputFor.append(x)

    rapTimeFor=time.time()

    outputList = [x for x in input]
    rapTimeList = time.time()

    print("for文を回した場合 ： "+str(rapTimeFor-startTime))
    print("リスト内包表記の場合 ： "+str(rapTimeList-rapTimeFor))



def _pulse2Func(x) :
	return x+2
def exsampleOfMap() :
	input = [1,2,3,4]
	output0 = [x+2 for x in input]
	output1 = [_pulse2Func(x) for x in input]

	print(output0)
	print(output1)

def _upper2Func(x) :
	return x >2
def exsampleOfFilter() :
	input = [1,2,3,4]
	output0 = [x for x in input if x > 2]
	output1 = [x for x in input if _upper2Func(x)]

	print(output0)
	print(output1)

def exsampleOfMapAndFilter() :
	input = [1,2,3,4]
	output = [x+2 for x in input if x > 2]

	print(output)


def doubleRoop() :
	input = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
	output0=[]
	for subInput in input :
		for x in subInput :
			output0.append(x)

	output1=[x for subInput in input for x in subInput]

	print(output0)
	print(output1)

def ifelse() :
	input=[1,2,3,4,5,6]
	output0=[]
	for i in input :
		x=i-2
		if(x < 0) :
			output0.append(0)
		else :
			output0.append(x)
	output1 = [x-2 if x-2>0 else 0 for x in input]

	print(output0)
	print(output1)


def hutatsu() :
	input0=[0,1,2,3,4]
	input1=[5,6,7,8]
	output=[[x0, x1] for x0,x1 in zip(input0, input1)]

	print(output)

def makeList() :

	a=[[0]*3]*3
	b=[[0 for i in range(3)] for j in range(3)]

	print(a)
	print(b)

	a[0][0]=1
	b[0][0]=1

	print(a)
	print(b)


def setVer() :
	input={1,2,3,4,5}
	output={x for x in input}
	print(output)

def setKantan() :
	input = [1,1,1,2,3,4,5]
	output = list(set(input))
	print(output)

def yarisugi() :
	input0 = [1,2,3,4,5,6,7,8,9,10]
	input1 = [11,12,13,14,15,16,17,18,19,20]

	_input0=[]
	for i in input0 :
		if i%2==0 :
			_input0.append(i)
	_input1=[]
	for i in input1 :
		if i%2==0 :
			_input1.append(i)
	output=[]
	for i, j in zip(_input0, _input1) :
		c = i+j
		if(c >15) :
			output.append(c)
		else :
			output.append(0)
	print(output)

	output = [x+y if x+y>15 else 0 for x,y in zip([i for i in input0 if i%2==0],[j for j in input1 if j%2==0])]
	print(output)

def dictNaihou() :
	input = ["tarou", "jirou", "saburou", "shirou"]
	output = {name : index for index, name in enumerate(input)}
	print(output)

def myHash(name) :
	return random.randint(1,100)

def dictHash() :
	input = ["tarou", "jirou", "saburou", "shirou"]
	output = {myHash(name) : name for name in input}
	print(output)

def speed2() :
	input = [x for x in range(9999999)]

	startTime = time.time()
	output0=[]
	for i in input :
		output0.append(i)
	
	rapTime1 = time.time()

	output1=[]
	appendObject = output1.append
	for i in input :
		appendObject(i)

	rapTime2 = time.time()

	output2 = [x for x in input]

	rapTime3 = time.time()


	print("普通のfor文"+str(rapTime1-startTime))
	print("リスト内包表記を使用"+str(rapTime3-rapTime2))
	print("いい感じにしたやつ"+str(rapTime2-rapTime1))

def runDemo(index) :
	if(index == 0) :
		speedDemo()
	elif(index == 1) :
		exsampleOfMap()
	elif(index == 2) :
		exsampleOfFilter()
	elif(index == 3) :
		exsampleOfMapAndFilter()
	elif(index == 4) :
		doubleRoop()
	elif(index==5) :
		ifelse()
	elif(index==6) :
		hutatsu()
	elif(index==7) :
		makeList()
	elif(index==8) :
		setVer()
	elif(index==9) :
		setKantan()
	elif(index==10) :
		dictNaihou()
	elif(index==11) :
		dictHash()
	elif(index==12) :
		yarisugi()
	elif(index==13) :
		speed2()




if __name__ == '__main__' :
	if(len(sys.argv) < 2) :
		print("数字を選択してください")
	else :
		runDemo(int(sys.argv[1]))

