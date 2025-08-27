def take_magic_damage(health, resist, amp, spell_power):
    print(health)
    magic_damage = (amp * spell_power) - resist
    print(magic_damage)
    health = health - magic_damage
    print(health)
    return health

def unlock_achievement(before_xp, ach_xp, ach_name):
    after_xp = before_xp + ach_xp
    print("After xp: ", after_xp)
    alert = "Achievement Unlocked: " + ach_name
    print(alert)
    return after_xp, alert

def binary_search(target, arr):
    #Sorted already so start in the middle of the list
    if len(arr) == 0:
        return False
    end = len(arr) - 1
    start = 0
    #Sticking point
    while start <= end:
        mid = (end + start) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            end = mid - 1
        elif arr[mid] < target:
            start = mid + 1
    return False

def count_names(list_of_lists, target_name):
    count_names = 0
    for list in list_of_lists:
        count_names += list.count(target_name)
    return count_names
            
print("test to get things checked in github")

def split_players_into_teams(players):
    even_players = players[::2]
    #Two :: to get to the end of the list before the stepper
    odd_players = players[1::2]
    return even_players, odd_players

def merge(dict1, dict2):
    merge_dict = {}
    for key in dict1:
        merge_dict[key] = dict1[key]
    for key in dict2:
        merge_dict[key] = dict2[key]
    return merge_dict