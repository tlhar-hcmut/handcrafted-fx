init:
	convert assets/examplate.gif -coalesce assets/example-%03d.jpg

clean:
	rm assets/*.jpg