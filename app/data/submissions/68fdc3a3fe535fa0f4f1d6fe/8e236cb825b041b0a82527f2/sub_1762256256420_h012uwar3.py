n, m = map(int, input().split())
genres = [input() for _ in range(n)]

films = []
for i in range(m):
    genre = genres[int(input()[2:]) - 1]
    day, month, year = map(int, input().split("/"))
    name = input()
    episodes = int(input())
    films.append(
        {
            "index": i + 1,
            "genre": genre,
            "day": day,
            "month": month,
            "year": year,
            "name": name,
            "episodes": episodes,
        }
    )

films.sort(key=lambda f: (f["year"], f["month"], f["day"], f["name"], -f["episodes"]))
for film in films:
    index = film["index"]
    genre = film["genre"]
    day = film["day"]
    month = film["month"]
    year = film["year"]
    name = film["name"]
    episodes = film["episodes"]

    print(f"P{index:03d} {genre} {day:02d}/{month:02d}/{year:04d} {name} {episodes}")