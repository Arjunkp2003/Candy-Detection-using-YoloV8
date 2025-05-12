# Candy-Detection-using-YoloV8


🚀 Candy Detection Using YOLOv8 on Google Colab 🍬

I recently completed a computer vision project focused on multi-class candy detection using YOLOv8 and trained it on a custom dataset in Google Colab. The dataset included 11 different candy types such as MMs (regular & peanut), Airheads, Gummy Worms, Milky Way, Nerds, Skittles, Snickers, Starburst, Three Musketeers, and Twizzlers.

Using Ultralytics YOLOv8, I fine-tuned the model on a labeled dataset and achieved impressive results on the validation set with a mean Average Precision (mAP@0.5) of 96.7% and mAP@0.5:0.95 of 86.6%. Class-wise precision and recall were consistently high, with several classes like Twizzlers, Nerds, and Snickers reaching near-perfect accuracy. The model was efficient too, processing each image in approximately 1.5 ms end-to-end on a Tesla T4 GPU.

This project was a great learning experience in model training, data preparation using data.yaml, evaluation metrics, and deploying models on GPU via Colab. It showcases how YOLOv8 can be effectively used for real-time object detection tasks, even on diverse and colorful objects like candy wrappers.

Feel free to connect if you're working on similar computer vision applications or looking to collaborate!








### 📌 1. Key Features & Technologies Used

* **Model Architecture:** Ultralytics YOLOv8 (You Only Look Once, Version 8) — state-of-the-art for real-time object detection.
* **Custom Dataset:** 11 candy classes including MMs, Airheads, Gummy Worms, Milky Way, Nerds, Skittles, Snickers, Starburst, Three Musketeers, and Twizzlers.
* **Training Platform:** Google Colab (Tesla T4 GPU).
* **Labeling Format:** YOLO annotation format with a `data.yaml` file to define classes and paths.
* **Performance:**

  * `mAP@0.5`: 96.7%
  * `mAP@0.5:0.95`: 86.6%
  * Inference speed: \~1.5 ms per image.
* **Tools & Libraries:**

  * Ultralytics `yolov8` package
  * Python & OpenCV for image preprocessing
  * Roboflow/LabelImg (if used) for annotation
  * Matplotlib for visualization

---

### ⚙️ 2. How It Works (Step-by-Step)

1. **Dataset Collection & Annotation:**

   * Gather images of various candy types.
   * Annotate bounding boxes using tools like LabelImg or Roboflow.
   * Save labels in YOLO format and define metadata in `data.yaml`.

2. **Environment Setup in Google Colab:**

   * Install Ultralytics YOLOv8: `!pip install ultralytics`
   * Mount Google Drive or upload dataset directly.

3. **Model Configuration & Training:**

   * Load YOLOv8 model using `from ultralytics import YOLO`.
   * Fine-tune pretrained weights (`yolov8n.pt` or `yolov8s.pt`) on custom data.
   * Train using:

     ```python
     model = YOLO('yolov8n.pt')
     model.train(data='data.yaml', epochs=50, imgsz=640)
     ```

4. **Validation & Evaluation:**

   * Automatically computes metrics like mAP, precision, and recall.
   * Use `model.val()` to generate performance reports and visualizations.

5. **Inference on Test Images:**

   * Use `model.predict(source='image.jpg')` to detect candies.
   * Visualize bounding boxes and class labels on output images.

6. **Deployment on GPU (Colab):**

   * All steps are GPU-accelerated using a Tesla T4 via Colab’s free tier.
   * Enables real-time inference and model experimentation.

---

Let me know if you'd like a visual diagram, GitHub README template, or code snippet for any part!
