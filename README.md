# object Detector web interface for Retinanet and Yolov models using mmdetection 
<img width="959" alt="image" src="https://user-images.githubusercontent.com/100495094/215632065-52d064f8-268d-42ae-801b-2e90bc3e1690.PNG">
<img width="949" alt="model" src="https://user-images.githubusercontent.com/100495094/215632530-7834fa0c-3fef-49ca-b600-620250640b8f.PNG">

## Requirements

- Our codebase use [MMDetection](https://github.com/open-mmlab/mmdetection), which can be installed following the offcial instuctions.

- Flask, which can be installed running :
```shell
pip install Flask
```
- Retinanet model, which can be downloaded from [Retinanet model](https://download.openmmlab.com/mmdetection/v2.0/retinanet/retinanet_r50_fpn_1x_coco/retinanet_r50_fpn_1x_coco_20200130-c2398f9e.pth)
- Yolov model, which can be downloaded from [Yolov model](https://download.openmmlab.com/mmdetection/v2.0/yolo/yolov3_mobilenetv2_320_300e_coco/yolov3_mobilenetv2_320_300e_coco_20210719_215349-d18dff72.pth)

### Setup 
- Place the two models's files in web interface folder

### Run objects-detector interface
- You can run the interface by executing the app python file first :
```shell
python web interface/app.py 
```
- then copy and paste the given url in your browser and add /image to it 

