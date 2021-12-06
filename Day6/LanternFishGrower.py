def expand_fish(fish_list, days):
    fish_dict = convert_to_dict(fish_list)
    for day in range(days):
        new_dict = {i: 0 for i in range(9)}
        for i in range(0, 8):
            new_dict[i] = fish_dict[i+1]
        new_dict[6] += fish_dict[0]
        new_dict[8] += fish_dict[0]
        print(fish_dict)
        fish_dict = new_dict
    return sum([fish_dict[key] for key in fish_dict.keys()])

def convert_to_dict(fish_list):
    output = {i: 0 for i in range(9)}
    for i in fish_list:
        output[i] += 1
    print(output)
    return output



