num_id = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(num_id)
while True:
    link_a = int(input("enter first numbers"))
    link_b = int(input("enter second numbers"))
    for i in range(len(num_id)):
        if num_id[i] == num_id[link_a]:
            num_id[i] = num_id[link_b]
    print(num_id)
