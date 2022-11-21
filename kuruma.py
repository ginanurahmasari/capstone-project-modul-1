# Database awal mobil rental
carList = [
    {   
        'Plate' : 'B 612 EMR',
        'Model' : 'Toyota Innova',
        'Transmission' : 'Manual',
        'Color' : 'Hitam',
        'Price' : '800000',
        'Status' : 'Available'
    },
    {   
        'Plate' : 'B 909 NR',
        'Model' : 'Toyota Innova',
        'Transmission' : 'Matic',
        'Color' : 'Silver',
        'Price' : '800000',
        'Status' : 'Available'
    },
    {
        'Plate' : 'B 1105 KN',
        'Model' : 'Toyota Avanza',
        'Transmission' : 'Matic',
        'Color' : 'Putih',
        'Price' : '600000',
        'Status' : 'Available'
    },
    {
        'Plate' : 'B 2301 LT',
        'Model' : 'Toyota Avanza',
        'Transmission' : 'Manual',
        'Color' : 'Hitam',
        'Price' : '600000',
        'Status' : 'Available'
    },
    {
        'Plate' : 'B 2011 HD',
        'Model' : 'Daihatsu Xenia',
        'Transmission' : 'Manual',
        'Color' : 'Silver',
        'Price' : '550000',
        'Status' : 'Available'
    },
    {
        'Plate' : 'B 1402 AL',
        'Model' : 'Daihatsu Xenia',
        'Transmission' : 'Matic',
        'Color' : 'Hitam',
        'Price' : '550000',
        'Status' : 'Available'
    }
]

# Function untuk menampilkan tabel database mobil
def showTable() :
    print ('\n===   Database Mobil Rental   ===\n')
    print ('Index   | Plat Nomor\t| Jenis Mobil \t\t| Transmisi\t| Warna \t| Harga/hari\t| Status')
    for i in range(len(carList)) :
        print('{}\t| {}    \t| {}   \t| {}  \t| {} \t| {}\t| {}'.format(i,carList[i]['Plate'],carList[i]['Model'],carList[i]['Transmission'],carList[i]['Color'],carList[i]['Price'],carList[i]['Status']))

# Data peminjaman mobil
rentalList = []

# Function untuk menampilkan tabel data peminjaman mobil
def showRental() :
    print ('\n===   Data Peminjaman Mobil   ===\n')
    print ('Index   | Nama Peminjam\t| Plat Nomor \t| Jenis Mobil    | Durasi  | Harga/hari | Total Harga  | Status')
    for i in range(len(rentalList)) :
        print('{}\t| {}    \t| {}   \t| {}  | {}\t   | {}     | {}      | {}'.format(i,rentalList[i]['Name'],rentalList[i]['Plate'],rentalList[i]['Model'],rentalList[i]['Days'],rentalList[i]['Price'],rentalList[i]['Total'],rentalList[i]['Status']))

# Password admin
password = 111213

# Function menu login
def login () :
    while True :
        pilih = input('''
    ------------------------------------------------
           Selamat Datang di Kuruma Rent Car!
    ------------------------------------------------
                1 - Admin login
                2 - Exit
    
    Masukan pilihan menu yang ingin dijalankan:
    ''')

        if (pilih == '1') :
            inputPass = int(input('Silakan masukan password admin: '))
            if inputPass == password :
                mainMenu ()
            else :
                print('\n*** Password yang anda masukan salah ***')
        elif (pilih == '2') :
            print('''
                Anda telah keluar dari program  
                  ***   Terima kasih   ***
            ''')
            break
        else :
            print('\n*** Input salah, silakan masukan angka sesuai pilihan ***')

# Function main menu
def mainMenu () :
    while True :
        pilihMenu = input('''
        --------------------------------------------------
                Kuruma Rent Car Database System
        --------------------------------------------------
                1 - Menu tampilkan database mobil
                2 - Menu tambah data mobil
                3 - Menu perbarui data mobil
                4 - Menu hapus data mobil
                5 - Menu peminjaman mobil
                6 - Menu pengembalian mobil
                7 - Exit
        
        Masukan pilihan menu yang ingin dijalankan: 
        ''')

        if (pilihMenu == '1') :
            read()
        elif (pilihMenu == '2') :
            create()
        elif (pilihMenu == '3') :
            update()
        elif (pilihMenu == '4') :
            delete()
        elif (pilihMenu == '5') :
            rent()
        elif (pilihMenu == '6') :
            kembali()
        elif (pilihMenu == '7') :
            print('''
                Anda telah keluar dari program  
                  ***   Terima kasih   ***
            ''')
            exit()
        else :
            print('\n*** Input salah, silakan masukan angka sesuai pilihan ***')

