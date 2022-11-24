from django.shortcuts import render
from movies.models import Movie
from movies.models import VoteMovie
from django.contrib.auth import get_user_model


import math
from collections import defaultdict
# Create your views here.

user_genre_weight = []


def sim_msd(name1, name2):
    # name1: 유저 데이터 셋
    # name2: 순회 무비 데이터
    sum = 0
    count = 0
    for genres in name1:
        if genres in name2 :
            sum += pow(name1[genres]- name2[genres], 2)
            count += 1
    if count == 0 :
        return 0
    else:
        return 1 / (1+(sum/count))


## ! 본 장르에 따라 가중치 부여해서 추가하기

def sim_cosine(name1, name2):
    global user_genre_weight
    sum_name1 = 0
    sum_name2 = 0
    sum_name1_name2 = 0
    count = i = 0
    for genres in name1:
        if genres in name2:
            sum_name1 += pow(name1[genres], 2) * user_genre_weight[i]
            sum_name2 += pow(name2[genres], 2) * user_genre_weight[i]
            sum_name1_name2 += name1[genres]*name2[genres] * user_genre_weight[i]
        i += 1
    if math.sqrt(sum_name1)*math.sqrt(sum_name2) != 0:
        return sum_name1_name2 / (math.sqrt(sum_name1)*math.sqrt(sum_name2))
    else: 
        return 0    

# def sim_pearson(name1, name2):
#     global user_genre_weight
#     avg_name1 = 0
#     avg_name2 = 0
#     count = 0

#     for genres in name1:
#         if genres in name2:
#             avg_name1 += name1[genres]
#             avg_name2 += name2[genres]
#             count += 1

#     if count != 0:
#         avg_name1 = avg_name1 / count
#         avg_name2 = avg_name2 / count
        
#     sum_name1 = 0
#     sum_name2 = 0
#     sum_name1_name2 = 0
#     count = i = 0
#     for genres in name1:
#         if genres in name2:
#             sum_name1 += pow(name1[genres] - avg_name1, 2) * user_genre_weight[i]
#             sum_name2 += pow(name2[genres] - avg_name2, 2) * user_genre_weight[i]
#             sum_name1_name2 += (name1[genres] - avg_name1) * (name2[genres] - avg_name2) * user_genre_weight[i]
#             print(name1[genres], avg_name1, name2[genres], avg_name2)
#         i += 1
#     if math.sqrt(sum_name1) * math.sqrt(sum_name2) != 0:
#         return sum_name1_name2 / (math.sqrt(sum_name1) * math.sqrt(sum_name2))
#     else :
#         return 0

# def top_match(data, name, index=3, sim_function=sim_pearson):
#     li = []
#     for i in data:
#         if name != i:
#             li.append((sim_function(data,name,i),i))

def entropy(name1, name2):
    sum_entropy = 0
    name2_lengh = len(name2)
    for genres in name1:
        if genres in name2:
            sum_entropy -= math.log(float(name2[genres]))
    return sum_entropy/name2_lengh

