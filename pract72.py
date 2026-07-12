#Keyword argument

def movie(title , rating = 8 , language = "English", year = 2025):
    print(f"title={title}",f"rating={rating}",f"language={language}",f"year={year}")


movie("Batman")
movie("Batman",language="hindi")
movie("Batman",year=2012,rating=10)
movie(language="English", year=2008, rating=9, title="Batman")