# Function untuk menu tampilkan database mobil
def read() :
    while True :
        pilih1 = input('''
        --------------------------------------------
                Menu tampilkan database mobil
        --------------------------------------------
              1 - Tampilkan semua data mobil
              2 - Tampilkan sesuai kategori
              3 - Cari berdasarkan plat nomor
              4 - Kembali ke main menu

        Masukan pilihan menu yang ingin dijalankan: 
        ''')

        if (pilih1 == '1') :
            if len(carList) != 0 :
                showTable()
            else :
                print ('\n***  Tidak ada data mobil  ***')
                continue
        elif (pilih1 == '2') :
            if len(carList) != 0 :
                inputKategori = input('''
                Pilihan kategori :
                    1. Jenis Mobil
                    2. Transmisi
                    3. Warna
                    4. Status peminjaman
                Masukan kategori yang ingin ditampilkan: 
                ''')
                if (inputKategori == '1') :
                    inputJenis = input('\n Masukan jenis mobil yang ingin ditampilkan: ').title()
                    print ('\n===   Database Mobil Rental   ===\n')
                    print ('Index   | Plat Nomor\t| Jenis Mobil \t\t| Transmisi\t| Warna \t| Harga/hari\t| Status')
                    count = 0
                    for i in range(len(carList)) :
                        if inputJenis == carList[i]['Model'] :
                            print('{}\t| {}    \t| {}   \t| {}  \t| {} \t| {}\t| {}'.format(i,carList[i]['Plate'],carList[i]['Model'],carList[i]['Transmission'],carList[i]['Color'],carList[i]['Price'],carList[i]['Status']))
                        elif inputJenis != carList[i]['Model'] :
                            count += 1
                            if count == len(carList) :
                                print ('\n***  Tidak ada data mobil ***')   
                elif (inputKategori == '2') :
                    inputTransmisi = input('\n Masukan transmisi mobil yang ingin ditampilkan: ').title()
                    print ('\n===   Database Mobil Rental   ===\n')
                    print ('Index   | Plat Nomor\t| Jenis Mobil \t\t| Transmisi\t| Warna \t| Harga/hari\t| Status')
                    count = 0
                    for i in range(len(carList)) :
                        if inputTransmisi == carList[i]['Transmission'] :
                            print('{}\t| {}    \t| {}   \t| {}  \t| {} \t| {}\t| {}'.format(i,carList[i]['Plate'],carList[i]['Model'],carList[i]['Transmission'],carList[i]['Color'],carList[i]['Price'],carList[i]['Status']))
                        elif inputTransmisi != carList[i]['Transmission'] :
                            count += 1
                            if count == len(carList) :
                                print ('\n***  Tidak ada data mobil ***')   
                elif (inputKategori == '3') :
                    inputWarna = input('\n Masukan warna mobil yang ingin ditampilkan: ').title()
                    print ('\n===   Database Mobil Rental   ===\n')
                    print ('Index   | Plat Nomor\t| Jenis Mobil \t\t| Transmisi\t| Warna \t| Harga/hari\t| Status')
                    count = 0
                    for i in range(len(carList)) :
                        if inputWarna == carList[i]['Color'] :
                            print('{}\t| {}    \t| {}   \t| {}  \t| {} \t| {}\t| {}'.format(i,carList[i]['Plate'],carList[i]['Model'],carList[i]['Transmission'],carList[i]['Color'],carList[i]['Price'],carList[i]['Status']))
                        elif inputWarna != carList[i]['Color'] :
                            count += 1
                            if count == len(carList) :
                                print ('\n***  Tidak ada data mobil ***')  
                elif (inputKategori == '4') :
                    inputStatus = input('\n Masukan status mobil yang ingin ditampilkan: ').title()
                    print ('\n===   Database Mobil Rental   ===\n')
                    print ('Index   | Plat Nomor\t| Jenis Mobil \t\t| Transmisi\t| Warna \t| Harga/hari\t| Status')
                    count = 0
                    for i in range(len(carList)) :
                        if inputStatus == carList[i]['Status'] :
                            print('{}\t| {}    \t| {}   \t| {}  \t| {} \t| {}\t| {}'.format(i,carList[i]['Plate'],carList[i]['Model'],carList[i]['Transmission'],carList[i]['Color'],carList[i]['Price'],carList[i]['Status']))
                        elif inputStatus != carList[i]['Status'] :
                            count += 1
                            if count == len(carList) :
                                print ('\n***  Tidak ada data mobil ***')  
                else :
                    print('\n*** Input salah, silakan masukan angka sesuai pilihan ***\n')      
            else :
                print ('\n***  Tidak ada data mobil ***')
        elif (pilih1 == '3') :
            inputPlat = input('\n Masukkan plat nomor mobil yang ingin ditampilkan: ').upper()
            print ('\n===   Database Mobil Rental   ===\n')
            print ('Index   | Plat Nomor\t| Jenis Mobil \t\t| Transmisi\t| Warna \t| Harga/hari\t| Status')
            count = 0
            for i in range(len(carList)) :
                if inputPlat == carList[i]['Plate'] :
                    print('{}\t| {}    \t| {}   \t| {}  \t| {} \t| {}\t| {}'.format(i,carList[i]['Plate'],carList[i]['Model'],carList[i]['Transmission'],carList[i]['Color'],carList[i]['Price'],carList[i]['Status']))
                elif inputPlat != carList[i]['Plate'] :
                    count += 1
                    if count == len(carList) :
                        print ('\n***  Tidak ada data mobil  ***')
                        continue   
        elif (pilih1 == '4') :
            break
        else :
            print('\n*** Input salah, silakan masukan angka sesuai pilihan ***')

