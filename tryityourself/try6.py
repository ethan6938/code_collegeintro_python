import requests
import plotly.graph_objects as go

# Function to get GitHub repos for a given language
def get_github_repos(language='Python'):
    url = f"https://api.github.com/search/repositories?q=language:{language}&sort=stars"
    headers = {'Accept': 'application/vnd.github.v3+json'}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

# List of languages to analyze
languages = ['JavaScript', 'Ruby', 'C', 'Java', 'Perl', 'Haskell', 'Go']
repo_data = {}

for lang in languages:
    try:
        data = get_github_repos(lang)
        repo_data[lang] = data['items'][:10]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {lang}: {e}")

# Plot the data
fig = go.Figure()

for lang, repos in repo_data.items():
    repo_names = [repo['name'] for repo in repos]
    stars = [repo['stargazers_count'] for repo in repos]
    fig.add_trace(go.Bar(name=lang, x=repo_names, y=stars))

fig.update_layout(
    title="Top 10 GitHub Repositories by Stars for Different Languages",
    xaxis_title="Repository Name",
    yaxis_title="Stars",
    barmode='group'
)

fig.show()
