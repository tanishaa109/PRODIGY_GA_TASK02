# PRODIGY_GA_TASK02 - Text to Image Generator using Stable Diffusion

## 📌 Project Overview

This project uses a pre-trained Stable Diffusion model to generate images from text prompts.

Users can enter a text description, and the model generates a corresponding AI-created image using Generative AI techniques.

This project was developed as part of the Prodigy Infotech Generative AI Internship.

---

## 🚀 Features

* Text-to-image generation
* Uses pre-trained Stable Diffusion model
* User prompt based image creation
* AI-generated image outputs
* Google Colab GPU support
* Output image saving

---

## 🛠️ Technologies Used

* Python
* PyTorch
* Hugging Face Diffusers
* Transformers
* Stable Diffusion
* Google Colab
* GitHub

---

## 📂 Project Structure

```text
PRODIGY_GA_TASK02/
│
├── README.md
├── app.py
├── requirements.txt
├── PRODIGY_GA_02.ipynb
│
├── outputs/
│   ├── generated_image_1.png
│   └── generated_image_2.png
│
└── screenshots/
    ├── 01_model_loaded.png
    ├── 02_prompt_input.png
    └── 03_generated_image.png
```

---

## ▶️ How to Use

### Method 1: Open Directly in Google Colab (Recommended)

1. Open Google Colab.
2. Click **File → Open Notebook**.
3. Select the **GitHub** tab.
4. Search for your GitHub repository.
5. Open:

```text
PRODIGY_GA_02.ipynb
```

6. Enable GPU:

```text
Runtime → Change Runtime Type → GPU
```

7. Run all cells.
8. Enter a text prompt.
9. The model will generate and display an image.

---

### Method 2: Download Notebook and Run in Colab

1. Open `PRODIGY_GA_02.ipynb` from the repository.
2. Download the notebook.
3. Open Google Colab.
4. Upload the notebook.
5. Enable GPU.
6. Run all cells.
7. Enter your desired text prompt.

---

### Method 3: Run Locally (Optional)

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python app.py
```

Note: Stable Diffusion is resource intensive. Google Colab with GPU is recommended for best performance.

---

## 🖼️ Example Prompts

* a futuristic city at night
* a cute panda eating pizza
* an astronaut riding a horse on the moon
* a cyberpunk street in Tokyo
* a royal tiger sitting on a golden throne

---

## 📸 Outputs

Generated sample images are available in the `outputs` folder.

Project execution screenshots are available in the `screenshots` folder:

* 01_model_loaded.png
* 02_prompt_input.png
* 03_generated_image.png

These screenshots demonstrate:

* Successful model loading
* User prompt input
* AI-generated image generation

---

## ⚠️ GitHub Notebook Preview

Sometimes GitHub may fail to render large Jupyter notebooks and display a notebook preview error.

If this happens:

1. Open the notebook directly in Google Colab.
2. Or download the notebook and upload it to Colab.
3. Run the notebook normally.

The notebook file itself remains fully functional.

## Note for Running the Notebook

This project was developed and tested using **Google Colab**.

If you open the notebook in VS Code, you may see the warning:

```python
Import "google.colab" could not be resolved
```

This is expected because the `google.colab` package is available only inside the Google Colab environment.

### How to Run

1. Download the notebook from this repository.
2. Open Google Colab.
3. Upload the notebook.
4. Run all cells sequentially.
5. Ensure GPU runtime is enabled:

   * Runtime → Change Runtime Type → GPU

The notebook is intended to be executed in Google Colab and may show import warnings in local IDEs such as VS Code.


---

## 🎯 Internship Task

**Prodigy Infotech – Generative AI Internship**

**Task 02:** Generate images from text prompts using a pre-trained generative model (Stable Diffusion).

---

## 👨‍💻 Author

**Tanisha Sharma**
