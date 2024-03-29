#!/usr/bin/env python3
from utils.rgbmatrix import RGBMatrix, RGBMatrixOptions
from multiprocessing import Process
from threading import Thread
from PIL import Image
import argparse
import time
import sys

def displayMatrix(image):

	# Configuration for the matrix
	image = Image.open(image)
	options = RGBMatrixOptions()
	options.hardware_mapping = 'adafruit-hat'
	options.cols = 64
	options.rows = 32
	options.gpio_slowdown = 5
	options.pwm_bits = 1
	options.pwm_lsb_nanoseconds = 100
	matrix = RGBMatrix(options = options)

	# Make image fit our screen
	image.thumbnail((matrix.width, matrix.height),Image.ANTIALIAS)
	matrix.SetImage(image.convert('RGB'))
	while True:
		time.sleep(60)
