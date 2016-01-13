# ASCII Marching Squares

## Description

Marching Squares is the 2D variant of the Marching Cubes algorithm.
This tool is a marching squares for binary values, specified in an ascii file.

The output is a tiling of a primitive set.
The primitive set contains sixteen cases, as defined by the SW (bit0), SE (bit1), NW (bit2) and NE (bit3) quadrants.

A sample primitive set that can be used:

![t0](t0.png "0x0")
![t1](t1.png "0x1")
![t2](t2.png "0x2")
![t3](t3.png "0x3")
![t4](t4.png "0x4")
![t5](t5.png "0x5")
![t6](t6.png "0x6")
![t7](t7.png "0x7")
![t8](t8.png "0x8")
![t9](t9.png "0x9")
![ta](ta.png "0xa")
![tb](tb.png "0xb")
![tc](tc.png "0xc")
![td](td.png "0xd")
![te](te.png "0xe")
![tf](tf.png "0xf")

When combined with the input...
```
XXXXXXXXXXXXXXXX
XX-----X----XXXX
XXXX-X---X----XX
XXXX-X---XXXX--X
X-XX--------X--X
X-XX--XXX--XXX-X
X--X---X----X--X
X--XXXXX--XXXX-X
X--X---X-----X-X
X------XXXX--X-X
X-XXXXXXXXX--X-X
X---X--XXXX--X-X
X-XXX---XX---X-X
X-----------XXXX
X--------XXXXX-X
XXXXXXXXXXXXXXXX
```

...the following output image will be assembled:
![output](output.png "output")

## Requirements

You require python3 installation in /usr/bin/python3

You need to have Imagemagick 'convert' and 'display' tools installed, and accessible in path.

## Usage

```
./ams map0.txt
```

