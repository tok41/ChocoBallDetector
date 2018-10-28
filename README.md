# ChocoBallDetector

- Chocoball Detector
- based on [ChainerCV](https://chainercv.readthedocs.io/en/stable/#)
  - using [Faster-RCNN](https://chainercv.readthedocs.io/en/stable/reference/links/faster_rcnn.html?highlight=faster%20rcnn)

## Preparation
### environment
- clone this repository
- install libraries
```
$ pip install -r requirements.txt
```

- cleate following directory
```
$ mkdir model
$ mkdir data
$ mkdir data/res_images
$ mkdir tmp
	# for keeping temporary image
$ mkdir out
	# output directory
$ mkdir uploads
```

### Model
- model/snapshot_model.npz

### classes file
- data/classes.txt

## Testing
- store image-data to "data/res_images"
```
$ python chocoball_counter.py
```
- output detected image to "out"
  - out/detected.png

