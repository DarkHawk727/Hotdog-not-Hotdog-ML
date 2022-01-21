import requests, lxml, re, json, os 
from bs4 import BeautifulSoup
from bing_image_downloader import downloader
import os
import cv2
import imghdr

downloader.download('hotdog', limit=20000,  output_dir='dataset2', adult_filter_off=True, force_replace=False, timeout=1, verbose=True)