def index(request, user_pk) :
    # movies = Movie.objects.all()
    movies1990s = Movie.objects.filter(release_date__range=(0,1999))
    movies2000s = Movie.objects.filter(release_date__range=(2000,2010))
    movies2010s = Movie.objects.filter(release_date__range=(2010,2050))

    # print(movies1990s)
    # print(movies2000s)
    # print(movies2010s)

    movies1990s_rating = defaultdict(int)
    movies2000s_rating = defaultdict(int)
    movies2010s_rating = defaultdict(int)

    user_movie_genres = defaultdict(int)
    user_movie_centries = defaultdict(int)
    user_movie_centries[2010] += 1
    user_movie_centries[2000] += 1
    user_movie_centries[1990] += 1
    user_movie_rankings = defaultdict(int)
    user_movie_rankings_avg = defaultdict(int)

    # 쿼리셋
    get_user_votes = VoteMovie.objects.filter(like_users = user_pk)
    
    # 유저에 대한 기본 데이터 정리
    for get_user_vote in get_user_votes:

        user_vote_year = int(get_user_vote.like_movies.release_date[0:4])
        if user_vote_year >= 2010:
            user_movie_centries[2010] += 1
        elif user_vote_year <= 2000:
            user_movie_centries[1990] += 1
        else:
            user_movie_centries[2000] += 1

        # 장르 출력
        sub_stack = ''
        user_vote = get_user_vote.vote
        get_user_vote_movie_genres = [] 
        for g in get_user_vote.like_movies.genres:
            if g.isalpha():
                sub_stack += g
            elif sub_stack:
                get_user_vote_movie_genres.append(sub_stack)
                sub_stack = ''
        
        # 본 영화는 제외한 데이터 조회
        movies1990s = movies1990s.exclude(pk=get_user_vote.like_movies.pk)
        movies2000s = movies2000s.exclude(pk=get_user_vote.like_movies.pk)
        movies2010s = movies2010s.exclude(pk=get_user_vote.like_movies.pk)

        # 유저의 별점에 따른 모델 생성
        for genre in get_user_vote_movie_genres:
            user_movie_genres[genre] += 1
            user_movie_rankings[genre] += int(user_vote)
            user_movie_rankings_avg[genre] = user_movie_rankings[genre]/user_movie_genres[genre]
    # 영화 별 데이터 셋 정렬
    for m in movies1990s:
        sub_stack = ''
        m_genres = []
        sub_dic = {}
        for g in m.genres:
            if g.isalpha():
                sub_stack += g
            elif sub_stack:
                m_genres.append(sub_stack)
                sub_stack = ''
        for genre in m_genres:
            sub_dic[genre] = m.vote_average/2
        movies1990s_rating[m.pk] = sub_dic

    for m in movies2000s:
        sub_stack = ''
        m_genres = []
        sub_dic = {}
        for g in m.genres:
            if g.isalpha():
                sub_stack += g
            elif sub_stack:
                m_genres.append(sub_stack)
                sub_stack = ''
        for genre in m_genres:
            sub_dic[genre] = m.vote_average/2
        movies2000s_rating[m.pk] = sub_dic

    for m in movies2010s:
        sub_stack = ''
        m_genres = []
        sub_dic = {}
        for g in m.genres:
            if g.isalpha():
                sub_stack += g
            elif sub_stack:
                m_genres.append(sub_stack)
                sub_stack = ''
        for genre in m_genres:
            sub_dic[genre] = m.vote_average/2
        movies2010s_rating[m.pk] = sub_dic

    # print(movies1990s_rating)
    # print(movies2000s_rating)
    # print(movies2010s_rating)

    movies1990s_result = defaultdict(int)
    movies2000s_result = defaultdict(int)
    movies2010s_result = defaultdict(int)

    global user_genre_weight
    for i, v in user_movie_genres.items():
        user_genre_weight.append(v/sum(user_movie_genres.values()))
    # for i, v in user_movie_genres.items():
    #     user_genre_weight.append( 1 / ( 1 + math.exp(-v/sum(user_movie_genres.values()))))
    
    # msd
    # for name2_pk, name2_value in movies1990s_rating.items():
    #     movies1990s_result[name2_pk] = sim_msd(user_movie_rankings_avg, name2_value)
    # sorted_dict1990s = sorted(movies1990s_result.items(), key = lambda item: item[1], reverse = True)

    # for name2_pk, name2_value in movies2000s_rating.items():
    #     movies2000s_result[name2_pk] = sim_msd(user_movie_rankings_avg, name2_value)
    # sorted_dict2000s = sorted(movies2000s_result.items(), key = lambda item: item[1], reverse = True)

    # for name2_pk, name2_value in movies2010s_rating.items():
    #     movies2010s_result[name2_pk] = sim_msd(user_movie_rankings_avg, name2_value)
    # sorted_dict2010s = sorted(movies2010s_result.items(), key = lambda item: item[1], reverse = True)


    # 코사인 유사도
    for name2_pk, name2_value in movies2010s_rating.items():
        movies2010s_result[name2_pk] = sim_cosine(user_movie_rankings_avg, name2_value)
    sorted_dict2010s = sorted(movies2010s_result.items(), key = lambda item: item[1], reverse = True)

    for name2_pk, name2_value in movies2000s_rating.items():
        movies2000s_result[name2_pk] = sim_cosine(user_movie_rankings_avg, name2_value)
    sorted_dict2000s = sorted(movies2000s_result.items(), key = lambda item: item[1], reverse = True)

    for name2_pk, name2_value in movies1990s_rating.items():
        movies1990s_result[name2_pk] = sim_cosine(user_movie_rankings_avg, name2_value)
    sorted_dict1990s = sorted(movies1990s_result.items(), key = lambda item: item[1], reverse = True)


    # 피어슨 유사도 검색
    # for name2_pk, name2_value in movies2010s_rating.items():
    #     movies2010s_result[name2_pk] = sim_pearson(user_movie_rankings_avg, name2_value)
    # sorted_dict2010s = sorted(movies2010s_result.items(), key = lambda item: item[1], reverse = True)

    # for name2_pk, name2_value in movies2000s_rating.items():
    #     movies2000s_result[name2_pk] = sim_pearson(user_movie_rankings_avg, name2_value)
    # sorted_dict2000s = sorted(movies2000s_result.items(), key = lambda item: item[1], reverse = True)

    # for name2_pk, name2_value in movies1990s_rating.items():
    #     movies1990s_result[name2_pk] = sim_pearson(user_movie_rankings_avg, name2_value)
    # sorted_dict1990s = sorted(movies1990s_result.items(), key = lambda item: item[1], reverse = True)
    
    
    # 엔트로피 가중치
    # for name2_pk, name2_value in movies2010s_rating.items():
    #     movies2010s_result[name2_pk] = entropy(user_movie_rankings_avg, name2_value)
    #     sorted_dict2010s = sorted(movies2010s_result.items(), key = lambda item: item[1], reverse = True)

    # for name2_pk, name2_value in movies2000s_rating.items():
    #     movies2000s_result[name2_pk] = entropy(user_movie_rankings_avg, name2_value)
    # sorted_dict2000s = sorted(movies2000s_result.items(), key = lambda item: item[1], reverse = True)

    # for name2_pk, name2_value in movies1990s_rating.items():
    #     movies1990s_result[name2_pk] = entropy(user_movie_rankings_avg, name2_value)
    # sorted_dict1990s = sorted(movies1990s_result.items(), key = lambda item: item[1], reverse = True)

    # print(sorted_dict1990s)
    # print(sorted_dict2010s)
    # print(sorted_dict2000s)

    # 비율에 따라서 년도별 영화 추천 리스트 생성

    total_rating = 0
    total_rating_1990 = 0
    total_rating_2000 = 0
    total_rating_2010 = 0
    rating_1990 = rating_2000 = rating_2010 = 0
    for key, value in user_movie_centries.items():
        if int(key) == 1990:
            total_rating += int(value)
            total_rating_1990 += int(value)
        if int(key) == 2000:
            total_rating += int(value)
            total_rating_2000 += int(value)
        if int(key) == 2010:
            total_rating += int(value)
            total_rating_2010 += int(value)
    result_movie_pk_sim = []

    rating_1990 = math.ceil(total_rating_1990/total_rating*10)
    rating_2000 = math.ceil(total_rating_2000/total_rating*10)
    rating_2010 = math.ceil(total_rating_2010/total_rating*10)
    
    for i in range(0, rating_2010*3):
        result_movie_pk_sim.append([sorted_dict2010s[i][0], Movie.objects.get(pk=sorted_dict2010s[i][0]).vote_average])
    for i in range(0, rating_2000*3):
        result_movie_pk_sim.append([sorted_dict2000s[i][0], Movie.objects.get(pk=sorted_dict2000s[i][0]).vote_average])
    for i in range(0, rating_1990*3):
        result_movie_pk_sim.append([sorted_dict1990s[i][0], Movie.objects.get(pk=sorted_dict1990s[i][0]).vote_average])

    result_movie_pk_sim.sort(key=lambda x:x[1], reverse=True)
    result_movies = []

    for i in result_movie_pk_sim[0:10]:
        item = {
            'title' : Movie.objects.get(pk=i[0]).title,
            'poster_path' : Movie.objects.get(pk=i[0]).poster_path,
            'pk' : Movie.objects.get(pk=i[0]).pk,
        }
        result_movies.append(item)
    
    context = {
        'items': result_movies
    }

    return render(request, 'recommendations/index.html', context)








