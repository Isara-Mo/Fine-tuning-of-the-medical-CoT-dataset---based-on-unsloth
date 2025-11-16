from unsloth import FastLanguageModel

max_seq_length = 2048
dtype=None          # 设置数据类型,None为不指定
load_in_4bit=False  # 是否加载4bit数据

model,tokenizer=FastLanguageModel.from_pretrained(
    model_name="/home/isara/LLM/DeepSeek-R1-Distill-Qwen-7B",
    max_seq_length=max_seq_length,
    dtype=dtype,
    load_in_4bit=load_in_4bit,
)

FastLanguageModel.for_inference(model)      #将模型设置为推理模式

question="请问如何证明根号2为无理数？"
inputs=tokenizer([question],return_tensors="pt").to("cuda")
outputs=model==model.generate(
    input_ids=inputs.input_ids,
    max_new_tokens=max_seq_length,
    use_cache=True
)