# Function untuk menu tambah data mobil
def create() :
    while True :
        pilih2 = input('''
        --------------------------------------------
                 Menu tambah data mobil
        --------------------------------------------
                1 - Tambah data mobil
                2 - Kembali ke main menu

        Masukan pilihan menu yang ingin dijalankan: 
        ''')

        if (pilih2 == '1') :
            while True :
                newPlate = input('Masukan plat nomor mobil yang ingin ditambahkan:  ').upper()
                for i in range(len(carList)) :
                    if carList[i]['Plate'] == newPlate :
                        print ('\n***  Data sudah ada  ***')
                        break
                else :
                    print('\n*** Silakan masukan data mobil yang akan ditambahkan ***')
                    newModel = input('Masukan jenis mobil: ').title()
                    newTrans = input('Masukan jenis transmisi mobil: ').capitalize()
                    newColor = input('Masukan warna mobil: ').capitalize()
                    newPrice = int(input('Masukan harga sewa per hari: '))
                    while True :
                        checker = input('Apakah Anda yakin akan menyimpan data ini? (ya/tidak) ').lower()
                        if checker == 'ya' :
                            carList.append ({
                            'Plate' : newPlate,
                            'Model' : newModel,
                            'Transmission' : newTrans,
                            'Color' : newColor,
                            'Price' : newPrice,
                            'Status' : 'Available'        
                            })
                            showTable()
                            print ('\n***  Data berhasil disimpan  ***')
                            break
                        elif checker == 'tidak' :
                            showTable()
                            print ('\n***  Data tidak disimpan  ***')
                            break
                        else :
                            print('\n*** Input salah, silakan masukan ya/tidak ***\n')
                break            
        elif (pilih2 == '2') :
            mainMenu()
        else :
            print('\n*** Input salah, silakan masukan angka sesuai pilihan ***')

