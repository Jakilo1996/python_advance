import nmap

nm = nmap.PortScanner()
ret = nm.scan('139.224.244.4', '25601')
print(ret)
