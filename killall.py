import paramiko
import sys

def log(ip):
	cli = paramiko.SSHClient()
	cli.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		cli.connect(hostname=ip,username='iiserb',password='iiserb',timeout=1)
		_,out3,error3 = cli.exec_command(' killall systemd; killall sysmdn  &> /dev/null')
		cli.close()
	except Exception as e:
		print('Connection failed!!')


ip = ['172.28.123.'+str(i) for i in range(1,115)]
ip2 = ['172.28.154.'+str(i) for i in range(1,60)]
ip3 = ['172.28.155.'+str(i) for i in range(1,46)]
ip4 = ['172.28.122.'+str(i) for i in range(1,90)]
ips = ip+ip3+ip2+ip4
for ip in ips:
	print(ip)
	log(ip)

