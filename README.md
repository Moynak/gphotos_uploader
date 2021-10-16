# gphotos_uploader
This allows to upload folders of images and videos in seperate albums

1. Go to : developers.google.com/photos
2. console.cloud.google.com in API library search for Photos Library API
3. in Photos Library API, manage-> API enabled
4. create OAuth 2.0 client ID code, download the json console.cloud.google.com/apis/credentials

5. create python virtual environment
	python -m venv gphotos

6.	activate the venv: 
	.\gphotos\Scripts\activate

7. install google client library:
	Search: sheets API python -> developers.google.com/sheets/api/quickstart/python

	pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

	pip install pandas

8. create script

9. for each run, re downlaod OAuth 2.0 client ID code, download the json console.cloud.google.com/apis/credentials,
	
	delete the pickle file




Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
