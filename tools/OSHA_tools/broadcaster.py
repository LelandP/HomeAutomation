from socket import *


def broadcast_msg(msg, port):
	"""
	"""
	s=socket(AF_INET, SOCK_DGRAM)
	s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
	s.sendto(msg,('255.255.255.255', port))

def listen_and_wait(port):
	"""
	"""
	s=socket(AF_INET, SOCK_DGRAM)
	s.bind(('0.0.0.0',port))
	m = None
	while m is None:
		m=s.recvfrom(1024)
	return m