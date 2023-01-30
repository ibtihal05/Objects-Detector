from flask import Flask, request, render_template, redirect
import os
from mmdet.apis import ( inference_detector,
                        init_detector, show_result_pyplot)


app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

destination=""
IMG_FOLDER = os.path.join('static', 'IMG')
app.config['UPLOAD_FOLDER'] = IMG_FOLDER

@app.route("/image", methods=["POST","GET"])
def image():
    global destination
    path = os.path.join(APP_ROOT, 'images/')
    if not os.path.isdir(path):
        os.mkdir(path)
    
    if request.method == "POST":
        img = request.files['img']

        if img.filename == '':
            print("Image must have a file name")
            return redirect(request.url)

        imgname = img.filename
        destination = "/".join([path, imgname])
        img.save(destination)
    
        return render_template("model.html")
    else :
        return render_template("image.html")
    

@app.route("/model", methods=["POST","GET"])
def model():
    global destination
    if request.method == "POST" :
        model=request.form["model"]
        # execution of the detection's code
        img=destination
        if model=="Yolov" :
            config="yolov3_mobilenetv2_320_300e_coco.py "
            checkpoint="yolov3_mobilenetv2_320_300e_coco_20210719_215349-d18dff72.pth"
        elif model=="RetinaNet" :
            config="retinanet_r50_fpn_1x_coco.py "
            checkpoint="retinanet_r50_fpn_1x_coco_20200130-c2398f9e.pth"
        else :
            return redirect(request.url)

        device="cpu"
        palette="coco"
        score_thr=0.3
        out_file="./static/IMG/result.jpg"

        model = init_detector(config, checkpoint, device=device)
        # test a single image
        result = inference_detector(model,img)
        # show the results
        show_result_pyplot(
            model,
            img,
            result,
            palette=palette,
            score_thr=score_thr,
            out_file=out_file)

        # end of detection now show result
        result_image = os.path.join(app.config['UPLOAD_FOLDER'], 'result.jpg')
        return render_template("result.html", result_image=result_image)
    else :
        return render_template("model.html")


@app.route("/result")
def result():
    return render_template("result.html")


if __name__ == "__main__":
    app.run()