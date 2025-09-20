listmenu=['shop','bar','gacha']

welcome=input('halo selamat datang di RPG Text Based\nKetik "MENU"')
welcome=welcome.lower()
welcomeS=welcome.split()
if welcomeS == "menu":
    menu=input('[Menu]\n\n[Shop]\n[Bar]\n[Gacha]')
    # if menu == 'shop':
    #     shop=input('halo selamat datang di toko, apa yang ingin kamu beli?\n\n[Pedang] [Perisai]\n[Ramuan Penyembuh]  [Ramuan Mana]\n[Peliharaan]  [Token Gacha]')
    #     shop=shop.lower()
    #     if shop == 'pedang':
    #         kategoripedang=input('[Pedang kayu ☆]\n[Pedang batu ☆]\n[Pedang perunggu ☆☆]\n[Pedang tembaga ☆☆☆]\n[Pedang emas ☆☆☆☆]\n[Pedang Besi]\n[Pedang diamond ☆☆☆☆☆]')
    #         if kategoripedang == 'pedang kayu':
    #             pedangkayu=input('Berapa banyak yang ingin kamu beli?')
    #             if pedangkayu <=1 and <= 100:
    #                 print(f'Ini {pedangkayu} pedangmu :3 (jangan digunakan untuk hal yang tidak-tidak ya..)')
    #             else:
    #                 print('tidak memenuhi syarat batas minimal dan maksimal pembelian')
    #         if kategoripedang == 'pedang batu':
    #             pedangbatu=0
    #             while pedangbatu <=1 and <=100:
    #                 print('ini pedang batumu')

if welcomeS == "bar":
    bar=input('selamat datang di bar.Tolong tunjukan kartu identitasmu, apakah kamu memilikinya?\n[iya]     [tidak]')
    bar=bar.lower()
    if bar == "iya" or "1":
        insidebar=input("Selamat datang di Bar kami, kamu bisa melakukan kegiatan dari istirahat, beli makan dan minum, atau dugem dengan mbak mbaknya ;)\n[Beli minum]\n[Beli makan]\n[Dugem]\n[Judi]\n[istirahat]")
        insidebar=insidebar.lower()
        if insidebar== "beli minum" or "1":
            beliminum=input('hai, namaku Bele, aku penjual minuman alkohol terbaik dikota ini, mau beli?\n[Cocktail cap elang merah]\n[whiskiy (real)]\n[air berapi]\n[air keras (esbatu isinya) ]\n[cocktail without a tail in it]\n[kencing anime]')
            beliminum=beliminum.lower()
            


            #cocktail cap elang, whiskiy real, air berapi, air keras, cocktail tanpa tail, kencing anime