genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


def get_melon_best_album(genre_array, play_array):
    # 구현해보세요!
    music_dic = {}
    music_dic_info = {}
    result = []

    for n in range(len(genre_array)):
        if genre_array[n] not in music_dic:
            music_dic[genre_array[n]] = play_array[n]
            music_dic_info[genre_array[n]] = [[n,play_array[n]]]
        else :
            music_dic[genre_array[n]] += play_array[n]
            music_dic_info[genre_array[n]].append([n,play_array[n]])

    sorted_music_dic = sorted(music_dic.items(),key = lambda item: item[1],reverse = True)

    for a in sorted_music_dic:
        sorted_music = sorted(sorted(music_dic_info[a[0]]),key=lambda item:item[1],reverse = True)
        result.append(sorted_music[0][0])
        result.append(sorted_music[1][0])

    return result


print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!