# Function untuk menu perbarui data mobil
def update() :
    while True :
        pilih3 = input('''
        --------------------------------------------
                 Menu perbarui data mobil
        --------------------------------------------
                1 - Perbarui data mobil
                2 - Kembali ke main menu

        Masukan pilihan menu yang ingin dijalankan: 
        ''')

        if (pilih3 == '1') :
            plateNum = input('\n Masukan plat nomor mobil yang ingin diperbarui: ').upper()
            count = 0
            for i in range(len(carList)) :
                if plateNum == carList[i]['Plate'] :
                    print ('\n===   Database Mobil Rental   ===\n')
                    print ('Index   | Plat Nomor\t| Jenis Mobil \t\t| Transmisi\t| Warna \t| Harga/hari\t| Status')
                    print('{}\t| {}    \t| {}   \t| {}  \t| {} \t| {}\t| {}'.format(i,carList[i]['Plate'],carList[i]['Model'],carList[i]['Transmission'],carList[i]['Color'],carList[i]['Price'],carList[i]['Status']))
                    while True :
                        checker = input('Apakah Anda yakin akan memperbarui data ini? (ya/tidak) ').lower()
                        if checker == 'ya' :
                            inputKategori = input('''
                            Pilih kategori yang akan diperbarui:
                            1. Plat Nomor
                            2. Jenis Mobil
                            3. Transmisi
                            4. Warna
                            5. Harga sewa
                            Masukan kategori yang dipilih:
                            ''')
                            if (inputKategori == '1') :
                                newPlat = input('\n Masukan plat mobil yang akan diperbarui: ').upper()
                                while True :
                                    checker = input('Apakah Anda yakin akan menyimpan data ini? (ya/tidak) ').lower()
                                    if checker == 'ya' :
                                        carList[i]['Plate'] = newPlat
                                        showTable()
                                        print ('\n***  Data telah disimpan  ***')
                                        break
                                    elif checker == 'tidak' :
                                        showTable()
                                        print ('\n***  Data tidak disimpan  ***')
                                        break
                                    else :
                                        print('\n*** Input salah, silakan masukkan ya/tidak ***') 
                            if (inputKategori == '2') :
                                newJenis = input('\n Masukan jenis mobil yang akan diperbarui: ').title()
                                while True :
                                    checker = input('Apakah Anda yakin akan menyimpan data ini? (ya/tidak) ').lower()
                                    if checker == 'ya' :
                                        carList[i]['Model'] = newJenis
                                        showTable()
                                        print ('\n***  Data telah disimpan  ***')
                                        break
                                    elif checker == 'tidak' :
                                        showTable()
                                        print ('\n***  Data tidak disimpan  ***')
                                        break
                                    else :
                                        print('\n*** Input salah, silakan masukkan ya/tidak ***')
                            if (inputKategori == '3') :
                                newTransmisi = input('\n Masukan jenis transmisi yang akan diperbarui: ').title()
                                while True :
                                    checker = input('Apakah Anda yakin akan menyimpan data ini? (ya/tidak) ').lower()
                                    if checker == 'ya' :
                                        carList[i]['Transmission'] = newTransmisi
                                        showTable()
                                        print ('\n***  Data telah disimpan  ***')
                                        break
                                    elif checker == 'tidak' :
                                        showTable()
                                        print ('\n***  Data tidak disimpan  ***')
                                        break
                                    else :
                                        print('\n*** Input salah, silakan masukkan ya/tidak ***\n')
                            if (inputKategori == '4') :
                                newColor = input('\n Masukan warna mobil yang akan diperbarui: ').title()
                                while True :
                                    checker = input('Apakah Anda yakin akan menyimpan data ini? (ya/tidak) ').lower()
                                    if checker == 'ya' :
                                        carList[i]['Color'] = newColor
                                        showTable()
                                        print ('\n***  Data telah disimpan  ***')
                                        break
                                    elif checker == 'tidak' :
                                        showTable()
                                        print ('\n***  Data tidak disimpan  ***')
                                        break
                                    else :
                                        print('\n*** Input salah, silakan masukan ya/tidak ***')
                            if (inputKategori == '5') :
                                newPrice = input('\n Masukan harga sewa mobil yang akan diperbarui: ').title()
                                while True :
                                    checker = input('Apakah Anda yakin akan menyimpan data ini? (ya/tidak) ').lower()
                                    if checker == 'ya' :
                                        carList[i]['Price'] = newPrice
                                        showTable()
                                        print ('\n***  Data telah disimpan  ***')
                                        break
                                    elif checker == 'tidak' :
                                        showTable()
                                        print ('\n***  Data tidak disimpan  ***')
                                        break
                                    else :
                                        print('\n*** Input salah, silakan masukan ya/tidak ***')
                            break
                        elif checker == 'tidak' :
                            showTable()
                            print ('\n***  Data tidak diperbarui  ***')
                            break
                        else :
                            print('\n*** Input salah, silakan masukan ya/tidak ***\n')
                elif plateNum != carList[i]['Plate'] :
                    count += 1
                    if count == len(carList) :
                        print ('\n***  Tidak ada data mobil  ***')
        elif (pilih3 == '2') :
            break
        else :
            print('\n*** Input salah, silakan masukan angka sesuai pilihan ***')

