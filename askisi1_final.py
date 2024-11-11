import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfcinv


# Υπολογίζω το SNRdb χρησιμοποιώντας την erfcinv της βιβλιοθήκης 
def SNRdb(M,Pb):
    a=np.sqrt(2)*erfcinv(Pb*M*np.log2(M)/(M-1))
    SNR=np.power(a,2)*(np.power(M,2)-1)/6/np.log2(M)
    return 10*np.log10(SNR)

# Το τελευταίο ψηφίο του ΑΜ
last_digit=9;

# Πιθανότητα σφάλματος Pb
P=1/np.power(10,(last_digit+2))
print('Pb=',P)

# Υπολογίζω τις δυνάμεις του 2^m και τις αποθηκεύω στη μεταβλητή M
M = [np.power(2,i) for i in range(1, 10+1)]
print('M=',M,'\n');

# Καλώ τη συνάρτηση για τον υπολογισμό του SNRdb για τις διάφορες τιμές Μ και P, και τις 
# αποθηκεύω στη λίστα SNr 
SNr=[SNRdb(x,P) for x in M ]

# Γραφικές των αποτελεσμάτων
plt.plot(M, SNr,linestyle = 'solid')  
plt.title(" Γραφική παράσταση πηλίκου σήματος-προς- θόρυβο ανά-bit SNR$_b$ συναρτήσει της τάξης του PAM  ",fontsize=7)
plt.ylabel("$SNR_{db}$") 
plt.xlabel("M")
plt.grid()

plt.savefig('snr.png', dpi='figure')
plt.show()
