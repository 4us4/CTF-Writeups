import binascii
n = int('0b100001001010100010010000101111101000011010101000100011001111011011010000110100101100100011001000110010101101110001011010110110101100101011100110111001101100001011001110110010100101101011010010110111000101101011001000110100101100110011001100110010101110010011001010110111001110100001011010110011001101111011011100111010001110011001011100110111001101001011000110110010101111101', 2) 
print binascii.unhexlify('%x' % n)