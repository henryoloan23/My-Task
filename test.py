def selisih_waktu(jam1, menit1, jam2, menit2):
    if menit1 < menit2:
        menit2 += 60
        jam1 -= 1
        
    selisihMenit = menit2 - menit1
    selisihJam = jam2 - jam1
    
    return selisihJam, selisihMenit

def main():
    jam1 = int(input('Masukkan jam mulai = '))
    menit1 = int(input('Masukkan menit mulai = '))
    jam2 = int(input('Masukkan jam selesai = '))
    menit2 = int(input('Masukkan menit selesai = '))
    
    jam, menit = selisih_waktu(jam1, menit1, jam2, menit2)
    print(f"selisih waktu diantara kedua waktu tersebut adalah {jam} jam dan {menit} menit")
    
while True:
    userInput = input('Halo user apakah kamu ingin menghitung (Y/N) ? : ')
    
    if (userInput == 'Y'):
        main()
    else:
        break

    

