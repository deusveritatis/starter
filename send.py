import paramiko


def log(ip):
	cli = paramiko.SSHClient()
	cli.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		cli.connect(hostname=ip,username='iiserb',password='iiserb',timeout=1)
		ftp = cli.open_sftp()
		path1 = '/home/iiserb/.local/mech'                 #path in host
		path = '/home/iiserb/.cache/mech'                  #path in remote
		ftp.put(path1,path)
		ftp.close()
		cli.close()
		print('done')
	except Exception as e:
		print('Connection failed!!')



ip1 = ['172.28.123.'+str(i) for i in range(1,120)]
ip2 = ['172.28.154.'+str(i) for i in range(1,60)]
ip3 = ['172.28.155.'+str(i) for i in range(1,46)]
ip4 = ['172.28.122.'+str(i) for i in range(1,80)]
ips=ip1+ip2+ip3+ip4
for ip in ips:
	print(ip)
	log(ip)
