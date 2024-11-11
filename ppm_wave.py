import numpy as np
"""
     Χρησιμοποείται ο παλμός default_pulse ώστε να υπολογιστεί ο παλμός κάθε ομάδα bit σε μία περίοδο.
p(t)=1, T1<t<T2, else p(t)=0
"""
def default_pulse(t, T1,T2):
    i = np.where( (t >= T1) & (t<T2) )
    x = np.zeros(t.size)
    x[i] = 1
    return x 

def ppm_waveform(k,T,M,p_callable=default_pulse,samples=200):
    # Φτιάχνω ένα διάνυσμα το οποία περιέχει (αριθμό bits)*samples αριθμό χρονικών στιγμών για κάθε ομάδα bit.
    # από 0 έως  (αριθμό bits)* Τ, ώστε να επαρκεί ο χρόνος που χρειάζεται για να χωρέσει 
    # ο κάθε παλμός μέσα σε μία περίοδο. 
    t=np.linspace(0,len(k)*T,len(k)*len(k)*samples+1)
    a=1
    wave=np.zeros(len(t))
    # Εφόσον γνωρίζω πόσα χρονικά στοιχεία αντιστοιχούν σε μία περίοδο TS, χρησιμοποιώ το μέρος του t που αντιστοιχεί στην ομάδα bit που θέλω να μεταδώσω. 
    idx=np.arange((a-1)*len(k)*samples,a*len(k)*samples,1)
    for i in range(0,len(k)):
        # search in this region
        wave[idx]=(p_callable(t[idx],k[a-1]*T/M+(a-1)*T,     (k[a-1]+1)*T/M+(a-1)*T  ))
	# κάθε φορά που αυξάνει το α, μετακινούμε κατά μία περίοδο TS ώστε να μεταδώσω τον επόμενο παλμό.
        a=a+1
        idx=np.arange((a-1)*len(k)*samples,a*len(k)*samples,1)
        
    return t, wave