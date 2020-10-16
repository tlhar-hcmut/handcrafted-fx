PY=python3

init:
	convert assets/examplate.gif -coalesce assets/example-%03d.jpg
	ffmpeg -i assets/example-%03d.jpg assets/example.avi 
	pip3 install -r requirements.txt

clean:
	rm assets/*.jpg
	rm assets/*.avi

mhi:
	${PY} src/mhi.py

sift:
	${PY} src/sift.py

hog:
	${PY} src/hog.py 