# Function untuk menu hapus data mobil
def delete() :
    while True :
        pilih4 = input('''
        --------------------------------------------
                 Menu hapus data mobil
        --------------------------------------------
                1 - Hapus data mobil
                2 - Kembali ke main menu

        Masukan pilihan menu yang ingin dijalankan: 
        ''')

        if (pilih4 == '1') :
            plateNum = input('\n Masukan plat nomor mobil yang ingin dihapus: ').upper()
            count = 0
            for i in range(len(carList)) :
                if plateNum == carList[i]['Plate'] :
                    print ('\n===   Database Mobil Rental   ===\n')
                    print ('Index   | Plat Nomor\t| Jenis Mobil \t\t| Transmisi\t| Warna \t| Harga/hari\t| Status')
                    print('{}\t| {}    \t| {}   \t| {}  \t| {} \t| {}\t| {}'.format(i,carList[i]['Plate'],carList[i]['Model'],carList[i]['Transmission'],carList[i]['Color'],carList[i]['Price'],carList[i]['Status']))
                    while True :
                        checker = input('Apakah Anda yakin akan menghapus data ini? (ya/tidak) ').lower()
                        if checker == 'ya' :
                            del carList[i]
                            showTable()
                            print ('\n***  Data berhasil dihapus  ***')
                            delete()
                        elif checker == 'tidak' :
                            showTable()
                            print ('\n***  Data tidak dihapus  ***')
                            delete()
                        else :
                            print('\n*** Input salah, silakan masukan ya/tidak ***\n')
                elif plateNum != carList[i]['Plate'] :
                    count += 1
                    if count == len(carList) :
                        print ('\n***  Tidak ada data mobil  ***')     
        elif (pilih4 == '2') :
            mainMenu()
        else :
            print('\n*** Input salah, silakan masukan angka sesuai pilihan ***')

