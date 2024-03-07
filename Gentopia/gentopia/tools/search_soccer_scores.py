import requests
from bs4 import BeautifulSoup

from typing import AnyStr
from gentopia.tools.basetool import *

class SoccerScoreSearchArgs(BaseModel):
    pass

class SoccerScoreSearch(BaseTool):
    """Tool that adds the capability to read a PDF file."""
    name = "search_soccer_scores"
    description = ("A tool that premier league's upcoming fixtures")
    args_schema: Optional[Type[BaseModel]] = SoccerScoreSearchArgs

    def _run(self) -> str:
        res = requests.get('https://www.bbc.com/sport/football/premier-league/scores-fixtures/2024-03?filter=results')
        soup = BeautifulSoup(res.text, 'html.parser')

        res = ""

        for fixtures in soup.find_all('div', class_='qa-match-block'):
            fixtures = fixtures.text
            res += fixtures
            res += "\n"

        return res


    async def _arun(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError


if __name__ == "__main__":
    ans = SoccerScoreSearch()._run("Attention for transformer")
    print(ans)
