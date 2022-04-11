banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
bank_name=open("bankname","w")
bank_name.write("")
for i in banks_list:
     bank_name.write(""+ i+"\n")
bank_name.close()