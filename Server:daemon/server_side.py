 #!/usr/bin/env python
 # -*- coding: utf-8 -*-

#This program read the data from the serial connection, save the data and send alerts to
#the configured email.


import glob, os, serial, sys, time



##Start the serial connection with arduino
class SerialConnection:

	def __init__(self):

		if os.name == 'nt':
			##Windows stuff
			self.serialPort = glob.glob("COM*")[0]
			print serialPort
		if os.name == 'posix':
			## Unix stuff
			self.serialPort = glob.glob("/dev/tty.usbmodem*")[0]
			print self.serialPort
		else:
			print "Error Arduino not found"

		self.speed = 57600

def main():

	serialConnection = SerialConnection()
	ser = serial.Serial(serialConnection.serialPort, serialConnection.speed) 
	response =''

	while True:
		nb = raw_input('Choose a letter')
		if nb=='q':
			print("Exit program")
			sys.exit()
		ser.write(nb)
		time.sleep(0.1)
		while ser.inWaiting()>0:
			response += ser.read()
		print response
		response = ''
		#Data analysis thread and alert system
		try:
			thread.start_new_thread (dataAnalysys, response ) #TODO create data analysis
		except:
			print "Unable to start data analysis and alert thread"



if __name__ == '__main__':
	main()



		