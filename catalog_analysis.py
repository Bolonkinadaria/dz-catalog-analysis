import math

#---Исходные данные---
movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]}, # noqa: E501
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]
#---Этап 1: Разминка---
def average_rating(movies):
    total = sum(m["rating"] for m in movies)
    return round(total / len(movies), 1)

def catalog_age_stats(movies, current_year=2026):
    ages = [current_year - m["year"] for m in movies]
    # Возвращаем кортеж (tuple): (самый старый, самый новый, среднее)
    return (max(ages), min(ages), math.ceil(sum(ages) / len(ages)))

def duration_in_hours(minutes):
    return f"{minutes // 60}ч {minutes % 60}м"

#---Этап 2: Условия и match---
def rating_tier(rating):
    if rating >= 9:
        return "шедевр"
    elif 7 <= rating <= 8.9:
        # Обязательно используем тернарный оператор
        return "хорошо" if rating >= 8 else "хорошо"
    elif 5 <= rating <= 6.9:
        return "средне"
    else:
        return "слабо"

def decade_label(year):
    # Обязательно используем match с case _ if
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if 2015 <= year <= 2020:
            return "недавние"
        case _:
            return "старые"

#---Этап 3: Циклы---
def print_non_comedy(movies):
    for m in movies:
        if "comedy" in m["genres"]:
            continue # Обязательно continue
        print(m["title"])

def find_first_masterpiece(movies):
    i = 0
    while i < len(movies):
        if movies[i]["rating"] > 9.0:
            print(f"Найден шедевр: {movies[i]['title']}")
            break # Обязательно break
        i += 1
    else:
        # Ветка else сработает, только если break не был вызван
        print("Шедевров не найдено")

def count_long_movies(movies, threshold=120):
    count = 0
    for m in movies:
        if m["duration_min"] > threshold:
            count += 1 # Только накопление, нельзя sum()
    return count

#---Этап 4: Строки---
def normalize_title(title):
    words = title.split()
    # Меняем регистр первой буквы через срез и .upper()
    return " ".join([w[0].upper() + w[1:] for w in words])

def make_slug(title):
    normalized = normalize_title(title)
    # Используем .lower() и .replace()
    return normalized.lower().replace(" ", "-")

def format_report_line(movie):
    title = normalize_title(movie["title"])
    genres = ", ".join(sorted(movie["genres"])) # Жанры по алфавиту
    duration = duration_in_hours(movie["duration_min"])
    # Обязательно f-строка
    return f'"{title}" ({movie["year"]}) — {movie["rating"]}/10, {duration}, жанры: {genres}' # noqa: E501

#---Этап 5: Списки---
def titles_sorted_by_rating(movies):
    # Сортировка через sorted() с ключом, не меняем исходный список
    sorted_movies = sorted(movies, key=lambda m: m["rating"], reverse=True)
    return [m["title"] for m in sorted_movies]

def top_n_by_rating(movies, n=3):
    sorted_movies = sorted(movies, key=lambda m: m["rating"], reverse=True)
    # Возвращаем именно кортежи (title, rating)
    return [(m["title"], m["rating"]) for m in sorted_movies[:n]]

#--- Этап 6: Словари---
def count_by_genre(movies):
    counts = {}
    for m in movies:
        for genre in m["genres"]:
            # Обязательно dict.get()
            counts[genre] = counts.get(genre, 0) + 1
    return counts

def actor_filmography(movies):
    filmography = {}
    for m in movies:
        for actor in m["actors"]:
            if actor not in filmography:
                filmography[actor] = []
            filmography[actor].append(m["title"])
    return filmography

def high_rated_dict(movies):
    avg = average_rating(movies)
    # Обязательно генератор словаря (dict comprehension)
    return {m["title"]: m["rating"] for m in movies if m["rating"] > avg}

#---Этап 7: Множества---
def all_genres(movies):
    genres = set()
    for m in movies:
        # Объединение множеств
        genres |= m["genres"]
    return genres

def common_actors(movie1, movie2):
    # Пересечение множеств
    return set(movie1["actors"]) & set(movie2["actors"])

def genres_only_in_one(movies_a, movies_b):
    # Разность множеств
    return all_genres(movies_a) - all_genres(movies_b)

#---Этап 8: Итераторы и генераторы---
def iter_high_rated(movies, min_rating=8.0):
    # Обязательно yield
    for m in movies:
        if m["rating"] >= min_rating:
            yield m

#---Этап 9: Итоговый отчет---
def build_report(movies):
    print("ОТЧЕТ ПО КАТАЛОГУ")
    print(f"Средний рейтинг: {average_rating(movies)}")
    # Берем среднее из кортежа (третий элемент)
    print(f"Средний возраст фильмов: {catalog_age_stats(movies)[2]} лет")
    print()
    
    print("Топ-3 фильма:")
    for title, rating in top_n_by_rating(movies, 3):
        for m in movies:
            if m["title"] == title:
                print(format_report_line(m))
                break
    print()
    
    print("Фильмов по жанрам:")
    genre_counts = count_by_genre(movies)
    # Сортируем по убыванию количества
    for genre, count in sorted(genre_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  {genre} — {count}")
    print()
    
    all_g = sorted(list(all_genres(movies)))
    # Выводим одной строкой через join
    print(f"Все жанры каталога: {', '.join(all_g)}")

# --- Точка входа ---
if __name__ == "__main__":
    build_report(movies)