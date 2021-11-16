# variable1
slipGaji = "PT. XYZ"
garis = '------------------'
namaPegawai1 = "Ahmad"
agama = "Islam"
jumlahAnak = 2
gaji_pokok = 4000000
tunjangan_jabatan = 20/100
tunjangan_keluarga = 10/100
gaji_kotor = gaji_pokok + 800000 + 400000
zakat_profesi = gaji_kotor - 2.5/100
take_home_pay = gaji_pokok + 800000 + 400000
# variable2
namaPegawai2 = "Alex"
agama2 = "Kristen Protestan"
jumlahAnak2 = 5
gaji_Pokok2 = 6000000
tunjangan_jabatan2 = 20/100
tunjangan_keluarga2 = 20/100
gaji_kotor2 = gaji_Pokok2 + 1200000 + 1200000 
zakat_profesi2 = gaji_kotor2 - 0
take_home_pay2 = gaji_Pokok2 + 1200000 + 1200000 - 0 
# pegawai1
if gaji_pokok < 400000:
    tunjangan_jabatan = gaji_pokok * (20/100)
else:
    tunjangan_jabatan = gaji_pokok * (20/100)

if gaji_pokok < 400000:
    tunjangan_keluarga = gaji_pokok * (10/100)
else:
    tunjangan_keluarga = gaji_pokok * (10/100)

if gaji_kotor < 5200000:
    zakat_profesi = gaji_kotor * (2.5/100)
else:
    zakat_profesi = gaji_kotor * (2.5/100)
# pegawai2
if gaji_Pokok2 < 600000:
    tunjangan_jabatan2 = gaji_Pokok2 * (20/100)
else:
    tunjangan_jabatan2 = gaji_Pokok2 * (20/100)

if gaji_Pokok2 < 600000:
    tunjangan_keluarga2 = gaji_Pokok2 * (20/100)
else:
    tunjangan_keluarga2 = gaji_Pokok2 * (20/100)

if gaji_kotor2 < 6400000:
    zakat_profesi2 =  0
else:
    zakat_profesi2 =  0

# print pegawai1
print("SLIP GAJI",slipGaji,
"\n",garis,
"\nNama Pegawai\t\t\t:",namaPegawai1,
"\nAgama\t\t\t\t:",agama,
"\nJumblah Anak\t\t\t:",jumlahAnak,
"\nGaji Pokok\t\t\t:", gaji_pokok)

tunjangan_jabatan = gaji_pokok + tunjangan_jabatan
print('tunjangan jabatan               : {}'.format(int(tunjangan_jabatan)))

tunjangan_keluarga = gaji_pokok + tunjangan_keluarga
print('tunjangan keluarga              : {}'.format(int(tunjangan_keluarga)))

gaji_kotor = gaji_pokok + 400000 + 800000
print('gaji kotor                      : {}'.format(int(gaji_kotor)))

zakat_profesi = gaji_kotor - zakat_profesi
print('zakat profesi                   : {}'.format(int(zakat_profesi)))

take_home_pay = gaji_pokok + 400000 + 800000 - 130000
print('take_home_pay                   : {}'.format(int(take_home_pay)))
# print pegawai2
print("\nSLIP GAJI",slipGaji,
"\n",garis,
"\nNama Pegawai\t\t\t:",namaPegawai2,
"\nAgama\t\t\t\t:",agama2,
"\nJumlah Anak\t\t\t:",jumlahAnak2,
"\nGaji Pokok\t\t\t:",gaji_Pokok2)

tunjangan_jabatan2 = gaji_Pokok2 + tunjangan_jabatan2
print('tunjangan jabatan               : {}'.format(int(tunjangan_jabatan2)))

tunjangan_keluarga2 = gaji_Pokok2 + tunjangan_keluarga2
print('tunjangan keluarga              : {}'.format(int(tunjangan_keluarga2)))

gaji_kotor2 = gaji_Pokok2 + 1200000 + 1200000 
print('gaji kotor                      : {}'.format(int(gaji_kotor2)))

zakat_profesi2 =  0
print('zakat profesi                   : {}'.format(int(zakat_profesi2)))

take_home_pay2 = gaji_Pokok2 + 1200000 + 1200000 - 0
print('take_home_pay                   : {}'.format(int(take_home_pay2)))
