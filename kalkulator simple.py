#fungsi penjumlahan
def add(x,y):
  return x + y
#fungsi pengurangan
def substract(x,y):
  return x - y
#fungsi perkalian
def multiply(x,y):
  return x * y
#fungsi pembagian
def divide(x,y):
  return x / y
  
#menu operasi
print("pilih operasi")
print("1.Penjumlahan")
print("2.pengurangan")
print("3.perkalian")
print("4.pembagian")

#meminta input dr pengguna

choice = input("masukan pilihan (1,2,3,4): "
)
num1 = int(input("masukan bilangan pertama :"))
num2 = int(input("masukan bilangan kedua :"))

if choice == "1":
   print(num1, "+" ,num2, "=" ,add(num1,num2))
 
elif choice == "2":
   print(num1, "-" ,num2, "=" ,substract(num1,num2))
  
elif choice == "3" :
   print(num1, "*" ,num2, "=" ,multiply(num1,num2))
 
elif choice == "4" :
   if num2 != 0:
       print(num1, "/" ,num2, "=" ,divide(num1,num2))
   else:
       print("pembagian pake nol gadibolehin bos")
 
else:
   print("salah input cui")
  


  


  



 
 