# Function untuk menu peminjaman mobil
def rent() :
    while True :
        pilih5 = input('''
        --------------------------------------------
                  Menu peminjaman mobil
        --------------------------------------------
            1 - Tampilkan data peminjaman mobil
            2 - Tambah data peminjaman mobil
            3 - Pembayaran peminjaman mobil
            4 - Kembali ke main menu

        Masukan pilihan menu yang ingin dijalankan: 
        ''')

        if (pilih5 == '1') :
            if len(rentalList) != 0 :
                showRental()
            else :
                print ('\n***  Tidak ada data peminjaman mobil  ***')
        elif (pilih5 == '2') :
            while True :
                showTable()
                inputPlate = input('Masukan plat nomor mobil yang akan dipinjam:  ').upper()
                count = 0
                for i in range(len(carList)) :
                    if carList[i]['Plate'] == inputPlate :
                        print('\n*** Silakan masukan data peminjaman yang akan ditambahkan ***')
                        inputName = input('Nama peminjam:  ').title()
                        inputModel = carList[i]['Model']
                        inputDays = int(input('Durasi peminjaman (hari): '))
                        inputPrice = int(carList[i]['Price'])
                        inputTotal = inputDays * inputPrice
                        while True :
                            checker = input('Apakah Anda yakin akan menyimpan data ini? (ya/tidak) ').lower()
                            if checker == 'ya' :
                                rentalList.append ({
                                'Name' : inputName,
                                'Plate' : inputPlate,
                                'Model' : inputModel,
                                'Days' : inputDays,
                                'Price' : inputPrice,
                                'Total' : inputTotal,
                                'Status' : 'Belum Lunas'       
                                })
                                carList[i]['Status'] = 'Rented'
                                showRental()
                                print ('\n***  Data berhasil disimpan  ***')
                                break
                            elif checker == 'tidak' :
                                showRental()
                                print ('\n***  Data tidak disimpan  ***')
                                break
                            else :
                                print('\n*** Input salah, silakan masukkan ya/tidak ***\n')
                    elif inputPlate != carList[i]['Plate'] :
                        count += 1
                        if count == len(carList) :
                            print ('\n***  Tidak ada data mobil  ***')
                            break
                break
        elif (pilih5 == '3') :
            if len(rentalList) != 0 :
                showRental()
                inputPay = input('\n Masukan plat nomor mobil yang akan dibayar: ').upper()
                count = 0
                for i in range(len(rentalList)) :
                    if inputPay == rentalList[i]['Plate'] :
                        model = rentalList[i]['Model']
                        durasi = rentalList[i]['Days']
                        harga = rentalList[i]['Price']
                        total = int(rentalList[i]['Total'])
                        print('\n*** Detail Pembayaran ***')
                        print(f'{model} : {durasi} x {harga} = {total}')
                        while True :
                            bayar = int(input('\nMasukan jumlah uang : '))
                            if(bayar == total):
                                rentalList[i]['Status'] = 'Lunas'
                                showRental()
                                print('\n*** Pembayaran lunas! ***')
                                break
                            elif(bayar < total):
                                kurang = total - bayar
                                print(f'\nUang kurang sebesar {kurang}')
                            elif(bayar > total):
                                lebih = bayar - total
                                rentalList[i]['Status'] = 'Lunas'
                                showRental()
                                print(f'\nUang kembalian : {lebih}')
                                print('\n*** Pembayaran lunas! ***')
                                break
                    elif inputPay != rentalList[i]['Plate'] :
                        count += 1
                        if count == len(rentalList) :
                                print ('\n***  Tidak ada data peminjaman mobil ***')  
            else :
                print ('\n***  Tidak ada data peminjaman mobil  ***')
        elif (pilih5 == '4') :
            mainMenu()
        else :
            print('\n*** Input salah, silakan masukan angka sesuai pilihan ***')

# Function untuk menu pengembalian mobil
def kembali() :
    while True :
        pilih6 = input('''
        --------------------------------------------
                  Menu pengembalian mobil
        --------------------------------------------
            1 - Pengembalian mobil
            2 - Kembali ke main menu

        Masukan pilihan menu yang ingin dijalankan: 
        ''')

        if (pilih6 == '1') :
            if len(rentalList) != 0 :
                showRental()
                inputPlat = input('Masukan plat nomor mobil yang akan dikembalikan:  ').upper()
                count = 0
                for i in range(len(rentalList)) :
                    if rentalList[i]['Plate'] == inputPlat :
                        if rentalList[i]['Status'] == 'Lunas' :
                            while True :
                                checker = input('Apakah Anda yakin akan mengembalikan mobil ini? (ya/tidak) ').lower()
                                if checker == 'ya' :
                                    del rentalList[i]
                                    showRental()
                                    print ('\n***  Mobil telah dikembalikan  ***')
                                    for i in range(len(carList)) :
                                        if carList[i]['Plate'] == inputPlat :
                                            carList[i]['Status'] = 'Available'
                                            kembali()
                                elif checker == 'tidak' :
                                    showRental()
                                    print ('\n***  Mobil tidak dikembalikan  ***')
                                    break
                                else :
                                    print('\n*** Input salah, silakan masukan ya/tidak ***\n')
                        else :
                            print('\n*** Tagihan belum lunas, mohon lakukan pembayaran ***')
                    elif rentalList[i]['Plate'] != inputPlat :
                        count += 1
                        if count == len(rentalList) :
                            print ('\n***  Tidak ada data mobil  ***')
            else :
                print ('\n***  Tidak ada data peminjaman mobil  ***')
        elif (pilih6 == '2') :
            mainMenu()
        else :
            print('\n*** Input salah, silakan masukan angka sesuai pilihan ***')

# Memanggil menu awal
login()