from cuaca import provinsi
from cuaca import ramalan

print("Ramalan Cuaca\n")
print("List Provinsi:")
provinsi.read_provinsi()
print("")

while(True):
    while(True):
        try:
            user_input=int(input("Masukan nomor provinsi: "))
        except ValueError:
            print("Mohon menginput angka")
        else: 
            if user_input > 34:
                print("Melebihi batas list provinsi") 
            else:
                urutan_kota, nama_provinsi, nama_ibukota = provinsi.get_provinsi_from_user(user_input)
                print("Pilihan:")
                print("1. Masukan nama kota yang ingin diketahui cuacanya yang ada di Provinsi "+nama_provinsi)
                print("2. Biarkan default(Ibukota Provinsi)")
                while(True):
                    try:
                        user_input_pilihan_cuaca=int(input("Masukan nomor pilihan: "))
                    except ValueError:
                        print("Mohon menginput angka")
                    else:
                        if user_input_pilihan_cuaca > 2:
                            print("Melebihi batas pilihan")
                        else:
                            if user_input_pilihan_cuaca == 1:
                                user_input_kota = input("Masukan nama kota:")
                                ramalan.get_weather_report(nama_provinsi, user_input_kota)      

                            elif user_input_pilihan_cuaca == 2:
                                ramalan.get_weather_report(nama_provinsi,nama_ibukota)
                            
                            print("Apakah ingin melanjutkan?")
                            print("[1]Ya \t [2]Tidak")
                            while(True):
                                try:
                                    user_input_lanjut=int(input("Lanjut?: "))
                                    break
                                except ValueError:
                                    print("Mohon menginput angka")
                                else:
                                    break
                            if user_input_lanjut == 1:
                                print("List Provinsi:")
                                provinsi.read_provinsi()
                                print("")
                                break
                            elif user_input_lanjut == 2:
                                quit()

