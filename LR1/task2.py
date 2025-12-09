
n_list=100
n_str=50
n_symb=25
vol_symb=4
volume = 1.44*1024*1024
n_book=volume/(vol_symb*n_symb*n_str*n_list)
print("Количество книг, помещающихся на дискету:", round(n_book))
