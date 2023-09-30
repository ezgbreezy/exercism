data = [
        (([40, 39, 95, 80, 25, 31, 70, 55, 40, 90], 98), []),
        (([88, 29, 91, 64, 78, 43, 41, 77, 36, 50], 80), [88, 91]),
        (([100, 89], 100), [100]),
        (([88, 29, 91, 64, 78, 43, 41, 77, 36, 50], 78), [88, 91, 78]),
        (([], 80), [])]

for variant, (params, result) in enumerate(data, start=1):
    error_message = f'Expected: {result} but the number of scores above the threshold is incorrect.'
    print(f"Variant: {variant}, Param: {params}, Result: {result}")
