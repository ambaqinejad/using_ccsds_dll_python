import ctypes
import os

p = r'C:\Users\ambaqinejad\PycharmProjects\using_ccsds_dll'
dll_path = r'C:\Users\ambaqinejad\PycharmProjects\using_ccsds_dll\libCCSDS.dll'

os.add_dll_directory(p)

ccsds = ctypes.CDLL("libCCSDS.dll")
#
# # Define function return and argument types
# ccsds.create_packet.restype = ctypes.c_void_p
# ccsds.create_packet.argtypes = [ctypes.c_void_p]
# ccsds.destroy_packet.argtypes = [ctypes.c_void_p]
# ccsds.parse_packet.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint8), ctypes.c_int]
# ccsds.print_packet.argtypes = [ctypes.c_void_p]
#
# # Create a CCSDS packet instance
# packet = ccsds.create_packet()
#
# # Sample raw data (at least 6 bytes)
# raw_data = bytearray([0x08, 0x00, 0x01, 0x02, 0x00, 0x05, 0xAB, 0xCD, 0xEF])
#
# # Convert python bytearray to ctypes array
# raw_data_c = (ctypes.c_uint8 * len(raw_data))(*raw_data)
#
# # Parse packet
# ccsds.parse_packet(packet, raw_data_c, len(raw_data))
#
# # Print parsed packet
# ccsds.print_packet(packet)
#
# # Clean up
# ccsds.destroy_packet(packet)
import struct
print(struct.calcsize("P") * 8)  # Outputs 32 or 64 depending on the Python bit version
