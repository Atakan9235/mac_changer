import subprocess
import optparse

def arguments():
    parser=optparse.OptionParser()
    parser.add_option("-i","--interface",dest="interface",help="mac arayuz")
    parser.add_option("-m","--mac",dest="new_mac",help="yeni adress ekle")
    return parser.parse_args()

def macchanger(interface,macaddr):

	subprocess.call(["ifconfig",interface,"down"])
	subprocess.call(["ifconfig",interface,"hw","ether",macaddr])
	subprocess.call(["ifconfig",interface,"up"])

	print "[+] mac adre değişiyor %s suna %s"%(interface,macaddr)


(options,arguments)=arguments()
macchanger(options.interface,options.new_mac)
