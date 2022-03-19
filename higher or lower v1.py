import random
game_over = False

search_name = ["'Bir cesedi nasıl saklarım?'", "'Kedimin beni sevmesini nasıl sağlarım?'", "'Lady Gaga bir erkek mi'", "'flört eden kediler'", "'Ona nasıl çıkma teklifi edebilirim'", "'Cinayetten nasıl paçayı kurtarırım'",
               "'Sayısal lotoyu nasıl tuttururum?'", "'İşimden nefret ediyorum!'", "'Bir şeyi nasıl Google'larım?'","'Noel Baba gerçek mi?'","'Erkeklerin neden memesi var?'"]
search_number = [1000, 390, 18000, 110, 15000, 2000, 39000, 22000, 4500, 60500, 18000,]

first_random = random.randrange(0,12)

def game():
    global first_random
    global game_over
    second_random = random.randrange(0,12)
    #bug destroyer
    if first_random == second_random:
        second_random = random.randrange(0,12)
    #bug destroyer
    choice = int(input(f"Bu ay içinde;\n{search_name[first_random]} araması {search_number[first_random]} aranma sayısıyla mı / yoksa {search_name[second_random]} araması mı daha çok yapılmıştır.\n     ilki için 1 / ikinci için 2'ye basınız: "))
    if choice == 1:
        if search_number[first_random] > search_number[second_random]:
            print (f"DOĞRU! \n {search_name[first_random]} araması {search_number[first_random]} kez,{search_name[second_random]} araması {search_number[second_random]} kez yapılmıştır\n\n")
        else:
            print(
                f"Yanlış... \n {search_name[first_random]} araması {search_number[first_random]} kez,{search_name[second_random]} araması {search_number[second_random]} kez yapılmıştır\n\n")
            game_over = True
    elif choice == 2:
        if search_number[second_random] > search_number[first_random]:
            print (f"DOĞRU! \n {search_name[first_random]} araması {search_number[first_random]} kez,{search_name[second_random]} araması {search_number[second_random]} kez yapılmıştır\n\n")
            first_random = second_random
        else:
            print(
                f"Yanlış... \n {search_name[first_random]} araması {search_number[first_random]} kez,{search_name[second_random]} araması {search_number[second_random]} kez yapılmıştır\n\n")
            game_over = True


while game_over == False:
    game()

print ("GAME OVER")

