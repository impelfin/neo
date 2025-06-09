from huggingface_hub import hf_hub_download

model_id = 'meta-llama/Llama-3.2-1B'
snapshot_download(
    repo_id=model_id, 
    local_dir='/Users/Lune/Documents/Github/ai-3/ollama/finetuning/',
    local_dir_use_symlinks=False,
    revision='main'
)
