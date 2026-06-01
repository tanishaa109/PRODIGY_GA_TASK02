# PRODIGY_GA_TASK02 - Text to Image Generator using Stable Diffusion

## 📌 Project Overview
This project generates images from text prompts using a pre-trained Stable Diffusion model.

Users can enter a text description, and the model creates a corresponding AI-generated image.

---

## 🚀 Features
- Text-to-image generation
- Stable Diffusion pre-trained model
- User prompt based image creation
- AI-generated image outputs
- Google Colab GPU support

---

## 🛠️ Technologies Used
- Python
- PyTorch
- Hugging Face Diffusers
- Transformers
- Google Colab

---

## 📂 Project Structure

```text
PRODIGY_GA_TASK02/
│
├── app.py
├── requirements.txt
├── README.md
├── PRODIGY_GA_02.ipynb
├── outputs/
└── screenshots/
```

---

## ▶️ How to Run

### Method 1: Google Colab (Recommended)

1. Download `PRODIGY_GA_02.ipynb`
2. Open Google Colab
3. Upload the notebook
4. Enable GPU:
   Runtime → Change Runtime Type → GPU
5. Run all cells
6. Enter a text prompt
7. Generated image will be displayed and saved

---

### Method 2: Local System

```bash
pip install -r requirements.txt
python app.py
```

Note: Stable Diffusion is resource intensive. Google Colab with GPU is recommended.

---

## 🖼️ Sample Prompts

- a futuristic city at night
- a cute panda eating pizza
- an astronaut riding a horse
- a cyberpunk street in Tokyo
- a royal tiger sitting on a golden throne

---

## 📸 Outputs

Generated images are stored in the `outputs/` folder.

Screenshots of model loading, prompt input, and generated outputs are available in the `screenshots/` folder.

---

## ⚠️ Important Note

GitHub may occasionally fail to render large Jupyter notebooks in preview mode.

If the notebook preview does not load:

1. Download the notebook file
2. Open it directly in Google Colab
3. Run the notebook normally

The notebook itself is not affected.

---

## 👨‍💻 Internship Task

Prodigy Infotech - Generative AI Internship

Task 02: Text-to-Image Generation using Stable Diffusion