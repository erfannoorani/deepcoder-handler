import runpod
from vllm import LLM, SamplingParams

# Initialize the model
llm = LLM(model="agentica-org/DeepCoder-14B-Preview", model_dir="/runpod-volume/hf-cache")

def handler(job):
    job_input = job["input"]
    prompt = job_input.get("prompt", "Write a Python function to sort a list.")
    sampling_params = SamplingParams(temperature=0.7, max_tokens=512)
    outputs = llm.generate([prompt], sampling_params)
    return {"output": outputs[0].outputs[0].text}

runpod.serverless.start({"handler": handler})
