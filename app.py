from diffusers import StableDiffusionPipeline
import torch
import os

# folder for output images
os.makedirs("outputs", exist_ok=True)

print("Loading Stable Diffusion model... please wait ⏳")

model_id = "runwayml/stable-diffusion-v1-5"

pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float16
)

pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")

print("Model loaded successfully 🚀")

while True:
    prompt = input("\nEnter your text prompt (or type 'exit'): ")

    if prompt.lower() == "exit":
        print("Program ended 👋")
        break

    print("Generating image... 🎨")

    image = pipe(prompt).images[0]

    filename = f"outputs/{prompt[:30].replace(' ','_')}.png"
    image.save(filename)

    print("Image saved at:", filename)
    image.show()
    # just local version fallback
print("Run this project in Google Colab for best performance")