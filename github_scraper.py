import requests
from bs4 import BeautifulSoup
import pprint

def scrape_github_trending():
    url = "https://github.com/trending"
    response = requests.get(url)

    if response.status_code == 200:
        html_content = response.content
        soup = BeautifulSoup(html_content, "html.parser")

        # Check if the selector is valid and retrieves elements
        all_trending_repo = soup.select('article.Box-row h2')

        if all_trending_repo:
            trending_repositories = []

            for each_trending_repo in all_trending_repo:
                href_link = each_trending_repo.a.attrs.get("href")
                if href_link:
                    name = href_link[1:]
                    repo = {"label": name,
                            "link": "https://github.com{}".format(href_link)}
                    trending_repositories.append(repo)

            return trending_repositories
        else:
            print("No repositories found. Check the selector.")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

    return []

if __name__ == "__main__":
    trend_repo = scrape_github_trending()
    pprint.pprint(trend_repo)
