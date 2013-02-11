#!/usr/bin/python
import subprocess

def init():
	compilec = ['/usr/bin/gcc', 'runner.c', '-o', 'runner','-lm']
	subprocess.call(compilec)

def compilerun(filename,errfile,inputfile,outputfile,memlimit,timelimit):
	dotpos = filename.find(".")
	language=filename[dotpos+1:]
	compileerror=False
	fo = open(errfile,'w')
	if ( language == 'c' ):
		try:
			compilec = ['/usr/bin/gcc','-lm', '-W', filename]
			subprocess.call(compilec,stderr=fo)
			
			with open(errfile, 'r') as error_file:
				error = error_file.read()
			if not error:
				print "Compiled " + filename + " successfully"
				runc = ['./runner', 'a.out', '--input='+inputfile, '--output='+outputfile, '--mem='+memlimit, '--time='+timelimit]
				subprocess.call(runc,stderr=fo)
			else:
				compileerror=True
			
		except Exception as e:
			print e
			pass
	
	elif (language == 'cpp'):
		try:
			compilecpp = ['/usr/bin/g++','-lm','-w', filename]
			subprocess.call(compilecpp,stderr=fo)
			with open(errfile, 'r') as error_file:
				error = error_file.read()
			if not error:
				print "Compiled " + filename + " successfully"
				runcpp = ['./runner', 'a.out', '--input='+inputfile, '--output='+outputfile, '--mem='+memlimit, '--time='+timelimit]
				subprocess.call(runcpp)
			else:
				compileerror=True
		except Exception as e:
			print e
			pass
			
	elif (language == 'py'):
		try:
			#the py file has to have this line at the top: #!/usr/bin/python
			subprocess.call(['chmod','a+x',filename])
			runpy = ['./runner', filename, '--input='+inputfile, '--output='+outputfile, '--mem='+memlimit, '--time='+timelimit]
			
			subprocess.call(runpy,stderr=fo)
			
		except Exception as e:
			print e
			pass
			
	fo.close()
	with open(errfile, 'r') as error_file:
		if compileerror==False:
			error = error_file.read()
		else:
			error='CERR	'+error_file.read()
			#print error
		
	with open(outputfile, 'r') as output_file:
		output = output_file.read()
	
	#print output
	return error,output
		
init()
compilerun("hello.py","err.txt","input.txt","output.txt","200000000","2.0")
			

