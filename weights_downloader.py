import subprocess
import time
import os
from weights_manifest import WeightsManifest


class WeightsDownloader:
    supported_filetypes = [
        ".ckpt",
        ".safetensors",
        ".sft",
        ".pt",
        ".pth",
        ".bin",
        ".onnx",
        ".torchscript",
        ".engine",
        ".patch",
    ]

    def __init__(self):
        self.weights_manifest = WeightsManifest()
        self.weights_map = self.weights_manifest.weights_map

    def get_canonical_weight_str(self, weight_str):
        return self.weights_manifest.get_canonical_weight_str(weight_str)

    def get_weights_by_type(self, type):
        return self.weights_manifest.get_weights_by_type(type)

    def download_weights(self, weight_str):
        if weight_str in self.weights_map:
            if self.weights_manifest.is_non_commercial_only(weight_str):
                print(
                    f"⚠️  {weight_str} is for non-commercial use only. Unless you have obtained a commercial license.\nDetails: https://github.com/replicate/cog-comfyui/blob/main/weights_licenses.md"
                )

            if isinstance(self.weights_map[weight_str], list):
                for weight in self.weights_map[weight_str]:
                    self.download_if_not_exists(
                        weight_str, weight["url"], weight["dest"]
                    )
            else:
                self.download_if_not_exists(
                    weight_str,
                    self.weights_map[weight_str]["url"],
                    self.weights_map[weight_str]["dest"],
                )
        else:
            raise ValueError(
                f"{weight_str} unavailable. View the list of available weights: https://github.com/replicate/cog-comfyui/blob/main/supported_weights.md"
            )

    def check_if_file_exists(self, weight_str, dest):
        if dest.endswith(weight_str):
            path_string = dest
        else:
            path_string = os.path.join(dest, weight_str)
        return os.path.exists(path_string)

    def download_if_not_exists(self, weight_str, url, dest):
        if self.check_if_file_exists(weight_str, dest):
            print(f"✅ {weight_str} exists in {dest}")
            return
        WeightsDownloader.download(weight_str, url, dest)

    @staticmethod
    def download(weight_str, url, dest):
        if "/" in weight_str:
            subfolder = weight_str.rsplit("/", 1)[0]
            dest = os.path.join(dest, subfolder)
            os.makedirs(dest, exist_ok=True)

        # Construct the full destination path including the filename
        dest_path = os.path.join(dest, os.path.basename(weight_str))
        print(f"⏳ Downloading {weight_str} to {dest_path}")
        start = time.time()
        
        # Check if the file is a tar archive or needs extraction
        is_tar = url.endswith(('.tar', '.tar.gz', '.tgz', '.tar.bz2', '.tbz2'))
        needs_extraction = is_tar
        
        try:
            # Use appropriate flags based on file type
            if needs_extraction:
                # For tar archives, use -xf and point to the directory
                subprocess.check_call(
                    ["pget", "--log-level", "warn", "-xf", url, dest], close_fds=False
                )
            else:
                # For all other files, use -f and point to the full file path
                subprocess.check_call(
                    ["pget", "--log-level", "warn", "-f", url, dest_path], close_fds=False
                )
                
            elapsed_time = time.time() - start
            try:
                if os.path.exists(dest_path):
                    file_size_bytes = os.path.getsize(dest_path)
                    file_size_megabytes = file_size_bytes / (1024 * 1024)
                    print(
                        f"✅ {weight_str} downloaded to {dest} in {elapsed_time:.2f}s, size: {file_size_megabytes:.2f}MB"
                    )
                else:
                    print(f"⚠️ File not found at expected path: {dest_path}")
                    print(f"✅ {weight_str} downloaded to {dest} in {elapsed_time:.2f}s")
            except (FileNotFoundError, OSError) as e:
                print(f"⚠️ Error checking file size: {str(e)}")
                print(f"✅ {weight_str} downloaded to {dest} in {elapsed_time:.2f}s")
        except subprocess.CalledProcessError as e:
            print(f"Failed to download {weight_str}: {str(e)}")
            raise

    def delete_weights(self, weight_str):
        if weight_str in self.weights_map:
            weight_path = os.path.join(self.weights_map[weight_str]["dest"], weight_str)
            if os.path.exists(weight_path):
                os.remove(weight_path)
                print(f"Deleted {weight_path}")
