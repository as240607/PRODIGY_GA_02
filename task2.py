import torch
from diffusers import DiffusionPipeline
import os
from PIL import Image
import mediapy as media

# 🧠 Automatically choose device
device = "cuda" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if device == "cuda" else torch.float32

# 🎨 Supported styles and their model IDs
styles = {
    "realisian": "digiplay/Realisian_v5",
    "anime": "hakurei/waifu-diffusion",
    "cyberpunk": "CompVis/stable-diffusion-v1-4"
}

# 📢 Display styles and take user input
print("🎨 Available styles:")
for s in styles:
    print(f" - {s}")
style = input("Enter a style (or press Enter to use 'realisian'): ").strip().lower()
if style not in styles:
    print("⚠️ Invalid or no style selected. Using default: 'realisian'")
    style = "realisian"

model_id = styles[style]

# ✏️ Prompt input
user_input = input("Enter a prompt (or press Enter to use the default): ").strip()
prompt = user_input if user_input else "a hyper-realistic portrait of a female cyborg in a futuristic city"

# ❌ Negative prompt to improve quality
negative_prompt = (
    "bad-picture-chill-75v, ng_deepnegative_v1_75t, badhandv4, "
    "(worst quality:2), (low quality:2), (normal quality:2), (lowres:2), "
    "(bad anatomy:2), (bad hands:2), (watermark:2), (mole:1.5), (freckles:1.5)"
)

# 📏 Image size and seed
width = 512
height = 736
seed = 4329492846
use_refiner = False

# 🔄 Load pipeline
print(f"\n🔄 Loading model: {model_id}")
pipe = DiffusionPipeline.from_pretrained(
    model_id,
    torch_dtype=torch_dtype,
    safety_checker=None,
    requires_safety_checker=False
).to(device)

# 🎨 Generate image
generator = torch.Generator(device=device).manual_seed(seed)
result = pipe(
    prompt=prompt,
    width=width,
    height=height,
    negative_prompt=negative_prompt,
    output_type="latent" if use_refiner else "pil",
    generator=generator
)
images = result.images

# 💾 Save image
filename = f"{style}_output.jpg"
i = 1
while os.path.exists(filename):
    filename = f"{style}_output_{i}.jpg"
    i += 1
images[0].save(filename)

# 📷 Show and print result
media.show_images(images)
print("\n✅ Image generated and saved.")
print(f"🖼️ File: {filename}")
print(f"🎨 Style: {style}")
print(f"🧠 Prompt: {prompt}")
print(f"🎯 Seed: {seed}")