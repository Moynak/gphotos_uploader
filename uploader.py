from pprint import pprint
from init_photo_service import service
import pandas as pd


import os
import time
import datetime
import re



"""
batchCretae method
"""

import pickle
import requests

year = 2008
month = 10
day = 11
hour = 00
minute = 00
second = 0

parent_dir = "C:\\Users\moyna\Downloads\\testing"
upload_url = 'https://photoslibrary.googleapis.com/v1/uploads'
token = pickle.load(open('token_photoslibrary_v1.pickle', 'rb'))



# Method for uploading
def upload_image(image_path, upload_file_name, token):
    headers = {
        'Authorization': 'Bearer ' + token.token,
        'Content-type': 'application/octet-stream',
        'X-Goog-Upload-Protocol': 'raw',
        'X-Goog-File-Name': upload_file_name
    }    
    # Not the image file, the whole path
    img = open(image_path, 'rb').read()
    response = requests.post(upload_url, data=img, headers=headers)
    return response



for directory in os.listdir(parent_dir):
	try:
		print(directory.encode("utf-8"))
	except Exception as e:
		template = "An exception of type {0} occurred. Arguments:\n{1!r}"
		message = template.format(type(e).__name__, e.args)
		print (message)
	request_body = {
		'album': {'title': directory}
	}
	response_album = service.albums().create(body=request_body).execute()
	albumId = response_album.get('id')
	tokens = []
	names = []
	dir_path = os.path.join(parent_dir, directory)
	for filename in os.listdir(dir_path):
		image_path = os.path.join(dir_path, filename)
		response_img = upload_image(image_path, os.path.basename(image_path), token)
		if response_img.ok: 
			tokens.append(response_img.content.decode('utf-8'))
			names.append(filename)
		else:
			print(os.path.basename(image_path), " Did not upload: Status code = ", response_img.status_code)
			exit()
	#split the tokens into chunks of size 50
	start_idx = 0
	end_idx = len(tokens)
	for idx in range(start_idx, end_idx, 50):
		start_idx = idx
		part_tokens = tokens[start_idx: min(end_idx, start_idx + 50)]
		part_names = names[start_idx: min(end_idx, start_idx + 50)]
		# Now upload the images 
		new_media_items = [{'simpleMediaItem': {'uploadToken': part_tokens[part_idx], 'fileName': part_names[part_idx]}} for part_idx in range(len(part_tokens))]
		request_body = {
			'albumId': albumId,
			'newMediaItems': new_media_items
		}
		upload_response_img = service.mediaItems().batchCreate(body=request_body).execute()



