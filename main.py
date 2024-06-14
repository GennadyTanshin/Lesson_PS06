from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv

PATH = "C:\\Geckodriver\\geckodriver.exe"
service = Service(PATH)
driver = webdriver.Firefox(service=service)




