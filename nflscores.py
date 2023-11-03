#!/usr/bin/env python
# Display live NFL scores for the current week using the ESPN API.
from samplebase import SampleBase
from rgbmatrix import graphics
from rgbmatrix import RGBMatrixOptions
import requests
import time
from datetime import date, timedelta

class RunESPNAPI(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunESPNAPI, self).__init__(*args, **kwargs)

    def fetch_scores(self):
        today = date.today()
        current_year = today.year

        # Find the start of the current week (Sunday)
        current_date = today
        while current_date.weekday() != 6:  # 6 corresponds to Sunday
            current_date -= timedelta(days=1)

        start_date = current_date.strftime("%Y%m%d")

        # Find the end of the current week (Saturday)
        end_date = (current_date + timedelta(days=6)).strftime("%Y%m%d")

        api_url = f"http://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard?limit=1000&dates={start_date}-{end_date}"
        response = requests.get(api_url)
        data = response.json()
        return data

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("../../../fonts/7x13.bdf")
        textColor = graphics.Color(255, 0, 0)

        while True:
            offscreen_canvas.Clear()
            nfl_scores = self.fetch_scores()

            # Extract and format the NFL scores
            nfl_scores_text = "NFL Scores: "
            for event in nfl_scores.get("events", []):
                competition = event.get("competitions", [])[0]
                home_team = competition["competitors"][0]["team"]["abbreviation"]
                away_team = competition["competitors"][1]["team"]["abbreviation"]
                home_score = competition["competitors"][0]["score"]
                away_score = competition["competitors"][1]["score"]
                nfl_scores_text += f"{home_team} {home_score} - {away_team} {away_score} | "

            len = graphics.DrawText(offscreen_canvas, font, offscreen_canvas.width, 10, textColor, nfl_scores_text)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)

            for i in range(offscreen_canvas.width, -len, -1):
                offscreen_canvas.Clear()
                x = i
                graphics.DrawText(offscreen_canvas, font, x, 20, textColor, nfl_scores_text)
                offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
                time.sleep(0.05)

if __name__ == "__main__":
    options = RGBMatrixOptions()
    options.rows = 32
    options.cols = 64
    options.chain_length = 1
    options.parallel = 1
    options.hardware_mapping = "adafruit-hat"

    run_espn_api = RunESPNAPI(options=options)
    if not run_espn_api.process():
        run_espn_api.print_help()
