#!/usr/bin/python3

import sys
import os

if len( sys.argv ) != 2 :
	print( "Usage: %s intput.txt" % ( sys.argv[ 0 ], ) )
	sys.exit( 1 )

f = open( sys.argv[ 1 ], 'r' )

lines = [ x.strip() for x in f.readlines() ]
h = len( lines )
w = len( lines[0] )

print( "Input dimensions: %dx%d" % ( w, h ) )

h -= 1
w -= 1


vcmd = "convert "
for y in range( h ) :
	hcmd = "convert "
	for x in range( w ) :
		l0 = lines[ y+1 ]
		l1 = lines[ y+0 ]
		b0 = l0[x+0] == 'X'
		b1 = l0[x+1] == 'X'
		b2 = l1[x+0] == 'X'
		b3 = l1[x+1] == 'X'
		v = 0
		v += 1 if b0 else 0
		v += 2 if b1 else 0
		v += 4 if b2 else 0
		v += 8 if b3 else 0
		hcmd += ( "t%x.png " % ( v, ) )
	hcmd += ( "+append row%02d.png " % ( y, ) )
	os.system( hcmd )
	vcmd += ( "row%02d.png " % ( y, ) )
vcmd += " -append output.png "
os.system( vcmd )
os.system( "display output.png" )

