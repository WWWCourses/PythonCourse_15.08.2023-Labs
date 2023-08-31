try:

    target_volume = int(input("Въведете обема, който искате да прелеете (от 10 до 9999 литра): "))


    if 10 <= target_volume <= 9999:
        count_bucket_2 = 0
        count_bucket_3 = 0

        current_bucket_2 = 0
        current_bucket_3 = 0

        while current_bucket_2 != target_volume and current_bucket_3 != target_volume:

            transferred = min(current_bucket_2, 3 - current_bucket_3)
            current_bucket_2 -= transferred
            current_bucket_3 += transferred
            count_bucket_2 += 1


            transferred = min(current_bucket_3, 2 - current_bucket_2)
            current_bucket_3 -= transferred
            current_bucket_2 += transferred
            count_bucket_3 += 1


        if current_bucket_2 == target_volume:
            print(f"За да прелеете {target_volume} литра вода, трябва да пълните кофата с 2 литра {count_bucket_2} пъти и кофата с 3 литра {count_bucket_3} пъти.")
        else:
            print(f"За да прелеете {target_volume} литра вода, трябва да пълните кофата с 3 литра {count_bucket_3} пъти и кофата с 2 литра {count_bucket_2} пъти.")
    else:
        print("Грешка! Въведете валиден обем.")
except ValueError:
    print("Грешка! Въведете числова стойност.")