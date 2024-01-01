list_provinsi = ["Aceh","Sumatera Utara",
"Sumatera Barat","Riau","Kepulauan Riau",
"Jambi","Sumatera Selatan","Bangka Belitung",
"Bengkulu","Lampung","DKI Jakarta","Banten",
"Jawa Barat","Jawa Tengah","DI Yogyakarta",
"Jawa Timur","Bali","Nusa Tenggara Barat","Nusa Tenggara Timur",
"Kalimantan Barat","Kalimantan Tengah","Kalimantan Selatan",
"Kalimantan Timur","Kalimantan Utara","Sulawesi Utara","Gorontalo",
"Sulawesi Tengah","Sulawesi Barat","Sulawesi Selatan","Sulawesi Tenggara",
"Maluku","Maluku Utara","Papua Barat","Papua"]

list_provinsi_ibukota = ["Banda Aceh","Medan","Padang","Pekanbaru","Tanjungpinang",
"Jambi","Palembang","Pangkal Pinang","Bengkulu","Bandar Lampung","Jakarta",
"Serang","Bandung","Semarang","Yogyakarta","Surabaya","Denpasar",
"Mataram","Kupang","Pontianak","Palangkaraya","Banjarmasin"," Samarinda",
"Tanjung Selor","Manado","Gorontalo","Palu","Mamuju",
"Makassar","Kendari","Ambon","Sofifi","Manokwari","Jayapura"]

def read_provinsi():
    for i in range(len(list_provinsi)):
        print(str(i+1)+". "+list_provinsi[i])

def get_provinsi_from_user(provinsi):
    for i in range(len(list_provinsi)):
        if i==provinsi-1:
           #print(i, list_provinsi[i],"-",list_provinsi_ibukota[i])
           return i,list_provinsi[i],list_provinsi_ibukota[i]
