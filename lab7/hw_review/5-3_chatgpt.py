def fill_buckets(target_volume):
    bucket_2 = 0
    bucket_3 = 0
    steps = 0

    while bucket_2 != target_volume and bucket_3 != target_volume:
        if bucket_2 == 0:
            bucket_2 = 2
        elif bucket_3 == 3:
            bucket_3 = 0
        else:
            space_left_in_bucket_3 = 3 - bucket_3
            if bucket_2 <= space_left_in_bucket_3:
                bucket_3 += bucket_2
                bucket_2 = 0
            else:
                bucket_2 -= space_left_in_bucket_3
                bucket_3 = 3

        steps += 1

    return steps, bucket_2, bucket_3

def main():
    target_volume = int(input("Въведете обема на цистерната: "))
    steps, remaining_bucket_2, remaining_bucket_3 = fill_buckets(target_volume)

    if remaining_bucket_2 == target_volume:
        print(f"Целта е постигната след {steps} пъти с пълнене на кофа от 2 литра.")
    else:
        print(f"Целта е постигната след {steps} пъти с пълнене на кофа от 3 литра.")
        if remaining_bucket_2 > 0:
            print(f"Допълнително е необходима една кофа от 2 литра.")

if __name__ == "__main__":
    main()
