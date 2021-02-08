
A = 80000
txA = 3
B = 200000
txB = 1.5
anos = 0

while A < B:
    A += A * txA / 100
    B += B * txB / 100
    anos += 1
    print("{:2d} {:10.2f} {:10.2f}".
          format(anos,A,B))
    
print("Serao necessário(s) {:d} ano(s)".
      format(anos))
    