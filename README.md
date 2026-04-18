# 🌙 Low-Light Image Enhancement Web App

## 📌 Overview

This project is a web-based application that enhances images captured in low-light conditions. It improves brightness, contrast, and visibility using a combination of image processing and AI-inspired techniques.

Users can upload a dark image, process it instantly, and download the enhanced output through an interactive interface.

---

## 🚀 Features

* Upload low-light images
* Automatic brightness and contrast enhancement
* Adjustable gamma (brightness control)
* Side-by-side comparison (original vs enhanced)
* Download enhanced image
* Simple and responsive web interface

---

## 🧠 Methodology

The enhancement pipeline uses a hybrid approach:

1. **Gamma Correction** – Adjusts brightness levels
2. **CLAHE (Contrast Limited Adaptive Histogram Equalization)** – Enhances contrast
3. **Color Space Transformation (LAB)** – Improves luminance without distorting colors

This combination produces visually improved images without requiring heavy deep learning models.

---

## 🛠️ Tech Stack

* Python
* Streamlit
* OpenCV
* NumPy
* Pillow
* Matplotlib

---

## 📂 Project Structure

```
lowlight-project/
│
├── app.py              # Streamlit web application
├── enhance.py          # Image enhancement logic
├── requirements.txt    # Dependencies
└── test.jpg            # Sample input image (optional)
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/your-username/lowlight-enhancer.git
cd lowlight-enhancer
```

### 2. Create virtual environment (optional but recommended)

```
python -m venv venv
venv\Scripts\activate     # Windows
source venv/bin/activate  # Mac/Linux
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```
streamlit run app.py
```

Open the browser at:

```
http://localhost:8501
```

---

## 🌍 Deployment

The application is deployed using Streamlit Cloud.

👉 Live Demo:
https://your-app-name.streamlit.app

---

## 📊 Evaluation Metrics (Optional)

* PSNR (Peak Signal-to-Noise Ratio)
* SSIM (Structural Similarity Index)

These metrics can be used to quantitatively evaluate enhancement quality.

---

## 🔮 Future Improvements

* Integration of deep learning models (e.g., Zero-DCE, CNN-based enhancement)
* Real-time video enhancement
* Mobile application deployment
* Noise reduction using advanced denoising techniques

---

## 🎯 Applications

* Night photography enhancement
* Surveillance systems
* Medical imaging
* Satellite image processing
* Autonomous driving systems

---

## 🙌 Acknowledgements

* Open-source libraries and research in image processing
* Streamlit for rapid web app development

---

## 📬 Contact

For any queries or improvements, feel free to reach out.

---

⭐ If you found this project useful, consider giving it a star!
