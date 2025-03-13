# remote_custom_weights_url = "https://chatgenius.idealabs.mobi/iostattoo/model/custom_updated_weights.json"
local_custom_weights = {
    "CHECKPOINTS": [
        {
            "name": "samaritan3dCartoon_v20.safetensors",
            "url": "https://replicate.delivery/pbxt/KYC72ChS23fGECBUjYkoPFP3gQuOziBgBCMZZhGzxQMQT0WR/samaritan3dCartoon_v20.safetensors.tar",
        },
        {
            "name": "stable_cascade_stage_b.safetensors",
            "url": "https://replicate.delivery/pbxt/KYYXEciqLb5L3Qe0QjUCohWJSWkfy6ALxkM4P1dRx7z6smWz/upload.tar",
        },
        {
            "name": "stable_cascade_stage_c.safetensors",
            "url": "https://replicate.delivery/pbxt/KYZ0MnFVzxF8PERstp2UlUWSic9GB3UqpbNgKVQh7fUhQBZA/upload.tar",
        },
        {
            "name": "dreamshaperXL_v21TurboDPMSDE.safetensors",
            "url": "https://replicate.delivery/pbxt/MUVyZML25b8wwaBHGJIKQsQpvVHNEOAjsSd1Ozsz61OriA5O/upload.tar",
        },
        {
            "name": "juggernautXL_juggXILightningByRD.safetensors",
            "url": "https://chatgenius.idealabs.mobi/genius/model/juggernautXL_juggXILightningByRD.safetensors.tar",
        },
    ],
    "VAE": [
        {
            "name": "stage_a.safetensors",
            "url": "https://replicate.delivery/pbxt/KYRedsZRf7cN7VMBqa4qK5Hafyc9fodLgghIHTWW7KcCABIx/upload.tar",
        }
    ],
    "LORAS": [
        {
            "name": "DAtattooV5.safetensors",
            "url": "https://replicate.delivery/pbxt/LUdrvm2rWf8GH7fjOaqHboDoifpkLpnPz3NKSTum71etL8Of/upload.tar",
        },
        {
            "name": "tattoo/NST/NST_5.safetensors",
            "url": "https://replicate.delivery/pbxt/LXFJf7OSzS1mpSr6BKuBSGzms7L2Hmay9qeomEJ4B4R0cktJ/upload.tar",
        },
        {
            "name": "Xian-T_handfix.safetensors",
            "url": "https://replicate.delivery/pbxt/MUk9AHx0BQLgVN5rfQba0kRwDdE1IAb1t6D5AKCYGZiU55pF/upload.tar",
        },
    ],
    "CLIP": [
        {
            "name": "t5xxl_fp8.safetensors",
            "url": "https://replicate.delivery/pbxt/MZP3pMBlSM6sFAYnOjosF5deF7lcP865WXqv1zCv9md13vnL/upload.tar",
        }
    ],
    "CLIP_VISION": [
        {
            "name": "clip-vit-large-patch14-1.bin",
            "url": "https://replicate.delivery/pbxt/M3UHdlSGlJTLLH04hKRkkayPFYtmkSM3F8sE4PQn3Ggz1ZY0/upload.tar",
        },
        {
            "name": "siglip-so400m-patch14-384.safetensors",
            "url": "https://replicate.delivery/pbxt/MZN9ZOsYucYVRSvlMfMyglRDTHe3KyoD1nlwbxnweU3AH2rT/upload.tar",
        },
    ],
    "CONTROLNET": [
        {
            "name": "diffusion_pytorch_model.safetensors",
            "url": "https://chatgenius.idealabs.mobi/genius/model/diffusion_pytorch_model.safetensors.tar",
        }
    ],
    "INSTANTID": [
        {
            "name": "ip-adapter.bin",
            "url": "https://chatgenius.idealabs.mobi/genius/model/ip-adapter.bin.tar",
        }
    ],
    "xlabs/ipadapters": [
        {
            "name": "flux-ip-adapter-v2.safetensors",
            "url": "https://replicate.delivery/pbxt/M3Bxrk7TFKBEOkmilISb4NEkYy2oheShhCsfZABfWSgTL1fv/upload.tar",
        }
    ],
    "LLavacheckpoints": [
        {
            "name": "files_for_uform_gen2_qwen",
            "url": "https://replicate.delivery/pbxt/MVtAHg5JIWJlOlfJQv9O82OlEeWegM9UwprR2Ifg7RkXbCht/upload.tar",
        }
    ],
}


def convert_custom_weights_format(custom_weights):
    """Convert custom weights format to ComfyUI compatible format"""
    converted = {}
    # Convert CHECKPOINTS
    if "CHECKPOINTS" in custom_weights:
        for item in custom_weights["CHECKPOINTS"]:
            converted[item["name"]] = {
                "url": item["url"],
                "dest": "ComfyUI/models/checkpoints"
            }

    # Convert VAE
    if "VAE" in custom_weights:
        for item in custom_weights["VAE"]:
            converted[item["name"]] = {
                "url": item["url"],
                "dest": "ComfyUI/models/vae"
            }

    # Convert LORAS
    if "LORAS" in custom_weights:
        for item in custom_weights["LORAS"]:
            converted[item["name"]] = {
                "url": item["url"],
                "dest": "ComfyUI/models/loras"
            }

    # Convert CLIP_VISION
    if "CLIP_VISION" in custom_weights:
        for item in custom_weights["CLIP_VISION"]:
            converted[item["name"]] = {
                "url": item["url"],
                "dest": "ComfyUI/models/clip_vision"
            }

    # Convert CLIP
    if "CLIP" in custom_weights:
        for item in custom_weights["CLIP"]:
            converted[item["name"]] = {
                "url": item["url"],
                "dest": "ComfyUI/models/clip"
            }

    # Convert CONTROLNET
    if "CONTROLNET" in custom_weights:
        for item in custom_weights["CONTROLNET"]:
            converted[item["name"]] = {
                "url": item["url"],
                "dest": "ComfyUI/models/controlnet"
            }

    # Convert INSTANTID
    if "INSTANTID" in custom_weights:
        for item in custom_weights["INSTANTID"]:
            converted[item["name"]] = {
                "url": item["url"],
                "dest": "ComfyUI/models/instantid"
            }

    # Convert xlabs/ipadapters
    if "xlabs/ipadapters" in custom_weights:
        for item in custom_weights["xlabs/ipadapters"]:
            converted[item["name"]] = {
                "url": item["url"],
                "dest": "ComfyUI/models/xlabs/ipadapters"
            }

    # Convert LLavacheckpoints
    if "LLavacheckpoints" in custom_weights:
        for item in custom_weights["LLavacheckpoints"]:
            converted[item["name"]] = {
                "url": item["url"],
                "dest": "ComfyUI/models/llava"
            }

    return converted


def contact_with_custom_weights(weights_manifest):
    """Contact with custom weights"""
    # Ensure we're working with a mutable dictionary
    if not isinstance(weights_manifest, dict):
        weights_manifest = dict(weights_manifest)
    
    converted = convert_custom_weights_format(local_custom_weights)
    print("Converted custom weights:", converted)
    print("Original weights_manifest:", weights_manifest)
    
    # Update the dictionary
    for key, value in converted.items():
        weights_manifest[key] = value
    
    print("Updated weights_manifest:", weights_manifest)
    return weights_manifest
