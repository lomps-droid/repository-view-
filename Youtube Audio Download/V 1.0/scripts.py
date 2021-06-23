import sys, pafy
from main import *
from main import Main



class Addurl:
    def __init__(self, url) -> None:
        self.url = url
    def set_URL(self):
        video_url = pafy.new(self.url)
        best = video_url.getbest()
        best.download(filepath=".//downloads//")
