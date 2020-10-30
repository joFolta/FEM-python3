# Explanation: https://practical.learnpython.dev/01_why_python/50_anatomy_of_a_python_program/#step-by-step

"""
A small Python program that uses the GitHub search API to list
the top projects by language, based on stars.
"""

import requests

GITHUB_API_URL = "https://api.github.com/search/repositories"


def create_query(languages, min_stars=50000):
    # NOTE: f string (format string)- similar to JS template literal
    query = f"stars:>{min_stars} " 

    for language in languages:
        query += f"language:{language} "

    # a sample query looks like: "stars:>50 language:python language:javascript"
    return query


def repos_with_most_stars(languages, sort="stars", order="desc"):
    query = create_query(languages)
    # NOTE: defining dictionary
    params = {"q": query, "sort": sort, "order": order}

    response = requests.get(GITHUB_API_URL, params=params)
    status_code = response.status_code

    if status_code != 200:
        raise RuntimeError(f"An error occurred. HTTP Code: {status_code}.")
    else:
        response_json = response.json()
        return response_json["items"]


if __name__ == "__main__":
    languages = ["python", "javascript", "ruby"]
    results = repos_with_most_stars(languages)

    for result in results:
        language = result["language"]
        stars = result["stargazers_count"]
        name = result["name"]

        # NOTE: print result
        print(f"-> {name} is a {language} repo with {stars} stars.")

# NOTE: Results of running program
# -> freeCodeCamp is a JavaScript repo with 316266 stars.
# -> vue is a JavaScript repo with 174560 stars.
# -> react is a JavaScript repo with 158310 stars.
# -> bootstrap is a JavaScript repo with 144989 stars.
# -> system-design-primer is a Python repo with 110576 stars.
# -> javascript is a JavaScript repo with 100994 stars.
# -> public-apis is a Python repo with 98938 stars.
# -> Python-100-Days is a Python repo with 94772 stars.
# -> d3 is a JavaScript repo with 94248 stars.
# -> react-native is a JavaScript repo with 91007 stars.
# -> Python is a Python repo with 90613 stars.
# -> awesome-python is a Python repo with 88229 stars.
# -> javascript-algorithms is a JavaScript repo with 83448 stars.
# -> create-react-app is a JavaScript repo with 83335 stars.
# -> axios is a JavaScript repo with 78365 stars.
# -> node is a JavaScript repo with 74425 stars.
# -> models is a Python repo with 66919 stars.
# -> 30-seconds-of-code is a JavaScript repo with 64928 stars.
# -> three.js is a JavaScript repo with 64429 stars.
# -> Font-Awesome is a JavaScript repo with 64238 stars.
# -> material-ui is a JavaScript repo with 62055 stars.
# -> angular.js is a JavaScript repo with 59508 stars.
# -> thefuck is a Python repo with 56845 stars.
# -> webpack is a JavaScript repo with 56219 stars.
# -> next.js is a JavaScript repo with 55606 stars.
# -> nodebestpractices is a JavaScript repo with 54342 stars.
# -> jquery is a JavaScript repo with 54116 stars.
# -> reveal.js is a JavaScript repo with 53517 stars.
# -> atom is a JavaScript repo with 53412 stars.
# -> django is a Python repo with 53257 stars.