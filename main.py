import TorFirefox
import PdfCompressor
import watchdogg
import os

import multiprocessing

def main():
	
	startWatchdog()


	##############################################################
	#	update the file_path with the pdf path to be compressed.  #
	# 	Include the multiprocessing part when importing this file#
	#	in your code 											 #
	##############################################################

	dir_path = os.path.dirname(os.path.realpath(__file__))
	file_path = dir_path + "/" + "h2.pdf"

	if os.path.isfile(file_path):
		Compress(file_path)
	else:
		print file_path,"file dont exists"


def Compress(file_path):
	browser = TorFirefox.getFirefoxBrowser()
	url = 'http://pdfcompressor.com/'
	browser.get(url)

	PdfCompressor.compressPDF(browser, file_path)
	print " ||||||| pdf = ", file_path, "uploaded ||||||||||"

	
	flag = PdfCompressor.downloadCompPDF(browser)
	## and unzipping it in the current folder
	# print os.getcwd()
	if(flag): #flag1 =0 when there is no fle to be downloaded
		print os.getcwd()
		TorFirefox.unzipFile(os.getcwd()+"/pdfcompressor.zip",os.getcwd())
		os.remove(os.getcwd()+"/pdfcompressor.zip")
		print "file compressed ! "

	#close the browser after doint all the shit
	TorFirefox.closeBrowser(browser)

def watchdog():
	### running daemon that checks if the file is downoaded completely or not
	w = watchdogg.Watcher()
	w.run()

def startWatchdog():
	'''
	### below updation is necessary in order to open watchdog
	coz after the last step is done (prev run) the file is updated to "DONE"
	and this same string is also required to close watchdog after all unzipping is done
	'''
	with open('/home/gugli/Documents/script_py/PdfCompressor/checkDownStatus.txt','w') as outFile:
			outFile.write("blah")


	p1 = multiprocessing.Process(name='p1', target=watchdog)
	p1.start()
	# p2 = multiprocessing.Process(name='p', target=sud)
	# p2.start()

if __name__ == "__main__":
	main()