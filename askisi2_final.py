import commlib as cl2
import ppm_wave as ppm
import numpy as np
import matplotlib.pyplot as plt
M=2
TS=1/1e+11

name='Maria Kollia'

""" Βήμα 1ο
    Η συνάρτηση δέχεται το ονοματεπώνυμο στα αγγλικά, χωρίζει το string σε χαρακτήρες.
    Στη συνέχεια, κάθε χαρακτήρας μετατρέπεται σε μία σειρά από 8bits.
"""

def str_to_bits_array(str):
    binary = ''.join(format(ord(i), '08b') for i in str)
    return np.array( [ int(x) for x in binary ] ).astype(int)


"""
Βήμα 2ο: 
        Σε περίπτωση όπου στην τελευταία ομάδα bits που μεταδίδουμε απομένουν λιγότερα
        από bits συμπληρώνουμε μηδενικά bits ώστε να έχουμε bits.
"""


def pad_zeroes(bits_array,M):
    if len(bits_array)%np.log2(M)>0:
        add_zeros=np.log2(M)-len(bits_array)%np.log2(M)
        bits_array=np.pad(bits_array,(0, int(add_zeros)), mode='constant', constant_values=0)
        
    return bits_array
        

    

binary_name=str_to_bits_array(name)
bits=pad_zeroes(binary_name,M)

# Μετατροπή των bits σε σύμβολα gray για τον υπολογισμό της κυματομορφές M-PPM και ομαδοποίηση κατά log2(M) bits.
 
fmap=cl2.pam_gray_forward_map(M)
symbols, bitgroups = cl2.bits_to_symbols(bits, fmap, return_bits = True)
print('Bit groups:')
print(bitgroups)
print('Encoded symbols:')
print(symbols)
    
 #Υπολογισμός κυματομορφής μέσω της συνάρτησης ppm_waveform από το αρχείο ppm.py
t, x = ppm.ppm_waveform(symbols, TS,M)

############ Αποθήκευση Διαγράμματος ########
cl2.plot_pam(t, x, M, bits, TS, dy = 1, plot_type = '-')

plt.title("M=%i" %M,loc='right') 
plt.rc('font', size=6)
figure = plt.gcf() # get current figure
figure.set_size_inches(14, 10)
plt.savefig("M"+str(M)+".png", dpi = 200)
plt.show()
