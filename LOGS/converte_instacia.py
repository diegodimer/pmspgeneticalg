import sys
import numpy as np
def main():
        f = open(sys.argv[1],"r")
        if f.mode == "r":
                contents = f.readlines()
#                print(contents[4])
                linha = contents[4].split(" ")
#                print(linha[0])
#                '(linha[1])
        f.close()
        line=0
	
        f = open(sys.argv[2],"w+")

        f.write("data;\n\n")
        f.write("set K :=\n")
        for i in range(int(contents[1])):
                f.write("\t%d\n" %(i+1))

        f.write(";\n\n")
        f.write("set I :=\n")
        for i in range(int(contents[2])+1):
                f.write("\t%d\n" %(i))
        f.write(";\n\n")
        f.write("set J :=\n")
        for i in range(int(contents[2])):
                f.write("\t%d\n" %(i+1)) 
        f.write(";\n\n")

        f.write("param P :=\n")
        line=4
        for i in range(int(contents[2])):
                numero = contents[line].split(" ")
                line = line + 1
                for j in range(int(contents[1])):
                        f.write("\t%d %d %d\n" %(i+1,j+1,int(numero[j])))

        f.write(";\n\n")

        matriz_s = np.empty((int(contents[1]),int(contents[2]),int(contents[2])))
        matriz_s[0][0][1] = 2
        for i in range(int(contents[1])):
                line = line + 1
                for j in range(int(contents[2])):
#                        print(contents[line])
                        numero = contents[line].split(" ")
                        line = line + 1
                        for k in range(int(contents[2])):
#                                print(numero[k]+"\n")
                                matriz_s[i][j][k] = int(numero[k])

        
        f.write("param S :=\n")
        for k in range(int(contents[2])+1):
                for i in range(int(contents[2])):
                        for j in range(int(contents[1])):
                                if k==0:
                                        f.write("\t%d %d %d 0\n" %(k,i+1,j+1))
                                else:
                                        f.write("\t%d %d %d %d\n" %(k,i+1,j+1,matriz_s[j][k-1][i]))
        f.write(";\n\n")
        f.write("end;\n")


        f.close()
if __name__ == "__main__":
	main()
