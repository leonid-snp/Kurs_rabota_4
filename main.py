import requests


get_url = "https://api.hh.ru/vacancies"

response = requests.get(get_url, params={"text": "Python"})

print(response.status_code)
print(response.json())


# def user_interaction():
#     platform = ["HeadHunter"]
#     search_query = input("Введите поисковой запрос: ")
#
#
# if __name__ == "__main__":
#     user_interaction()
