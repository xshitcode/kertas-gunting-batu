import random as r
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choose = input('''
Selamat datang dipermainan Kertas gunting batu
Pilih
1. Batu
2. Kertas
3. Gunting  
''')
print()

game = [rock, paper, scissors]
randomCpu = r.randint(0, len(game) - 1)
x = int(choose) - 1

if x < 0 or x >= 3:
  print("PILIHAN TIDAK TERSEDIA")
else:  
  print("Anda memilih \n" + game[x])
  print("Komputer memilih \n" + game[randomCpu])
  print()
  if game[randomCpu] == rock and game[x] == rock:
    print("Seri")
  elif game[randomCpu] == rock and game[x] == paper:
    print("Anda Menang")
  elif game[randomCpu] == rock and game[x] == scissors:
    print("Anda Kalah")
  elif game[randomCpu] == paper and game[x] == rock:
    print("Anda Kalah")
  elif game[randomCpu] == paper and game[x] == paper:
    print("Seri")
  elif game[randomCpu] == paper and game[x] == scissors:
    print("Anda Menang")
  elif game[randomCpu] == scissors and game[x] == rock:
    print("Anda Menang")
  elif game[randomCpu] == scissors and game[x] == paper:
    print("Anda Kalah")
  elif game[randomCpu] == scissors and game[x] == scissors:
    print("Seri")
  else:
    print("Error")