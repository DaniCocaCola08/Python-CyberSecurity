from socket import *
import time

startTime = time.time()

if __name__ == '__main__':
    target = input("Enter host for scanning: ")
    t_IP = gethostbyname(target)
    porta1 = int(input('Defina o intervalo de portas. Porta1:'))
    porta2 = int (input('Porta2: '))
    
    print('Scanneando o host: ', t_IP)

    for i in range (porta1, (porta2 + 1)):
        s = socket(AF_INET, SOCK_STREAM)

        conn = s.connect_ex((t_IP, i))
        if (conn == 0):
            print ('Porta %d: ABERTA' % (i,))
        s.close()

tempoTotal = time.time() - startTime

print ('Tempo total: ', time.time() - startTime)