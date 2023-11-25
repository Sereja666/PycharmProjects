import replicate

model = replicate.Client(api_token="b04fd99477416d4d7144e96874a8fae18392ddbc")
model = model.models.get("tstramer/midjourney-diffusion")

version = model.versions.get("b04fd99477416d4d7144e96874a8fae18392ddbc")


# https://replicate.com/tstramer/midjourney-diffusion/versions/436b051ebd8f68d23e83d22de5e198e0995357afef113768c20f0b6fcef23c8b#input
inputs = {
    # Input prompt
    'prompt': "a photo of an astronaut riding a horse on mars",

    # Specify things to not see in the output
    # 'negative_prompt': ...,

    # Width of output image. Maximum size is 1024x768 or 768x1024 because
    # of memory limits
    'width': 768,

    # Height of output image. Maximum size is 1024x768 or 768x1024 because
    # of memory limits
    'height': 768,

    # Prompt strength when using init image. 1.0 corresponds to full
    # destruction of information in init image
    'prompt_strength': 0.8,

    # Number of images to output.
    # Range: 1 to 4
    'num_outputs': 1,

    # Number of denoising steps
    # Range: 1 to 500
    'num_inference_steps': 50,

    # Scale for classifier-free guidance
    # Range: 1 to 20
    'guidance_scale': 7.5,

    # Choose a scheduler.
    'scheduler': "DPMSolverMultistep",

    # Random seed. Leave blank to randomize the seed
    # 'seed': ...,
}

# https://replicate.com/tstramer/midjourney-diffusion/versions/436b051ebd8f68d23e83d22de5e198e0995357afef113768c20f0b6fcef23c8b#output-schema
output = version.predict(**inputs)
print(output)
