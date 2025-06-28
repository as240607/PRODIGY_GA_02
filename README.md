## 🧠 Task-02: Image Generation with Pre-trained Models

### 📝 Objective

The goal of this task is to explore and utilize pre-trained text-to-image generative models like **DALL·E-mini** or **Stable Diffusion** to generate unique and high-quality images from natural language prompts. This exercise demonstrates how powerful generative models can create visual content with minimal effort using Python.

---

### ⚙️ Technologies & Tools Used

* **Python**
* **Torch (PyTorch)**: For hardware acceleration and tensor operations.
* **HuggingFace `diffusers` library**: To load and use pre-trained diffusion models.
* **Pillow (PIL)**: For image saving and manipulation.
* **MediaPy**: For image display.
* **Pre-trained Models**:

  * `digiplay/Realisian_v5`
  * `hakurei/waifu-diffusion` (anime style)
  * `CompVis/stable-diffusion-v1-4` (cyberpunk style)

---

### 🔍 Features

* Automatically detects and uses **GPU** if available, otherwise falls back to CPU.
* Supports **three styles** of image generation:

  * Realisian (hyper-realistic)
  * Anime (Waifu Diffusion)
  * Cyberpunk (Stable Diffusion)
* User can input their own **text prompt** or use the default one:
  `"a hyper-realistic portrait of a female cyborg in a futuristic city"`.
* Uses a **negative prompt** to suppress common artifacts such as bad hands, low quality, watermarks, and anatomical issues.
* Ensures image size consistency: `512 x 736 pixels`.
* Saves the generated image with an **auto-renaming** mechanism to avoid overwriting.
* Displays the image after generation and prints metadata like:

  * Prompt
  * Style
  * Filename
  * Seed used for reproducibility

---

### 🚀 How It Works

1. **Model Selection**:
   A style is chosen from a predefined dictionary. If no valid input is given, the default style is `'realisian'`.

2. **Prompt Input**:
   A prompt describing the image is taken from the user. If empty, a default futuristic portrait prompt is used.

3. **Model Loading**:
   The selected pre-trained model is loaded using `DiffusionPipeline.from_pretrained`.

4. **Image Generation**:
   The model uses the prompt and a fixed seed to generate a consistent output every time it runs.

5. **Image Saving & Display**:
   The image is saved in the same directory with a unique filename and displayed using MediaPy.

---

### 📂 Output Example

For the default prompt and style:

* **Prompt**: `"a hyper-realistic portrait of a female cyborg in a futuristic city"`
* **Style**: `realisian`
* **Filename**: `realisian_output.jpg`
* **Seed**: `4329492846`

The output is a detailed, AI-generated image saved locally and displayed on screen.

---

### 📌 References

* [HuggingFace Diffusers Documentation](https://huggingface.co/docs/diffusers/index)
* [Waifu Diffusion on HuggingFace](https://huggingface.co/hakurei/waifu-diffusion)
* [Stable Diffusion](https://huggingface.co/CompVis/stable-diffusion-v1-4)
* [Realistic Vision Model (Realisian)](https://huggingface.co/digiplay/Realisian_v5)
