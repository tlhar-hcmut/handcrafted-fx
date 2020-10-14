init:
	convert assets/examplate.gif -coalesce assets/example-%03d.jpg
	ffmpeg -i assets/example-%03d.jpg assets/example.avi 
	pip3 install opencv-python opencv-contrib-python

clean:
	rm assets/*.jpg
	rm assets/*.avi