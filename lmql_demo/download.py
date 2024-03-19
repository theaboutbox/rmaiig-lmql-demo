import requests
import os
from rich.progress import (
    Progress,
    TextColumn,
    BarColumn,
    DownloadColumn,
    TransferSpeedColumn,
    TimeRemainingColumn,
)


def download_file_with_progress(url: str, filename: str):
    """
    Downloads a file from a given URL and tracks the progress with a Rich progress bar.

    :param url: URL of the file to download.
    :param filename: Name of the file to save the download as.
    """
    # If the file exists, print a message and return early
    if os.path.exists(filename):
        print(f"The file '{filename}' already exists.")
        return

    with requests.get(url, stream=True) as response:
        response.raise_for_status()  # Check for request errors
        total_size_in_bytes = int(response.headers.get("content-length", 0))
        chunk_size = 8192  # Define the chunk size

        # Set up the Rich progress bar
        progress = Progress(
            TextColumn("[bold blue]{task.fields[filename]}", justify="right"),
            BarColumn(bar_width=None),
            DownloadColumn(),
            TransferSpeedColumn(),
            TimeRemainingColumn(),
            "[progress.percentage]{task.percentage:>3.0f}%",
        )

        # Start the download and track progress
        with progress:
            download_task = progress.add_task(
                "Download", total=total_size_in_bytes, filename=filename
            )
            with open(filename, "wb") as file:
                for chunk in response.iter_content(chunk_size=chunk_size):
                    file.write(chunk)
                    progress.update(download_task, advance=len(chunk))


def download_model(family, filename):
    output_path = f"llama2/{filename}"
    download_file_with_progress(
        f"https://huggingface.co/{family}/resolve/main/{filename}", output_path
    )
    return output_path


def download_llama2():
    return download_model("TheBloke/Llama-2-7B-GGUF", "llama-2-7b.Q4_K_M.gguf")


def download_mistral():
    return download_model("TheBloke/Mistral-7B-v0.1-GGUF", "mistral-7b-v0.1.Q4_K_M.gguf")
