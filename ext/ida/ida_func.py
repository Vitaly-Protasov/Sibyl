from idautils import *
ea = ScreenEA()
addresses = {}
for funcea in Functions(SegStart(ea), SegEnd(ea)):
	addresses[funcea]=1
	#print "Function %s at 0x%x" % (GetFunctionName(funcea), funcea)

	#for ref in CodeRefsTo(funcea, 1):
		#addresses[ref]=1
		#print " called from %s(0x%x)" % (GetFunctionName(ref), ref)

#for addr in addresses:
#	print "0x%x" % addr
print("Have found %d addresses" % len(addresses))

path = str(idc.GetInputFilePath())
filename = "%s_output.txt" % (path).split("/")[len((path).split("/")) - 1]

with open(filename, 'w') as f:
    for addr in addresses:
	#print "0x%x" % addr
        f.write(str("0x%x\n" % addr))

print("_output.txt at the same folder as binary")
